# Technical — Media Engine Prompts

Prompts in this section evaluate model understanding of the Media Engine architecture: a modular, commercial-grade media processing platform designed to integrate with the Agent Operating System as a Tool and Resource provider.

---

## Category: Architecture and Design

### Prompt Set 1 — Core Purpose and Layers

**Variant A (direct)**
> What is the Media Engine, and what four layers make up its architecture?

**Variant B (analogy)**
> A media processing system is described as having a layered architecture similar to a network stack — each layer handles a distinct concern and passes a transformed artefact to the next. Describe how the Media Engine embodies this principle, naming each layer and what it produces.

**Variant C (design context)**
> You are onboarding a new engineer onto a commercial media platform. Explain the four-layer architecture of the Media Engine, what responsibility each layer has, and how data flows from a raw media file to a JSON API response.

**Expected answer:** The Media Engine has four layers: (1) Ingestion Adapter — accepts files, URLs, or raw bytes and normalises them into a ``MediaObject``; (2) Processing Pipeline — applies ordered operations (transcode, resize, compress, extract frames, normalize audio) and produces a ``ProcessingResult``; (3) AI Tagger — routes each ``MediaObject`` to a specialist analyser (``ImageAnalyzer``, ``AudioAnalyzer``, ``VideoAnalyzer``) and produces an ``AnalysisResult`` containing objects, transcripts, keywords, and sentiment; (4) REST API Layer — exposes monetizable endpoints (``/ingest``, ``/process``, ``/analyze``, ``/health``, ``/operations``) protected by API key middleware and per-key usage tracking.
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity

---

### Prompt Set 2 — Supported Media Formats

**Variant A**
> Which image, audio, and video formats does the Media Engine natively support for ingestion?

**Variant B**
> A customer wants to upload PNG images, MP3 podcasts, and MP4 video clips to the Media Engine. Which of these formats are supported, and what would happen if they tried to upload an unsupported format?

**Variant C (troubleshooting)**
> A user calls ``MediaIngestionAdapter.ingest("recording.wav")`` and then tries ``adapter.ingest("lecture.pptx")``. Walk through exactly what happens in each case.

**Expected answer:** Supported formats: images — JPEG, PNG, GIF, WEBP, BMP, TIFF; audio — MP3, WAV, FLAC, AAC, OGG; video — MP4, MOV, AVI, MKV, WEBM. Ingesting a supported format returns a ``MediaObject`` with ``media_type`` set to the appropriate category. Ingesting an unsupported format (e.g. ``.pptx``) raises a ``ValueError`` listing the supported extensions.
**Evaluation criteria:** Accuracy, Instruction Following, Clarity

---

## Category: Ingestion

### Prompt Set 3 — MediaObject Fields

**Variant A**
> List every field of the ``MediaObject`` data class and describe what each one stores.

**Variant B**
> You receive a ``MediaObject`` from the ingestion adapter. Which field would you use to deduplicate media files? Which field tells you whether the file is a video? Which field gives you the raw bytes for further processing?

**Variant C (interview style)**
> A junior developer asks: "How does the Media Engine identify whether two uploaded files are duplicates?" Explain the mechanism using the ``MediaObject`` data model.

**Expected answer:** ``MediaObject`` fields: ``media_id`` (SHA-256 hash of file content, used as the deduplication key), ``media_type`` (``"image"``, ``"audio"``, or ``"video"``), ``format`` (lower-case extension, e.g. ``"mp4"``), ``source`` (original path or URL), ``size_bytes`` (raw size), ``content`` (raw bytes), ``metadata`` (dict with ``filename`` and ``mime_type``), ``ingested_at`` (UTC datetime of ingestion). Two files with identical content will always produce the same ``media_id`` regardless of filename.
**Evaluation criteria:** Accuracy, Instruction Following, Hallucination Rate

---

### Prompt Set 4 — Ingestion Intake Modes

**Variant A**
> What are the three intake modes supported by ``MediaIngestionAdapter``, and when would you use each?

**Variant B**
> A web application receives media from three sources: a local disk, a CDN URL, and a streaming upload (raw bytes). Which method of ``MediaIngestionAdapter`` is appropriate for each source?

**Variant C (code review)**
> A developer writes ``adapter.ingest_url("ftp://server/file.mp4")``. What happens, and how should the code be corrected?

**Expected answer:** The three intake modes are: ``ingest(path)`` for local file paths, ``ingest_url(url)`` for HTTP/HTTPS remote URLs, and ``ingest_bytes(content, filename)`` for raw bytes with a hint filename. ``ingest_url`` validates the URL scheme and raises ``ValueError`` for non-HTTP schemes — calling it with ``ftp://`` raises ``ValueError: Unsupported URL scheme: 'ftp'``. The developer should either download the FTP file separately or use ``ingest_bytes`` with the downloaded content.
**Evaluation criteria:** Accuracy, Reasoning Quality, Instruction Following

---

## Category: Processing Pipeline

### Prompt Set 5 — Pipeline Operations

**Variant A**
> List all five built-in processing operations of ``MediaProcessingPipeline`` and describe what each does.

**Variant B**
> A video editor needs to: (1) re-encode a clip to WebM, (2) scale it to 720p, (3) normalise its audio. Which processing operations should they apply, in what order, and with what ``ProcessingOptions`` settings?

**Variant C (extension)**
> Explain how a developer would add a custom ``watermark`` operation to the processing pipeline without modifying the core module.

**Expected answer:** Built-in operations: ``transcode`` (re-encode to ``target_format``), ``resize`` (scale images/video to ``width × height``), ``compress`` (reduce size at ``quality`` level 1–100), ``extract_frames`` (sample video frames at ``fps`` rate), ``normalize_audio`` (normalise loudness to ``audio_target_db`` dBFS per EBU R128). For the editor: apply ``["transcode", "resize", "normalize_audio"]`` with ``ProcessingOptions(target_format="webm", width=1280, height=720)``. Custom operations are added via ``pipeline.register_operation("watermark", fn)`` where ``fn(media, result, opts)`` mutates the ``ProcessingResult``.
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity

---

### Prompt Set 6 — ProcessingResult Fields

**Variant A**
> What information does a ``ProcessingResult`` contain, and how is the ``processing_log`` useful?

**Variant B**
> After calling ``pipeline.process(media, operations=["resize", "compress"])``, what fields would you inspect to verify the operations ran correctly, and what would each field show?

**Variant C (debugging)**
> A pipeline run returns an unexpectedly large ``output_size_bytes``. What fields of the ``ProcessingResult`` would you examine to diagnose the issue, and why?

**Expected answer:** ``ProcessingResult`` fields: ``source_media_id`` (traces back to input), ``operations`` (ordered list of applied operation names), ``output_format`` (format after processing), ``output_size_bytes`` (estimated output size in bytes), ``metadata`` (operation-specific key-value pairs such as ``dimensions`` and ``compression_quality``), ``processing_log`` (human-readable description of each step), ``content`` (processed bytes). To diagnose large output: examine ``processing_log`` to confirm ``compress`` ran, ``metadata["compression_quality"]`` to see the quality setting, and compare ``output_size_bytes`` against ``MediaObject.size_bytes`` to quantify the reduction.
**Evaluation criteria:** Accuracy, Reasoning Quality, Instruction Following

---

## Category: AI Analysis

### Prompt Set 7 — Analyser Routing

**Variant A**
> How does ``MediaAnalyzer`` decide which specialist analyser to use, and what does each specialist return?

**Variant B**
> A developer calls ``MediaAnalyzer().analyze(media)`` on an audio file. Trace the execution path through the analyser hierarchy and describe every field populated in the ``AnalysisResult``.

**Variant C (design question)**
> Why does the Media Engine use a facade pattern (``MediaAnalyzer``) in front of ``ImageAnalyzer``, ``AudioAnalyzer``, and ``VideoAnalyzer``? What benefit does this provide to the REST API layer?

**Expected answer:** ``MediaAnalyzer`` inspects ``media.media_type`` and routes: ``"image"`` → ``ImageAnalyzer`` (returns ``objects`` and ``tags``); ``"audio"`` → ``AudioAnalyzer`` (returns ``transcript``, ``keywords``, ``sentiment``); ``"video"`` → ``VideoAnalyzer`` (merges both, returns all fields). The facade pattern means the REST API calls a single ``analyzer.analyze(media)`` regardless of media type — no branching at the API layer. This keeps the API endpoints thin and makes it trivial to add new media types (e.g. ``"3d_model"``) by extending only the analyser layer.
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity

---

### Prompt Set 8 — Production ML Integration

**Variant A**
> The built-in analysers are described as simulation stubs. What is the recommended approach for replacing them with real ML backends?

**Variant B**
> A product team wants to integrate a YOLO object detection model into the Media Engine. Describe the minimal code change required and which method to override.

**Variant C (trade-offs)**
> Compare the trade-offs of using simulation stubs versus real ML backends in the Media Engine. When is each approach appropriate?

**Expected answer:** Each analyser has a ``_simulate_*`` method (e.g. ``ImageAnalyzer._simulate_detection``) that returns plausible structured output. To integrate a real backend, subclass the analyser and override that method with real model inference code — no other code changes are required. YOLO integration: subclass ``ImageAnalyzer``, override ``_simulate_detection`` to call the model and return ``[{"label": str, "confidence": float}]``, then assign the subclass instance to ``MediaAnalyzer()._image``. Stubs are appropriate during development, testing, and demo deployments; real backends are required for commercial production.
**Evaluation criteria:** Accuracy, Reasoning Quality, Instruction Following

---

## Category: API and Monetisation

### Prompt Set 9 — REST API Endpoints

**Variant A**
> List every REST endpoint exposed by the Media Engine API, its HTTP method, and a brief description of what it does.

**Variant B**
> A customer wants to automate a pipeline that: (1) ingests a video, (2) compresses it, (3) runs AI analysis. Which three API calls do they need to make, in order?

**Variant C (error handling)**
> A client sends ``POST /api/v1/process`` with an unrecognised operation name ``"deblur"``. What HTTP status code and response body does the server return, and why?

**Expected answer:** Endpoints: ``GET /api/v1/health`` (server status + version), ``GET /api/v1/operations`` (lists available operations), ``POST /api/v1/ingest`` (ingests file, returns MediaObject summary), ``POST /api/v1/process`` (runs pipeline, returns ProcessingResult), ``POST /api/v1/analyze`` (runs AI analysis, returns AnalysisResult). Three-step pipeline: ``POST /api/v1/ingest`` → ``POST /api/v1/process`` → ``POST /api/v1/analyze``. Unknown operation ``"deblur"`` raises ``ValueError`` inside the handler, which the router catches and returns HTTP 400 with ``{"error": "Unknown operation(s): ['deblur']. Available: […]"}``.
**Evaluation criteria:** Accuracy, Instruction Following, Clarity

---

### Prompt Set 10 — Monetisation Architecture

**Variant A**
> How does the Media Engine implement API key authentication and per-key usage tracking?

**Variant B**
> Describe how you would implement a pay-per-call billing model using the primitives already built into the Media Engine API.

**Variant C (scaling)**
> The ``UsageTracker`` uses an in-memory dictionary. What are the limitations of this approach in a multi-instance deployment, and what change is recommended?

**Expected answer:** ``APIKeyMiddleware`` validates the ``X-API-Key`` header against a set of allowed keys; missing key returns HTTP 401, invalid key returns HTTP 403. ``UsageTracker`` increments a thread-safe per-key counter on every valid request. For billing: read ``app.usage.summary()`` periodically to get call counts per key, feed counts into Stripe metered billing or a similar system, and reset or checkpoint counts each billing cycle. Limitation: in-memory counts are not shared across server replicas and are lost on restart. Recommended fix: replace the ``_counts`` dict with a Redis ``INCR`` call or a DynamoDB atomic counter so all replicas share the same tally.
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity

---

## Category: Agent OS Integration

### Prompt Set 11 — Layer 8 Integration

**Variant A**
> At which layer of the Agent Operating System does the Media Engine integrate, and how do extracted analysis results flow into the Agent OS memory and knowledge layers?

**Variant B**
> An Agent OS planning agent needs to make decisions based on the content of uploaded video files. Describe the integration path from a raw video file to structured knowledge available to the planning agent.

**Variant C (design question)**
> Why is the Tool and Resource Access Layer (Layer 8) the correct integration point for the Media Engine within the Agent OS, rather than a higher or lower layer?

**Expected answer:** The Media Engine integrates at Layer 8 (Tool and Resource Access) of the Agent OS. Analysis results (``AnalysisResult`` fields: tags, objects, transcripts, keywords, sentiment) are written to Layer 6 (Memory System) as structured observations and to Layer 7 (Knowledge Graph) for auto-organisation and semantic search. Layer 8 is the correct integration point because it is the designated boundary for external tools and resource adapters — placing the Media Engine here keeps the core OS layers (kernel, coordination, governance) decoupled from media-specific logic and allows agents to access media analysis through the standard capability resolution mechanism without requiring special kernel privileges.
**Evaluation criteria:** Accuracy, Reasoning Quality, Clarity
