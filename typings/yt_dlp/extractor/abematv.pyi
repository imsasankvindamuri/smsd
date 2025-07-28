from ..aes import aes_ecb_decrypt as aes_ecb_decrypt
from ..networking import RequestHandler as RequestHandler, Response as Response
from ..networking.exceptions import TransportError as TransportError
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, decode_base_n as decode_base_n, int_or_none as int_or_none, time_seconds as time_seconds, traverse_obj as traverse_obj, update_url as update_url, update_url_query as update_url_query
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class AbemaLicenseRH(RequestHandler):
    RH_NAME: str
    ie: Incomplete
    def __init__(self, *, ie: AbemaTVIE, **kwargs) -> None: ...

class AbemaTVBaseIE(InfoExtractor): ...
class AbemaTVIE(AbemaTVBaseIE): ...
class AbemaTVTitleIE(AbemaTVBaseIE): ...
