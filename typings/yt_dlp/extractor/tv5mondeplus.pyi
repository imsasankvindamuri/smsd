from ..utils import clean_html as clean_html, determine_ext as determine_ext, extract_attributes as extract_attributes, get_element_by_class as get_element_by_class, get_element_html_by_class as get_element_html_by_class, int_or_none as int_or_none, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class TV5MondePlusIE(InfoExtractor):
    IE_NAME: str
