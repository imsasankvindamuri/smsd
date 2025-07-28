from ..networking import Request as Request
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, UserNotLive as UserNotLive, determine_ext as determine_ext, filter_dict as filter_dict, int_or_none as int_or_none, orderedSet as orderedSet, parse_iso8601 as parse_iso8601, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class AfreecaTVBaseIE(InfoExtractor): ...

class AfreecaTVIE(AfreecaTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class AfreecaTVCatchStoryIE(AfreecaTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class AfreecaTVLiveIE(AfreecaTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class AfreecaTVUserIE(AfreecaTVBaseIE):
    IE_NAME: str
