from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_resolution as parse_resolution, traverse_obj as traverse_obj, try_get as try_get, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class MGTVIE(InfoExtractor):
    IE_DESC: str
    IE_NAME: str
