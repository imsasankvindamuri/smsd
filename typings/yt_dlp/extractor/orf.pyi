from ..utils import clean_html as clean_html, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, make_archive_id as make_archive_id, mimetype2ext as mimetype2ext, orderedSet as orderedSet, parse_age_limit as parse_age_limit, parse_iso8601 as parse_iso8601, remove_end as remove_end, str_or_none as str_or_none, strip_jsonp as strip_jsonp, try_call as try_call, unified_strdate as unified_strdate, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class ORFRadioIE(InfoExtractor):
    IE_NAME: str
    STATION_INFO: Incomplete

class ORFPodcastIE(InfoExtractor):
    IE_NAME: str

class ORFIPTVIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class ORFFM4StoryIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class ORFONIE(InfoExtractor):
    IE_NAME: str
