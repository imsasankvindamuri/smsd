from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, extract_attributes as extract_attributes, int_or_none as int_or_none, merge_dicts as merge_dicts, parse_iso8601 as parse_iso8601, strip_or_none as strip_or_none, traverse_obj as traverse_obj, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class IGNBaseIE(InfoExtractor): ...

class IGNIE(IGNBaseIE):
    IE_NAME: str

class IGNVideoIE(IGNBaseIE): ...
class IGNArticleIE(IGNBaseIE): ...
