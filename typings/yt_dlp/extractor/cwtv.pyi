from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_age_limit as parse_age_limit, parse_iso8601 as parse_iso8601, parse_qs as parse_qs, smuggle_url as smuggle_url, str_or_none as str_or_none, update_url_query as update_url_query
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class CWTVIE(InfoExtractor):
    IE_NAME: str

class CWTVMovieIE(InfoExtractor):
    IE_NAME: str
