from ..compat import compat_etree_fromstring as compat_etree_fromstring
from ..networking import Request as Request
from ..networking.exceptions import network_exceptions as network_exceptions
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, determine_ext as determine_ext, float_or_none as float_or_none, format_field as format_field, get_element_by_id as get_element_by_id, get_first as get_first, int_or_none as int_or_none, join_nonempty as join_nonempty, js_to_json as js_to_json, merge_dicts as merge_dicts, parse_count as parse_count, parse_qs as parse_qs, qualities as qualities, str_or_none as str_or_none, traverse_obj as traverse_obj, try_get as try_get, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin, variadic as variadic
from .common import InfoExtractor as InfoExtractor

class FacebookIE(InfoExtractor):
    IE_NAME: str

class FacebookPluginsVideoIE(InfoExtractor): ...

class FacebookRedirectURLIE(InfoExtractor):
    IE_DESC: bool

class FacebookReelIE(InfoExtractor):
    IE_NAME: str

class FacebookAdsIE(InfoExtractor):
    IE_NAME: str
