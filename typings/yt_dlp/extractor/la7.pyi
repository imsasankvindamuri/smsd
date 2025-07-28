from ..networking import HEADRequest as HEADRequest
from ..utils import float_or_none as float_or_none, int_or_none as int_or_none, parse_duration as parse_duration, unified_strdate as unified_strdate
from .common import InfoExtractor as InfoExtractor

class LA7IE(InfoExtractor):
    IE_NAME: str

class LA7PodcastEpisodeIE(InfoExtractor):
    IE_NAME: str

class LA7PodcastIE(LA7PodcastEpisodeIE):
    IE_NAME: str
