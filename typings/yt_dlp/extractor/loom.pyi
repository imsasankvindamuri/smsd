from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, filter_dict as filter_dict, get_first as get_first, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, update_url as update_url, url_or_none as url_or_none, variadic as variadic
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class LoomIE(InfoExtractor):
    IE_NAME: str

class LoomFolderIE(InfoExtractor):
    IE_NAME: str
