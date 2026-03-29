# Media Engine

A **commercial-grade, modular media processing platform** built for the Agent Operating System ecosystem.  The Media Engine handles multi-modal data (images, audio, and video) from ingestion through AI-driven analysis and exposes the entire pipeline via a monetizable REST API.

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Module Reference](#module-reference)
   - [Ingestion](#ingestion)
   - [Processing](#processing)
   - [AI Tagger](#ai-tagger)
   - [API Endpoints](#api-endpoints)
4. [Quick Start](#quick-start)
5. [REST API Reference](#rest-api-reference)
6. [Monetisation](#monetisation)
7. [Integration with Agent OS](#integration-with-agent-os)
8. [Extending the Platform](#extending-the-platform)
9. [Deployment](#deployment)

---

## Overview

The Media Engine is a four-layer platform:

```
┌──────────────────────────────────────────────────────┐
│                  REST API Layer                      │  ← monetizable endpoints
│  /ingest  /process  /analyze  /health  /operations   │
├──────────────────────────────────────────────────────┤
│               AI Tagger Layer                        │  ← object detection,
│  ImageAnalyzer · AudioAnalyzer · VideoAnalyzer       │     speech-to-text,
│  SentimentAnalyzer · MediaAnalyzer (facade)          │     sentiment analysis
├──────────────────────────────────────────────────────┤
│             Processing Pipeline Layer                │  ← transcode, resize,
│  MediaProcessingPipeline · ProcessingOptions         │     compress, extract
├──────────────────────────────────────────────────────┤
│              Ingestion Adapter Layer                 │  ← file path, URL,
│  MediaIngestionAdapter · MediaObject                 │     raw bytes
└──────────────────────────────────────────────────────┘
```

### Supported Formats

| Type  | Formats                                |
|-------|----------------------------------------|
| Image | JPEG, PNG, GIF, WEBP, BMP, TIFF        |
| Audio | MP3, WAV, FLAC, AAC, OGG               |
| Video | MP4, MOV, AVI, MKV, WEBM               |

---

## Architecture

### Design Principles

| Principle      | Implementation                                                   |
|----------------|------------------------------------------------------------------|
| Modularity     | Each layer is an independent Python package with a stable interface. |
| Pluggability   | Every analyser and pipeline operation can be swapped for a real ML backend without changing calling code. |
| Zero mandatory dependencies | Core logic uses only the Python standard library. |
| Monetisation-first | API key validation and per-key usage tracking are built in. |

### Data Flow

```
Media File / URL / Bytes
         │
         ▼
 MediaIngestionAdapter
         │  produces MediaObject
         ▼
 MediaProcessingPipeline      (optional — transcode / resize / compress)
         │  produces ProcessingResult
         ▼
    MediaAnalyzer             (optional — AI tagging)
         │  produces AnalysisResult
         ▼
 REST API Response (JSON)
```

---

## Module Reference

### Ingestion

**Package:** `media_engine.ingestion`

**`MediaIngestionAdapter`** — three intake modes:

| Method                          | Description                          |
|---------------------------------|--------------------------------------|
| `ingest(path)`                  | Local file path (`str` or `Path`).   |
| `ingest_url(url, timeout=30)`   | Remote HTTP/HTTPS URL.               |
| `ingest_bytes(content, filename)` | Raw `bytes` with a hint filename.  |

All methods return a **`MediaObject`** with fields:

| Field         | Type       | Description                                      |
|---------------|------------|--------------------------------------------------|
| `media_id`    | `str`      | SHA-256 hash of file content (deduplication key).|
| `media_type`  | `str`      | `"image"`, `"audio"`, or `"video"`.              |
| `format`      | `str`      | Lower-case extension (e.g. `"mp4"`, `"png"`).    |
| `source`      | `str`      | Original path or URL.                            |
| `size_bytes`  | `int`      | Raw size in bytes.                               |
| `content`     | `bytes`    | Raw file bytes.                                  |
| `metadata`    | `dict`     | `filename`, `mime_type`, and any extras.         |
| `ingested_at` | `datetime` | UTC timestamp.                                   |

---

### Processing

**Package:** `media_engine.processing`

**`MediaProcessingPipeline`** — sequential operation runner.

```python
result = pipeline.process(
    media,
    operations=["resize", "compress"],
    options=ProcessingOptions(width=1280, height=720, quality=75),
)
```

**Built-in operations:**

| Operation         | Applicable To       | Description                                   |
|-------------------|---------------------|-----------------------------------------------|
| `transcode`       | image, audio, video | Re-encode to `target_format`.                 |
| `resize`          | image, video        | Scale to `width × height`.                    |
| `compress`        | image, audio, video | Reduce size at `quality` level (1–100).       |
| `extract_frames`  | video               | Sample frames at `fps` rate.                  |
| `normalize_audio` | audio, video        | Normalise loudness to `audio_target_db` dBFS. |

**`ProcessingOptions` fields:**

| Field            | Default   | Description                            |
|------------------|-----------|----------------------------------------|
| `target_format`  | `None`    | Output format for `transcode`.         |
| `width`          | `None`    | Target width for `resize`.             |
| `height`         | `None`    | Target height for `resize`.            |
| `quality`        | `80`      | Compression quality (1–100).           |
| `fps`            | `1`       | Frames per second for `extract_frames`.|
| `audio_target_db`| `-23.0`   | Target loudness (EBU R128).            |

**Custom operations** can be registered:

```python
def sharpen(media, result, opts):
    result.metadata["sharpened"] = True
    result.processing_log.append("sharpen: applied unsharp mask")

pipeline.register_operation("sharpen", sharpen)
```

---

### AI Tagger

**Package:** `media_engine.ai_tagger`

**`MediaAnalyzer`** — unified facade, routes to specialist analyser by `media_type`.

```python
analyzer = MediaAnalyzer()
result   = analyzer.analyze(media_object)
print(result.to_dict())
```

**Specialist analysers:**

| Analyser           | Input       | Output fields                                   |
|--------------------|-------------|-------------------------------------------------|
| `ImageAnalyzer`    | image       | `objects` (label + confidence), `tags`          |
| `AudioAnalyzer`    | audio/video | `transcript`, `keywords`, `sentiment`           |
| `VideoAnalyzer`    | video       | all of the above, merged                        |
| `SentimentAnalyzer`| text string | `{"label": "positive\|neutral\|negative", "score": float}` |

**`AnalysisResult` fields:**

| Field       | Type              | Description                              |
|-------------|-------------------|------------------------------------------|
| `media_id`  | `str`             | Source `MediaObject.media_id`.           |
| `analyzer`  | `str`             | Name of the analyser used.               |
| `tags`      | `list[str]`       | Consolidated string labels.              |
| `objects`   | `list[dict]`      | `[{"label": "…", "confidence": 0.xx}]`   |
| `transcript`| `str`             | Full text transcript.                    |
| `keywords`  | `list[str]`       | High-signal terms from transcript.       |
| `sentiment` | `dict`            | `{"label": "…", "score": float}`.        |

> **Production note:** Built-in analysers are simulation stubs.  Replace the `_simulate_*` methods with real ML backends (YOLO, Whisper, Detectron2, etc.) without changing any calling code.

---

### API Endpoints

**Package:** `media_engine.api_endpoints`

**`create_app(api_keys, host, port)`** — factory function.

```python
from media_engine.api_endpoints import create_app

app = create_app(
    api_keys={"prod-key-abc123"},  # omit for dev mode (no auth)
    host="0.0.0.0",
    port=8080,
)
app.run()   # blocks — use app.run_background() for tests
```

---

## Quick Start

```python
from media_engine.ingestion  import MediaIngestionAdapter
from media_engine.processing import MediaProcessingPipeline, ProcessingOptions
from media_engine.ai_tagger  import MediaAnalyzer

# 1. Ingest
adapter = MediaIngestionAdapter()
media   = adapter.ingest("sample.mp4")
print(media)  # MediaObject(id=3f4a1b2c…, type=video, format=mp4, size=2,048,000 bytes)

# 2. Process
pipeline = MediaProcessingPipeline()
result   = pipeline.process(
    media,
    operations=["resize", "compress"],
    options=ProcessingOptions(width=1920, height=1080, quality=80),
)
print(result.processing_log)
# ['resize: output dimensions set to 1920×1080', 'compress: quality=80%, …']

# 3. Analyse
analyzer     = MediaAnalyzer()
analysis     = analyzer.analyze(media)
print(analysis.objects)     # [{"label": "person", "confidence": 0.94}, …]
print(analysis.transcript)  # "Welcome to the Media Engine AI demonstration."
print(analysis.sentiment)   # {"label": "positive", "score": 0.75}
```

---

## REST API Reference

All endpoints accept and return **`application/json`**.  Authenticated endpoints require:

```
X-API-Key: <your-api-key>
```

### `GET /api/v1/health`

Returns server status and version.

**Response:**
```json
{ "status": "ok", "version": "1.0.0" }
```

---

### `GET /api/v1/operations`

Lists available processing operations.

**Response:**
```json
{ "operations": ["compress", "extract_frames", "normalize_audio", "resize", "transcode"] }
```

---

### `POST /api/v1/ingest`

Ingest a media file and return its metadata.

**Request:**
```json
{ "source": "/absolute/path/to/clip.mp4" }
```

**Response:**
```json
{
  "media_id": "3f4a1b2c…",
  "media_type": "video",
  "format": "mp4",
  "size_bytes": 2048000,
  "source": "/absolute/path/to/clip.mp4",
  "metadata": { "filename": "clip.mp4", "mime_type": "video/mp4" },
  "ingested_at": "2026-03-11T22:36:26.912Z"
}
```

---

### `POST /api/v1/process`

Process a media file with one or more pipeline operations.

**Request:**
```json
{
  "source": "/absolute/path/to/photo.jpg",
  "operations": ["resize", "compress"],
  "options": { "width": 800, "height": 600, "quality": 75 }
}
```

**Response:**
```json
{
  "source_media_id": "3f4a1b2c…",
  "operations": ["resize", "compress"],
  "output_format": "jpg",
  "output_size_bytes": 153600,
  "processing_log": [
    "resize: output dimensions set to 800×600",
    "compress: quality=75%, estimated size 204800 → 153600 bytes"
  ],
  "metadata": { "dimensions": "800x600", "compression_quality": 75 }
}
```

---

### `POST /api/v1/analyze`

Run AI analysis on a media file.

**Request:**
```json
{ "source": "/absolute/path/to/podcast.mp3" }
```

**Response:**
```json
{
  "media_id": "7d9e2f4a…",
  "analyzer": "audio_analyzer",
  "tags": [],
  "objects": [],
  "transcript": "Welcome to the Media Engine AI demonstration.",
  "keywords": ["welcome", "media", "engine", "demonstration"],
  "sentiment": { "label": "positive", "score": 0.75 },
  "metadata": { "format": "mp3", "source": "/absolute/path/to/podcast.mp3" }
}
```

---

## Monetisation

The API layer includes two built-in monetisation primitives:

### API Key Validation

```python
app = create_app(api_keys={"tier1-key-abc", "tier2-key-xyz"})
```

- Missing key → **401 Unauthorized**
- Invalid key  → **403 Forbidden**
- Valid key    → request proceeds

In production, replace the in-memory key set with a database-backed validator that enforces tier limits (e.g. requests per minute, monthly quotas).

### Usage Tracking

```python
print(app.usage.summary())
# {"tier1-key-abc": 142, "tier2-key-xyz": 58}
```

Each API call is counted per key.  Feed these counts into a billing pipeline (Stripe metered billing, AWS Marketplace, or a custom invoicing system) to charge customers on a **pay-per-call** model.

### Suggested Pricing Tiers

| Tier      | Monthly Price | Calls / month | Features                         |
|-----------|--------------|---------------|----------------------------------|
| Starter   | $49          | 5,000         | Ingest + process                 |
| Pro       | $199         | 50,000        | + AI analysis (image, audio)     |
| Enterprise| Custom       | Unlimited     | + video analysis, SLA, webhooks  |

---

## Integration with Agent OS

The Media Engine plugs into the Agent Operating System as a **Tool & Resource** provider at **Layer 8** (Tool and Resource Access Layer):

```
Agent OS Layer 8 (Tool and Resource Access)
        │
        ▼
Media Engine API  (POST /api/v1/analyze, etc.)
        │
        ▼
  AnalysisResult  →  Agent Memory Layer (Layer 6) as structured observation
  Tags / Transcripts → Knowledge Graph Layer (Layer 7) for auto-organisation
```

Extracted metadata (tags, objects, transcripts, sentiment) can be written directly into the Agent OS Knowledge Graph to enable:
- Semantic search over media archives.
- Automated content moderation agents.
- Media-aware planning and scheduling agents.

---

## Extending the Platform

### Swap in a real ML backend

```python
# Example: replace image analyser stub with a YOLO model
from media_engine.ai_tagger import ImageAnalyzer

class YOLOImageAnalyzer(ImageAnalyzer):
    def _simulate_detection(self, media):
        # Call your real YOLO model here
        return yolo_model.detect(media.content)

from media_engine.ai_tagger import MediaAnalyzer
analyzer = MediaAnalyzer()
analyzer._image = YOLOImageAnalyzer()
```

### Add a custom processing operation

```python
from media_engine.processing import MediaProcessingPipeline

pipeline = MediaProcessingPipeline()

def watermark(media, result, opts):
    result.metadata["watermarked"] = True
    result.processing_log.append("watermark: branding overlay applied")

pipeline.register_operation("watermark", watermark)
result = pipeline.process(media, operations=["watermark"])
```

---

## Deployment

### Local development (no auth)

```bash
python - <<'EOF'
from media_engine.api_endpoints import create_app
create_app(port=8080).run()
EOF
```

### Production (with auth)

```bash
python - <<'EOF'
from media_engine.api_endpoints import create_app
create_app(api_keys={"prod-key-abc123"}, host="0.0.0.0", port=8080).run()
EOF
```

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY media_engine/ ./media_engine/
EXPOSE 8080
CMD ["python", "-c", "from media_engine.api_endpoints import create_app; create_app(port=8080).run()"]
```

### Environment-variable key management

```python
import os
keys = set(os.environ.get("API_KEYS", "").split(","))
app = create_app(api_keys=keys or None)
```
