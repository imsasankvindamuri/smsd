from ..utils import ExtractorError as ExtractorError, str_or_none as str_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class AudiusBaseIE(InfoExtractor): ...

class AudiusIE(AudiusBaseIE):
    IE_DESC: str

class AudiusTrackIE(AudiusIE):
    IE_NAME: str
    IE_DESC: str

class AudiusPlaylistIE(AudiusBaseIE):
    IE_NAME: str
    IE_DESC: str

class AudiusProfileIE(AudiusPlaylistIE):
    IE_NAME: str
    IE_DESC: str
