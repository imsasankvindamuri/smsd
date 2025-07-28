from ..utils import UserNotLive as UserNotLive, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, url_or_none as url_or_none, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class PartiBaseIE(InfoExtractor): ...

class PartiVideoIE(PartiBaseIE):
    IE_NAME: str

class PartiLivestreamIE(PartiBaseIE):
    IE_NAME: str
