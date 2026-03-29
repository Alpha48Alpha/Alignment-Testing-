"""
Media Engine — Modular multi-modal media processing platform.

Top-level package exposing the four core sub-systems:

    ingestion       — multi-format media intake and validation
    processing      — transcoding, resizing, and compression pipeline
    ai_tagger       — AI-driven analysis (object detection, speech-to-text, sentiment)
    api_endpoints   — monetizable REST API layer

Typical usage
-------------
    from media_engine.ingestion import MediaIngestionAdapter
    from media_engine.processing import MediaProcessingPipeline
    from media_engine.ai_tagger import MediaAnalyzer
    from media_engine.api_endpoints import create_app

    adapter  = MediaIngestionAdapter()
    pipeline = MediaProcessingPipeline()
    analyzer = MediaAnalyzer()

    media    = adapter.ingest("clip.mp4")
    result   = pipeline.process(media, operations=["transcode", "compress"])
    tags     = analyzer.analyze(media)

    app = create_app()   # launch the REST API
    app.run()
"""

__version__ = "1.0.0"
__all__ = ["ingestion", "processing", "ai_tagger", "api_endpoints"]
