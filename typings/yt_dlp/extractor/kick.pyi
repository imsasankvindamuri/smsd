from ..utils import UserNotLive as UserNotLive, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, str_or_none as str_or_none, traverse_obj as traverse_obj, unified_timestamp as unified_timestamp, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class KickBaseIE(InfoExtractor): ...

class KickIE(KickBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class KickVODIE(KickBaseIE):
    IE_NAME: str

class KickClipIE(KickBaseIE):
    IE_NAME: str
