"""
media_engine.processing
=======================
Media processing pipeline — transcoding, resizing, and compression.

Architecture
------------
``MediaProcessingPipeline`` is a sequential operation runner.  Each operation
is a callable that accepts a ``ProcessingContext`` and returns a mutated copy.
Built-in operations are registered on the pipeline at construction time; custom
operations can be added via ``register_operation``.

Built-in operations
-------------------
transcode   — re-encode to a target format (simulated: updates format field).
resize      — scale images or video frames to target dimensions.
compress    — reduce file size by applying quality/bitrate reduction.
extract_frames — pull individual frames from a video at a given FPS.
normalize_audio — normalise audio loudness to a target dBFS level.

All operations are *non-destructive*: they return new ``ProcessingResult``
objects and never mutate the original ``MediaObject``.

Example
-------
>>> from media_engine.ingestion import MediaIngestionAdapter
>>> from media_engine.processing import MediaProcessingPipeline

>>> adapter  = MediaIngestionAdapter()
>>> pipeline = MediaProcessingPipeline()

>>> media  = adapter.ingest("clip.mp4")
>>> result = pipeline.process(media, operations=["transcode", "compress"])
>>> print(result.output_format)      # e.g. "mp4"
>>> print(result.processing_log)     # list of applied step descriptions
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional

from media_engine.ingestion import MediaObject

# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------


@dataclass
class ProcessingOptions:
    """
    Configuration knobs for the processing pipeline.

    Attributes
    ----------
    target_format   : Desired output format (e.g. "mp4", "webp").
    width           : Target width in pixels (resize/transcode).
    height          : Target height in pixels (resize/transcode).
    quality         : Compression quality 1–100 (higher = better, larger).
    fps             : Frames per second for frame extraction.
    audio_target_db : Target loudness in dBFS for audio normalisation.
    """

    target_format: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    quality: int = 80
    fps: int = 1
    audio_target_db: float = -23.0  # EBU R128 standard


@dataclass
class ProcessingResult:
    """
    Output of a completed processing run.

    Attributes
    ----------
    source_media_id  : ``media_id`` of the input ``MediaObject``.
    operations       : Ordered list of operation names that were applied.
    output_format    : Format of the processed output.
    output_size_bytes: Estimated size of the processed output.
    metadata         : Output-specific key-value pairs.
    processing_log   : Human-readable step-by-step description of what happened.
    content          : Processed content bytes (or original if not transformed).
    """

    source_media_id: str
    operations: List[str]
    output_format: str
    output_size_bytes: int
    metadata: dict = field(default_factory=dict)
    processing_log: List[str] = field(default_factory=list)
    content: bytes = field(default_factory=bytes)


# ---------------------------------------------------------------------------
# Built-in operation implementations
# ---------------------------------------------------------------------------


def _op_transcode(
    media: MediaObject, result: ProcessingResult, opts: ProcessingOptions
) -> None:
    """Re-encode to opts.target_format (simulation: updates metadata)."""
    if opts.target_format is None:
        result.processing_log.append("transcode: skipped (no target_format specified)")
        return
    old_fmt = result.output_format
    result.output_format = opts.target_format
    result.metadata["transcoded_from"] = old_fmt
    result.processing_log.append(
        f"transcode: {old_fmt} → {opts.target_format}"
    )


def _op_resize(
    media: MediaObject, result: ProcessingResult, opts: ProcessingOptions
) -> None:
    """Scale to target dimensions (simulation: records dimensions in metadata)."""
    if media.media_type not in {"image", "video"}:
        result.processing_log.append("resize: skipped (not applicable to audio)")
        return
    if opts.width is None and opts.height is None:
        result.processing_log.append("resize: skipped (no dimensions specified)")
        return
    w = opts.width or "auto"
    h = opts.height or "auto"
    result.metadata["dimensions"] = f"{w}x{h}"
    result.processing_log.append(f"resize: output dimensions set to {w}×{h}")


def _op_compress(
    media: MediaObject, result: ProcessingResult, opts: ProcessingOptions
) -> None:
    """Reduce file size by quality reduction (simulation: estimates new size)."""
    quality_ratio = opts.quality / 100
    estimated_size = int(media.size_bytes * quality_ratio)
    result.output_size_bytes = estimated_size
    result.metadata["compression_quality"] = opts.quality
    result.processing_log.append(
        f"compress: quality={opts.quality}%, "
        f"estimated size {media.size_bytes:,} → {estimated_size:,} bytes"
    )


def _op_extract_frames(
    media: MediaObject, result: ProcessingResult, opts: ProcessingOptions
) -> None:
    """Extract frames from video at the configured FPS."""
    if media.media_type != "video":
        result.processing_log.append("extract_frames: skipped (not a video)")
        return
    result.metadata["extracted_fps"] = opts.fps
    result.processing_log.append(
        f"extract_frames: extracting at {opts.fps} fps"
    )


def _op_normalize_audio(
    media: MediaObject, result: ProcessingResult, opts: ProcessingOptions
) -> None:
    """Normalise audio loudness to target dBFS level."""
    if media.media_type not in {"audio", "video"}:
        result.processing_log.append(
            "normalize_audio: skipped (not audio or video)"
        )
        return
    result.metadata["audio_target_db"] = opts.audio_target_db
    result.processing_log.append(
        f"normalize_audio: target loudness {opts.audio_target_db} dBFS (EBU R128)"
    )


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

OperationFn = Callable[[MediaObject, ProcessingResult, ProcessingOptions], None]


class MediaProcessingPipeline:
    """
    Sequential media processing pipeline.

    Operations are executed in the order they are listed in the ``operations``
    argument to ``process()``.  Unknown operation names raise ``ValueError``
    rather than silently skipping.

    Example
    -------
    >>> pipeline = MediaProcessingPipeline()
    >>> result = pipeline.process(
    ...     media,
    ...     operations=["resize", "compress"],
    ...     options=ProcessingOptions(width=1280, height=720, quality=75),
    ... )
    """

    _BUILTIN: Dict[str, OperationFn] = {
        "transcode": _op_transcode,
        "resize": _op_resize,
        "compress": _op_compress,
        "extract_frames": _op_extract_frames,
        "normalize_audio": _op_normalize_audio,
    }

    def __init__(self) -> None:
        self._operations: Dict[str, OperationFn] = dict(self._BUILTIN)

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register_operation(self, name: str, fn: OperationFn) -> None:
        """Add or replace a named operation in the pipeline."""
        self._operations[name] = fn

    @property
    def available_operations(self) -> List[str]:
        """Return sorted list of registered operation names."""
        return sorted(self._operations)

    # ------------------------------------------------------------------
    # Processing
    # ------------------------------------------------------------------

    def process(
        self,
        media: MediaObject,
        operations: List[str],
        options: Optional[ProcessingOptions] = None,
    ) -> ProcessingResult:
        """
        Run *operations* on *media* and return a ``ProcessingResult``.

        Parameters
        ----------
        media      : Input ``MediaObject`` (not mutated).
        operations : Ordered list of operation names to apply.
        options    : Configuration; defaults to ``ProcessingOptions()``.

        Raises
        ------
        ValueError
            If any operation name is not registered.
        """
        unknown = [op for op in operations if op not in self._operations]
        if unknown:
            raise ValueError(
                f"Unknown operation(s): {unknown}. "
                f"Available: {self.available_operations}"
            )

        opts = options or ProcessingOptions()
        result = ProcessingResult(
            source_media_id=media.media_id,
            operations=list(operations),
            output_format=media.format,
            output_size_bytes=media.size_bytes,
            metadata=copy.deepcopy(media.metadata),
            content=media.content,
        )

        for op_name in operations:
            self._operations[op_name](media, result, opts)

        return result
