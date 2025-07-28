from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, jwt_decode_hs256 as jwt_decode_hs256, parse_codecs as parse_codecs, try_get as try_get, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class DigitalConcertHallIE(InfoExtractor):
    IE_DESC: str
