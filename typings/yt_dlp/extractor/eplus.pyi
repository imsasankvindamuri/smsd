from ..utils import ExtractorError as ExtractorError, try_call as try_call, unified_timestamp as unified_timestamp, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class EplusIbIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
