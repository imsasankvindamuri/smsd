from ..utils import ExtractorError as ExtractorError, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class WPPilotBaseIE(InfoExtractor): ...

class WPPilotIE(WPPilotBaseIE):
    IE_NAME: str

class WPPilotChannelsIE(WPPilotBaseIE):
    IE_NAME: str
