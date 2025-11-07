"""
Compatibility layer for httpx v1 to provide the 0.28 API.

This module provides AsyncClient as an alias to ahttpx.Client
and adds missing exception types that were present in 0.28.
"""
import ahttpx
from ._streams import ByteStream


# Create AsyncClient as an alias to ahttpx.Client
# and monkey-patch it to add aclose() as an alias for close()
class AsyncClient(ahttpx.Client):
    """Async HTTP client with 0.28 API compatibility."""
    
    async def aclose(self):
        """Alias for close() to maintain 0.28 API compatibility."""
        await self.close()


# OpenTelemetry instrumentation compatibility
# httpx v1 only has ByteStream, but instrumentation expects SyncByteStream and AsyncByteStream
SyncByteStream = ByteStream
AsyncByteStream = ByteStream


# Add missing exception types from 0.28 that may be used in the codebase
class ReadTimeout(Exception):
    """Raised when a read operation times out."""


class ConnectTimeout(Exception):
    """Raised when a connection times out."""


class WriteTimeout(Exception):
    """Raised when a write operation times out."""


class PoolTimeout(Exception):
    """Raised when the connection pool times out."""


class NetworkError(Exception):
    """Base class for network-related errors."""


class ConnectError(NetworkError):
    """Raised when a connection cannot be established."""


class ReadError(NetworkError):
    """Raised when a read operation fails."""


class WriteError(NetworkError):
    """Raised when a write operation fails."""


class CloseError(NetworkError):
    """Raised when closing a connection fails."""


class ProtocolError(Exception):
    """Raised when a protocol error occurs."""


class DecodingError(Exception):
    """Raised when response decoding fails."""


class TooManyRedirects(Exception):
    """Raised when too many redirects occur."""


class InvalidURL(Exception):
    """Raised when an invalid URL is provided."""


class CookieConflict(Exception):
    """Raised when there is a cookie conflict."""


class StreamError(Exception):
    """Raised when a stream operation fails."""


class StreamConsumed(StreamError):
    """Raised when attempting to read from an already consumed stream."""


class ResponseNotRead(Exception):
    """Raised when response content is accessed before being read."""


class RequestNotRead(Exception):
    """Raised when request content is accessed before being read."""


class HTTPStatusError(Exception):
    """Raised when an HTTP status indicates an error."""

    def __init__(self, message, *, request=None, response=None):
        self.request = request
        self.response = response
        super().__init__(message)


class HTTPError(Exception):
    """Base class for HTTP-related errors."""


class RequestError(HTTPError):
    """Base class for request-related errors."""


class TransportError(RequestError):
    """Base class for transport-related errors."""


class TimeoutException(HTTPError):
    """Base class for timeout errors."""
