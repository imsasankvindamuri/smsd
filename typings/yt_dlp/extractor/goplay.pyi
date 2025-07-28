from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, remove_end as remove_end, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class GoPlayIE(InfoExtractor): ...
class InvalidLoginException(ExtractorError): ...
class AuthenticationException(ExtractorError): ...

class AwsIdp:
    ie: Incomplete
    pool_id: Incomplete
    client_id: Incomplete
    region: Incomplete
    url: Incomplete
    n_hex: str
    g_hex: str
    info_bits: Incomplete
    big_n: Incomplete
    g: Incomplete
    k: Incomplete
    small_a_value: Incomplete
    large_a_value: Incomplete
    def __init__(self, ie, pool_id, client_id) -> None: ...
    def authenticate(self, username, password): ...
