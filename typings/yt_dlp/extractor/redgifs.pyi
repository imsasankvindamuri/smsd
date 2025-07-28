from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, int_or_none as int_or_none, qualities as qualities, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class RedGifsBaseIE(InfoExtractor): ...
class RedGifsIE(RedGifsBaseIE): ...

class RedGifsSearchIE(RedGifsBaseIE):
    IE_DESC: str

class RedGifsUserIE(RedGifsBaseIE):
    IE_DESC: str
