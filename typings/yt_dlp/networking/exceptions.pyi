from ..utils import YoutubeDLError as YoutubeDLError
from .common import RequestHandler as RequestHandler, Response as Response
from _typeshed import Incomplete

class RequestError(YoutubeDLError):
    handler: Incomplete
    cause: Incomplete
    def __init__(self, msg: str | None = None, cause: Exception | str | None = None, handler: RequestHandler = None) -> None: ...

class UnsupportedRequest(RequestError): ...

class NoSupportingHandlers(RequestError):
    unsupported_errors: Incomplete
    unexpected_errors: Incomplete
    def __init__(self, unsupported_errors: list[UnsupportedRequest], unexpected_errors: list[Exception]) -> None: ...

class TransportError(RequestError): ...

class HTTPError(RequestError):
    response: Incomplete
    status: Incomplete
    reason: Incomplete
    redirect_loop: Incomplete
    def __init__(self, response: Response, redirect_loop: bool = False) -> None: ...
    def close(self) -> None: ...

class IncompleteRead(TransportError):
    partial: Incomplete
    expected: Incomplete
    def __init__(self, partial: int, expected: int | None = None, **kwargs) -> None: ...

class SSLError(TransportError): ...
class CertificateVerifyError(SSLError): ...
class ProxyError(TransportError): ...

network_exceptions: Incomplete
