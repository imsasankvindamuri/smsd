from ..utils import int_or_none as int_or_none, traverse_obj as traverse_obj, try_call as try_call, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class HRFernsehenIE(InfoExtractor):
    IE_NAME: str
    def extract_formats(self, loader_data): ...
