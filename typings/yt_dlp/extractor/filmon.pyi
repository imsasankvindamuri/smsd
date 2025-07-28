from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, qualities as qualities, strip_or_none as strip_or_none
from .common import InfoExtractor as InfoExtractor

class FilmOnIE(InfoExtractor):
    IE_NAME: str

class FilmOnChannelIE(InfoExtractor):
    IE_NAME: str
