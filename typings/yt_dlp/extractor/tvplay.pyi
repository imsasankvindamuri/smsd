from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, qualities as qualities, traverse_obj as traverse_obj, try_get as try_get, update_url_query as update_url_query, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class TVPlayIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class TVPlayHomeIE(InfoExtractor): ...
