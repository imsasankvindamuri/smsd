from ..networking import HEADRequest as HEADRequest
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, UnsupportedError as UnsupportedError, determine_ext as determine_ext, int_or_none as int_or_none, mimetype2ext as mimetype2ext, parse_qs as parse_qs, traverse_obj as traverse_obj, try_get as try_get, url_or_none as url_or_none, urlhandle_detect_ext as urlhandle_detect_ext, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class LBRYBaseIE(InfoExtractor): ...

class LBRYIE(LBRYBaseIE):
    IE_NAME: str
    IE_DESC: str

class LBRYChannelIE(LBRYBaseIE):
    IE_NAME: str
    IE_DESC: str

class LBRYPlaylistIE(LBRYBaseIE):
    IE_NAME: str
    IE_DESC: str
