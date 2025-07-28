from ..utils import OnDemandPagedList as OnDemandPagedList, float_or_none as float_or_none, traverse_obj as traverse_obj, unified_strdate as unified_strdate
from .common import InfoExtractor as InfoExtractor

class GronkhIE(InfoExtractor): ...

class GronkhFeedIE(InfoExtractor):
    IE_NAME: str

class GronkhVodsIE(InfoExtractor):
    IE_NAME: str
