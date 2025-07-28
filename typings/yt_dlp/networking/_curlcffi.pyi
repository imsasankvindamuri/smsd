import curl_cffi as curl_cffi
import curl_cffi.requests
import io
from ..dependencies import certifi as certifi
from ..utils import int_or_none as int_or_none
from ..utils.networking import select_proxy as select_proxy
from ._helper import InstanceStoreMixin as InstanceStoreMixin
from .common import Features as Features, Request as Request, Response as Response, register_preference as register_preference, register_rh as register_rh
from .exceptions import CertificateVerifyError as CertificateVerifyError, HTTPError as HTTPError, IncompleteRead as IncompleteRead, ProxyError as ProxyError, SSLError as SSLError, TransportError as TransportError
from .impersonate import ImpersonateRequestHandler as ImpersonateRequestHandler, ImpersonateTarget as ImpersonateTarget
from _typeshed import Incomplete

curl_cffi_version: Incomplete

class CurlCFFIResponseReader(io.IOBase):
    bytes_read: int
    def __init__(self, response: curl_cffi.requests.Response) -> None: ...
    def readable(self): ...
    def read(self, size=None): ...
    def close(self) -> None: ...

class CurlCFFIResponseAdapter(Response):
    fp: CurlCFFIResponseReader
    def __init__(self, response: curl_cffi.requests.Response) -> None: ...
    def read(self, amt=None): ...

BROWSER_TARGETS: dict[tuple[int, ...], dict[str, ImpersonateTarget]]

class CurlCFFIRH(ImpersonateRequestHandler, InstanceStoreMixin):
    RH_NAME: str
    def send(self, request: Request) -> Response: ...

def curl_cffi_preference(rh, request): ...
