from ..compat import compat_HTMLParseError as compat_HTMLParseError
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, extract_attributes as extract_attributes, find_xpath_attr as find_xpath_attr, get_element_by_attribute as get_element_by_attribute, get_element_by_class as get_element_by_class, int_or_none as int_or_none, join_nonempty as join_nonempty, js_to_json as js_to_json, merge_dicts as merge_dicts, parse_iso8601 as parse_iso8601, parse_qs as parse_qs, smuggle_url as smuggle_url, str_to_int as str_to_int, unescapeHTML as unescapeHTML
from .common import InfoExtractor as InfoExtractor
from .senategov import SenateISVPIE as SenateISVPIE
from .ustream import UstreamIE as UstreamIE

class CSpanIE(InfoExtractor):
    IE_DESC: str
    BRIGHTCOVE_URL_TEMPLATE: str

class CSpanCongressIE(InfoExtractor): ...
