from ..utils import parse_duration as parse_duration, traverse_obj as traverse_obj, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class RTVSIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
