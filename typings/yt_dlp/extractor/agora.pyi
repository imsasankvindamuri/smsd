from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, int_or_none as int_or_none, month_by_name as month_by_name, parse_duration as parse_duration, try_call as try_call
from .common import InfoExtractor as InfoExtractor

class WyborczaVideoIE(InfoExtractor):
    IE_NAME: str

class WyborczaPodcastIE(InfoExtractor): ...

class TokFMPodcastIE(InfoExtractor):
    IE_NAME: str

class TokFMAuditionIE(InfoExtractor):
    IE_NAME: str
