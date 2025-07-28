from ..utils import ExtractorError as ExtractorError, traverse_obj as traverse_obj
from .brightcove import BrightcoveNewIE as BrightcoveNewIE
from .common import InfoExtractor as InfoExtractor

class OneNewsNZIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    BRIGHTCOVE_URL_TEMPLATE: str
