from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, strip_or_none as strip_or_none, traverse_obj as traverse_obj, try_call as try_call, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class RedBeeBaseIE(InfoExtractor): ...

class ParliamentLiveUKIE(RedBeeBaseIE):
    IE_NAME: str
    IE_DESC: str

class RTBFIE(RedBeeBaseIE): ...
