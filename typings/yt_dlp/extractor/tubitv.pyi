from ..networking import Request as Request
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, js_to_json as js_to_json, strip_or_none as strip_or_none, traverse_obj as traverse_obj, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class TubiTvIE(InfoExtractor):
    IE_NAME: str

class TubiTvShowIE(InfoExtractor):
    IE_NAME: str
