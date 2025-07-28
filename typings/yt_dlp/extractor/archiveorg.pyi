from ..networking import HEADRequest as HEADRequest
from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, KNOWN_EXTENSIONS as KNOWN_EXTENSIONS, bug_reports_message as bug_reports_message, clean_html as clean_html, dict_get as dict_get, extract_attributes as extract_attributes, get_element_by_id as get_element_by_id, int_or_none as int_or_none, join_nonempty as join_nonempty, js_to_json as js_to_json, merge_dicts as merge_dicts, mimetype2ext as mimetype2ext, orderedSet as orderedSet, parse_duration as parse_duration, parse_qs as parse_qs, str_or_none as str_or_none, str_to_int as str_to_int, traverse_obj as traverse_obj, try_get as try_get, unified_strdate as unified_strdate, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urlhandle_detect_ext as urlhandle_detect_ext, variadic as variadic
from .common import InfoExtractor as InfoExtractor
from .youtube import YoutubeBaseInfoExtractor as YoutubeBaseInfoExtractor, YoutubeIE as YoutubeIE

class ArchiveOrgIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeWebArchiveIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
