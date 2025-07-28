from ..utils import ExtractorError as ExtractorError, JSON_LD_RE as JSON_LD_RE, base_url as base_url, clean_html as clean_html, determine_ext as determine_ext, extract_attributes as extract_attributes, get_element_by_class as get_element_by_class, merge_dicts as merge_dicts, parse_duration as parse_duration, smuggle_url as smuggle_url, try_get as try_get, url_basename as url_basename, url_or_none as url_or_none, urljoin as urljoin
from .brightcove import BrightcoveNewIE as BrightcoveNewIE
from .common import InfoExtractor as InfoExtractor

class ITVIE(InfoExtractor): ...

class ITVBTCCIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str
