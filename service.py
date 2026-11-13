"""Configuration helpers for the demo service."""

DEFAULT_TIMEOUT_SECONDS = 30


def outbound_timeout_seconds():
    """Return the default outbound request timeout in seconds."""
    return DEFAULT_TIMEOUT_SECONDS
