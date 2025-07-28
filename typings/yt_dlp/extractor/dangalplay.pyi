from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, join_nonempty as join_nonempty, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class DangalPlayBaseIE(InfoExtractor): ...

class DangalPlayIE(DangalPlayBaseIE):
    IE_NAME: str

class DangalPlaySeasonIE(DangalPlayBaseIE):
    IE_NAME: str
