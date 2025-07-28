import websockets as websockets
import websockets.sync.client
from ..utils import int_or_none as int_or_none
from ..utils.networking import select_proxy as select_proxy
from ._helper import create_connection as create_connection, create_socks_proxy_socket as create_socks_proxy_socket, make_socks_proxy_opts as make_socks_proxy_opts
from .common import Features as Features, Response as Response, register_rh as register_rh
from .exceptions import CertificateVerifyError as CertificateVerifyError, HTTPError as HTTPError, ProxyError as ProxyError, RequestError as RequestError, SSLError as SSLError, TransportError as TransportError
from .websocket import WebSocketRequestHandler as WebSocketRequestHandler, WebSocketResponse as WebSocketResponse
from _typeshed import Incomplete

websockets_version: Incomplete

class WebsocketsResponseAdapter(WebSocketResponse):
    def __init__(self, ws: websockets.sync.client.ClientConnection, url) -> None: ...
    def close(self) -> None: ...
    def send(self, message): ...
    def recv(self): ...

class WebsocketsRH(WebSocketRequestHandler):
    RH_NAME: str
    def __init__(self, *args, **kwargs) -> None: ...
    def close(self) -> None: ...
