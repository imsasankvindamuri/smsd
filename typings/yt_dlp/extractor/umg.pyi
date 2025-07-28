from ..utils import clean_html as clean_html
from ..utils.traversal import find_element as find_element, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class UMGDeIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
