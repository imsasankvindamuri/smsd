from ..compat import compat_etree_fromstring as compat_etree_fromstring
from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, UnsupportedError as UnsupportedError, clean_html as clean_html, dict_get as dict_get, extract_attributes as extract_attributes, find_xpath_attr as find_xpath_attr, fix_xml_ampersands as fix_xml_ampersands, float_or_none as float_or_none, int_or_none as int_or_none, join_nonempty as join_nonempty, js_to_json as js_to_json, mimetype2ext as mimetype2ext, parse_iso8601 as parse_iso8601, parse_qs as parse_qs, smuggle_url as smuggle_url, str_or_none as str_or_none, try_get as try_get, unescapeHTML as unescapeHTML, unsmuggle_url as unsmuggle_url, update_url_query as update_url_query, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .adobepass import AdobePassIE as AdobePassIE
from .common import InfoExtractor as InfoExtractor

class BrightcoveLegacyIE(InfoExtractor):
    IE_NAME: str

class BrightcoveNewBaseIE(AdobePassIE): ...

class BrightcoveNewIE(BrightcoveNewBaseIE):
    IE_NAME: str
