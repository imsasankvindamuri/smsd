from ..networking import HEADRequest as HEADRequest
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, determine_ext as determine_ext, extract_attributes as extract_attributes, filter_dict as filter_dict, format_field as format_field, int_or_none as int_or_none, join_nonempty as join_nonempty, parse_iso8601 as parse_iso8601, smuggle_url as smuggle_url, unsmuggle_url as unsmuggle_url, url_or_none as url_or_none
from ..utils.traversal import find_element as find_element, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from .dailymotion import DailymotionIE as DailymotionIE

class FranceTVBaseInfoExtractor(InfoExtractor): ...

class FranceTVIE(InfoExtractor):
    IE_NAME: str

class FranceTVSiteIE(FranceTVBaseInfoExtractor):
    IE_NAME: str

class FranceTVInfoIE(FranceTVBaseInfoExtractor):
    IE_NAME: str
