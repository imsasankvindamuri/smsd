from ..networking import Request as Request
from ..utils import ExtractorError as ExtractorError, js_to_json as js_to_json, traverse_obj as traverse_obj, update_url_query as update_url_query, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class FC2IE(InfoExtractor):
    IE_NAME: str

class FC2EmbedIE(InfoExtractor):
    IE_NAME: str

class FC2LiveIE(InfoExtractor):
    IE_NAME: str
