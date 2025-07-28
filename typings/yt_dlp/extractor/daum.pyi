from ..utils import parse_qs as parse_qs
from .common import InfoExtractor as InfoExtractor

class DaumBaseIE(InfoExtractor): ...

class DaumIE(DaumBaseIE):
    IE_NAME: str

class DaumClipIE(DaumBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class DaumListIE(InfoExtractor): ...

class DaumPlaylistIE(DaumListIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class DaumUserIE(DaumListIE):
    IE_NAME: str
