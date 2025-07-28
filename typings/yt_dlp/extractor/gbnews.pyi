from ..utils import ExtractorError as ExtractorError, extract_attributes as extract_attributes, get_elements_html_by_class as get_elements_html_by_class, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class GBNewsIE(InfoExtractor):
    IE_DESC: str
