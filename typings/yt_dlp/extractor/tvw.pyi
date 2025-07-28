from ..utils import clean_html as clean_html, extract_attributes as extract_attributes, parse_qs as parse_qs, remove_end as remove_end, require as require, unified_timestamp as unified_timestamp, url_or_none as url_or_none
from ..utils.traversal import find_element as find_element, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class TvwIE(InfoExtractor):
    IE_NAME: str

class TvwTvChannelsIE(InfoExtractor):
    IE_NAME: str
