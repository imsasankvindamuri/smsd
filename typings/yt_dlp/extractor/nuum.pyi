from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, UserNotLive as UserNotLive, filter_dict as filter_dict, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, str_or_none as str_or_none, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class NuumBaseIE(InfoExtractor): ...

class NuumMediaIE(NuumBaseIE):
    IE_NAME: str

class NuumLiveIE(NuumBaseIE):
    IE_NAME: str

class NuumTabIE(NuumBaseIE):
    IE_NAME: str
