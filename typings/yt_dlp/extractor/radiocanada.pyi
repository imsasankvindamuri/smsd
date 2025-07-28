from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, int_or_none as int_or_none, unified_strdate as unified_strdate
from .common import InfoExtractor as InfoExtractor

class RadioCanadaIE(InfoExtractor):
    IE_NAME: str

class RadioCanadaAudioVideoIE(InfoExtractor):
    IE_NAME: str
