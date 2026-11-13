"""Request options for outbound service clients."""

from service import outbound_timeout_seconds


def client_options():
    """Return a fresh options dictionary with the configured timeout."""
    return {"timeout_seconds": outbound_timeout_seconds()}
