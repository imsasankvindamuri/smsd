from ..compat import compat_etree_fromstring as compat_etree_fromstring
from ..cookies import LenientSimpleCookie as LenientSimpleCookie
from ..networking.exceptions import HTTPError as HTTPError
from ..networking.impersonate import ImpersonateTarget as ImpersonateTarget
from ..utils import ExtractorError as ExtractorError, KNOWN_EXTENSIONS as KNOWN_EXTENSIONS, MEDIA_EXTENSIONS as MEDIA_EXTENSIONS, UnsupportedError as UnsupportedError, determine_ext as determine_ext, determine_protocol as determine_protocol, dict_get as dict_get, extract_basic_auth as extract_basic_auth, filter_dict as filter_dict, format_field as format_field, int_or_none as int_or_none, is_html as is_html, js_to_json as js_to_json, merge_dicts as merge_dicts, mimetype2ext as mimetype2ext, orderedSet as orderedSet, parse_duration as parse_duration, parse_resolution as parse_resolution, smuggle_url as smuggle_url, str_or_none as str_or_none, traverse_obj as traverse_obj, try_call as try_call, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp, unsmuggle_url as unsmuggle_url, update_url as update_url, update_url_query as update_url_query, url_or_none as url_or_none, urlhandle_detect_ext as urlhandle_detect_ext, urljoin as urljoin, variadic as variadic, xpath_attr as xpath_attr, xpath_text as xpath_text, xpath_with_ns as xpath_with_ns
from .common import InfoExtractor as InfoExtractor
from .commonprotocols import RtmpIE as RtmpIE
from .youtube import YoutubeIE as YoutubeIE

class GenericIE(InfoExtractor):
    IE_DESC: str
    IE_NAME: str
    def report_following_redirect(self, new_url) -> None: ...
    def report_detected(self, name, num: int = 1, note=None) -> None: ...
