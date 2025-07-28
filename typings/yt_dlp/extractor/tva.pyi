from ..utils import float_or_none as float_or_none, int_or_none as int_or_none, smuggle_url as smuggle_url, strip_or_none as strip_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .brightcove import BrightcoveNewIE as BrightcoveNewIE
from .common import InfoExtractor as InfoExtractor

class TVAIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
