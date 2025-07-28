from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, qualities as qualities, remove_start as remove_start, smuggle_url as smuggle_url, unsmuggle_url as unsmuggle_url, update_url_query as update_url_query, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class SproutVideoIE(InfoExtractor): ...

class VidsIoIE(InfoExtractor):
    IE_NAME: str
