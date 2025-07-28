from ..compat import compat_ord as compat_ord
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, merge_dicts as merge_dicts, multipart_encode as multipart_encode, parse_duration as parse_duration, try_call as try_call, url_or_none as url_or_none, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class CDAIE(InfoExtractor): ...
class CDAFolderIE(InfoExtractor): ...
