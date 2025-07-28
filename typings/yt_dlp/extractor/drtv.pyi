from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, mimetype2ext as mimetype2ext, parse_iso8601 as parse_iso8601, try_call as try_call, update_url_query as update_url_query, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

SERIES_API: str

class DRTVIE(InfoExtractor):
    IE_NAME: str
    SUBTITLE_LANGS: Incomplete

class DRTVLiveIE(InfoExtractor):
    IE_NAME: str

class DRTVSeasonIE(InfoExtractor):
    IE_NAME: str

class DRTVSeriesIE(InfoExtractor):
    IE_NAME: str
