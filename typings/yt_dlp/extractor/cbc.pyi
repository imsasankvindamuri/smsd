from ..networking import HEADRequest as HEADRequest
from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, js_to_json as js_to_json, jwt_decode_hs256 as jwt_decode_hs256, mimetype2ext as mimetype2ext, orderedSet as orderedSet, parse_age_limit as parse_age_limit, parse_iso8601 as parse_iso8601, replace_extension as replace_extension, smuggle_url as smuggle_url, strip_or_none as strip_or_none, try_get as try_get, unified_timestamp as unified_timestamp, update_url as update_url, url_basename as url_basename, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from ..utils.traversal import require as require, traverse_obj as traverse_obj, trim_str as trim_str
from .common import InfoExtractor as InfoExtractor

class CBCIE(InfoExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class CBCPlayerIE(InfoExtractor):
    IE_NAME: str

class CBCPlayerPlaylistIE(InfoExtractor):
    IE_NAME: str

class CBCGemBaseIE(InfoExtractor): ...

class CBCGemIE(CBCGemBaseIE):
    IE_NAME: str

class CBCGemPlaylistIE(CBCGemBaseIE):
    IE_NAME: str

class CBCGemLiveIE(InfoExtractor):
    IE_NAME: str
