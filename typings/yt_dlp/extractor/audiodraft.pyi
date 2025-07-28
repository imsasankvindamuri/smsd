from ..utils import int_or_none as int_or_none
from .common import InfoExtractor as InfoExtractor

class AudiodraftBaseIE(InfoExtractor): ...

class AudiodraftCustomIE(AudiodraftBaseIE):
    IE_NAME: str

class AudiodraftGenericIE(AudiodraftBaseIE):
    IE_NAME: str
