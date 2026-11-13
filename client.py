"""Request options for outbound service clients."""

from service import request_timeout


def client_options():
    """Return a fresh options dictionary with the configured timeout."""
    return {"timeout_seconds": request_timeout()}
