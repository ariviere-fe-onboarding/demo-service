"""Health metadata for service integrations."""


def health_status():
    """Return static service metadata, not a dependency readiness probe."""
    return {"service": "demo-service", "status": "ok", "version": "1.0.0"}
