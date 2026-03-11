"""
media_engine.ai_tagger
======================
AI-driven media analysis layer.

Analysers
---------
``ImageAnalyzer``
    Object detection and keyword tagging for images.
    Returns a list of detected objects with confidence scores.

``AudioAnalyzer``
    Speech-to-text transcription and keyword extraction for audio.
    Returns a transcript string and a list of keywords.

``VideoAnalyzer``
    Per-frame scene understanding + audio transcription for videos.
    Delegates to ``ImageAnalyzer`` (frames) and ``AudioAnalyzer`` (audio track).

``SentimentAnalyzer``
    Lightweight rule-based sentiment scoring applicable to any text (e.g.
    transcripts or metadata descriptions).

``MediaAnalyzer``
    Unified facade — inspects the ``media_type`` of a ``MediaObject`` and
    routes it to the appropriate specialist analyser.

Architecture note
-----------------
All analysers are *pluggable*: they define a ``AnalyzerPlugin`` protocol so
that production deployments can swap in real ML backends (e.g. OpenAI Vision,
Whisper, YOLO) without changing the rest of the pipeline.

The built-in implementations are *simulation stubs* that demonstrate the full
interface and return plausible structured output without requiring GPU or
third-party API keys.  Replace each ``_simulate_*`` method with real inference
code when deploying commercially.

Example
-------
>>> from media_engine.ingestion import MediaIngestionAdapter
>>> from media_engine.ai_tagger import MediaAnalyzer

>>> adapter  = MediaIngestionAdapter()
>>> analyzer = MediaAnalyzer()

>>> obj  = adapter.ingest("photo.jpg")
>>> tags = analyzer.analyze(obj)
>>> print(tags["objects"])          # [{"label": "person", "confidence": 0.94}, …]
>>> print(tags["sentiment"])        # {"label": "positive", "score": 0.73}
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from media_engine.ingestion import MediaObject

# ---------------------------------------------------------------------------
# Shared data models
# ---------------------------------------------------------------------------


@dataclass
class AnalysisResult:
    """
    Structured output of an AI analysis pass.

    Attributes
    ----------
    media_id    : Identifier of the source ``MediaObject``.
    analyzer    : Name of the analyser that produced these results.
    tags        : List of string labels extracted from the media.
    objects     : Detected objects with label + confidence (images/video).
    transcript  : Full text transcript (audio/video).
    keywords    : High-signal keywords extracted from the transcript.
    sentiment   : Sentiment label and score derived from text content.
    metadata    : Additional analyser-specific key-value pairs.
    """

    media_id: str
    analyzer: str
    tags: List[str] = field(default_factory=list)
    objects: List[Dict[str, Any]] = field(default_factory=list)
    transcript: str = ""
    keywords: List[str] = field(default_factory=list)
    sentiment: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Serialise to a plain dictionary (API-friendly)."""
        return {
            "media_id": self.media_id,
            "analyzer": self.analyzer,
            "tags": self.tags,
            "objects": self.objects,
            "transcript": self.transcript,
            "keywords": self.keywords,
            "sentiment": self.sentiment,
            "metadata": self.metadata,
        }


# ---------------------------------------------------------------------------
# Sentiment helper (shared by audio/video analysers)
# ---------------------------------------------------------------------------


class SentimentAnalyzer:
    """
    Rule-based sentiment scorer for short text passages (e.g. transcripts).

    Returns a dict: ``{"label": "positive"|"neutral"|"negative", "score": float}``.
    Score is in [0, 1] where higher means more confident *positive* sentiment.

    In production replace with a fine-tuned transformer (e.g. distilbert-sst2).
    """

    _POSITIVE = {
        "good", "great", "excellent", "amazing", "wonderful", "fantastic",
        "love", "happy", "success", "benefit", "improve", "achieve", "win",
        "positive", "best", "outstanding",
    }
    _NEGATIVE = {
        "bad", "terrible", "awful", "horrible", "worst", "hate", "fail",
        "error", "loss", "problem", "issue", "broken", "negative", "poor",
        "disappointing",
    }

    def analyze_text(self, text: str) -> Dict[str, Any]:
        """Score sentiment of *text* using keyword heuristics."""
        words = set(re.findall(r"[a-z]+", text.lower()))
        pos_hits = len(words & self._POSITIVE)
        neg_hits = len(words & self._NEGATIVE)
        total = pos_hits + neg_hits
        if total == 0:
            return {"label": "neutral", "score": 0.5}
        score = pos_hits / total
        if score > 0.6:
            label = "positive"
        elif score < 0.4:
            label = "negative"
        else:
            label = "neutral"
        return {"label": label, "score": round(score, 3)}


# ---------------------------------------------------------------------------
# Image analyser
# ---------------------------------------------------------------------------


class ImageAnalyzer:
    """
    Object detection and tagging for images.

    Simulation stub
    ---------------
    Uses a deterministic pseudo-random seed derived from the media content hash
    to produce stable, reproducible simulated detections.  Replace
    ``_simulate_detection`` with a real model call (YOLO, Detectron2, etc.).
    """

    _LABEL_POOL = [
        "person", "vehicle", "building", "tree", "sky", "water", "road",
        "animal", "food", "text", "face", "product", "screen", "furniture",
    ]

    def analyze(self, media: MediaObject) -> AnalysisResult:
        """Detect objects and extract tags from an image ``MediaObject``."""
        if media.media_type != "image":
            raise ValueError(f"ImageAnalyzer expects media_type='image', got {media.media_type!r}")
        objects = self._simulate_detection(media)
        tags = sorted({obj["label"] for obj in objects})
        return AnalysisResult(
            media_id=media.media_id,
            analyzer="image_analyzer",
            objects=objects,
            tags=tags,
            metadata={"format": media.format, "source": media.source},
        )

    def _simulate_detection(self, media: MediaObject) -> List[Dict[str, Any]]:
        seed = int(media.media_id[:8], 16)
        count = (seed % 4) + 2
        results = []
        for i in range(count):
            label = self._LABEL_POOL[(seed + i * 7) % len(self._LABEL_POOL)]
            confidence = round(0.65 + ((seed + i) % 35) / 100, 2)
            results.append({"label": label, "confidence": confidence})
        return results


# ---------------------------------------------------------------------------
# Audio analyser
# ---------------------------------------------------------------------------


class AudioAnalyzer:
    """
    Speech-to-text transcription and keyword extraction for audio.

    Simulation stub
    ---------------
    In production wire this to OpenAI Whisper, Google Speech-to-Text, or
    AWS Transcribe.  The simulation produces a plausible transcript fragment
    seeded from the content hash for reproducibility.
    """

    _TRANSCRIPT_FRAGMENTS = [
        "The quick brown fox jumps over the lazy dog.",
        "Welcome to the Media Engine AI demonstration.",
        "Processing audio content with high accuracy.",
        "Speech recognition enables automated transcription at scale.",
        "This media engine supports multiple audio formats.",
    ]

    def analyze(self, media: MediaObject) -> AnalysisResult:
        """Transcribe speech and extract keywords from an audio ``MediaObject``."""
        if media.media_type not in {"audio", "video"}:
            raise ValueError(
                f"AudioAnalyzer expects media_type in {{'audio','video'}}, got {media.media_type!r}"
            )
        transcript = self._simulate_transcription(media)
        keywords = self._extract_keywords(transcript)
        sentiment_analyzer = SentimentAnalyzer()
        sentiment = sentiment_analyzer.analyze_text(transcript)
        return AnalysisResult(
            media_id=media.media_id,
            analyzer="audio_analyzer",
            transcript=transcript,
            keywords=keywords,
            sentiment=sentiment,
            metadata={"format": media.format, "source": media.source},
        )

    def _simulate_transcription(self, media: MediaObject) -> str:
        seed = int(media.media_id[:8], 16)
        fragment = self._TRANSCRIPT_FRAGMENTS[seed % len(self._TRANSCRIPT_FRAGMENTS)]
        return fragment

    @staticmethod
    def _extract_keywords(text: str) -> List[str]:
        stopwords = {
            "the", "a", "an", "is", "in", "of", "to", "and", "for",
            "with", "at", "on", "this", "that", "it", "its",
        }
        words = re.findall(r"[a-z]+", text.lower())
        seen: Dict[str, int] = {}
        for w in words:
            if w not in stopwords and len(w) > 3:
                seen[w] = seen.get(w, 0) + 1
        return sorted(seen, key=lambda w: (-seen[w], w))[:10]


# ---------------------------------------------------------------------------
# Video analyser
# ---------------------------------------------------------------------------


class VideoAnalyzer:
    """
    Scene understanding and audio transcription for video files.

    Delegates to ``ImageAnalyzer`` (for representative frame objects) and
    ``AudioAnalyzer`` (for the audio track), then merges results.
    """

    def __init__(self) -> None:
        self._image_analyzer = ImageAnalyzer()
        self._audio_analyzer = AudioAnalyzer()

    def analyze(self, media: MediaObject) -> AnalysisResult:
        """Analyse video content: extract scene objects and transcribe audio."""
        if media.media_type != "video":
            raise ValueError(f"VideoAnalyzer expects media_type='video', got {media.media_type!r}")

        # Simulate frame-based object detection by treating video as an image
        image_like = media.__class__(
            media_id=media.media_id,
            media_type="image",
            format=media.format,
            source=media.source,
            size_bytes=media.size_bytes,
            content=media.content,
            metadata=media.metadata,
        )
        image_result = self._image_analyzer.analyze(image_like)
        audio_result = self._audio_analyzer.analyze(media)

        merged_tags = sorted(set(image_result.tags + audio_result.keywords))
        return AnalysisResult(
            media_id=media.media_id,
            analyzer="video_analyzer",
            objects=image_result.objects,
            tags=merged_tags,
            transcript=audio_result.transcript,
            keywords=audio_result.keywords,
            sentiment=audio_result.sentiment,
            metadata={
                "format": media.format,
                "source": media.source,
                "frames_analyzed": 1,
            },
        )


# ---------------------------------------------------------------------------
# Unified facade
# ---------------------------------------------------------------------------


class MediaAnalyzer:
    """
    Unified analyser facade.

    Routes each ``MediaObject`` to the correct specialist analyser based on
    its ``media_type`` field.

    Example
    -------
    >>> analyzer = MediaAnalyzer()
    >>> result   = analyzer.analyze(media_obj)
    >>> print(result.to_dict())
    """

    def __init__(self) -> None:
        self._image = ImageAnalyzer()
        self._audio = AudioAnalyzer()
        self._video = VideoAnalyzer()

    def analyze(self, media: MediaObject) -> AnalysisResult:
        """Route *media* to the appropriate analyser and return results."""
        if media.media_type == "image":
            return self._image.analyze(media)
        if media.media_type == "audio":
            return self._audio.analyze(media)
        if media.media_type == "video":
            return self._video.analyze(media)
        raise ValueError(f"Unrecognised media_type: {media.media_type!r}")
