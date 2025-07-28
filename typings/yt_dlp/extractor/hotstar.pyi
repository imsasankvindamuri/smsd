from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, determine_ext as determine_ext, int_or_none as int_or_none, join_nonempty as join_nonempty, str_or_none as str_or_none, url_or_none as url_or_none
from ..utils.traversal import require as require, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class HotStarBaseIE(InfoExtractor): ...

class HotStarIE(HotStarBaseIE):
    IE_NAME: str
    IE_DESC: str

class HotStarPrefixIE(InfoExtractor):
    IE_DESC: bool

class HotStarSeriesIE(HotStarBaseIE):
    IE_NAME: str
