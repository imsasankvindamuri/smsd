from ...utils import ExtractorError as ExtractorError
from ._base import YoutubeBaseInfoExtractor as YoutubeBaseInfoExtractor

class YoutubeTruncatedURLIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: bool

class YoutubeTruncatedIDIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: bool
