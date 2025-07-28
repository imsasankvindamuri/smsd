from ..utils import ExtractorError as ExtractorError, unescapeHTML as unescapeHTML, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor
from .vimeo import VimeoIE as VimeoIE
from .youtube import YoutubeIE as YoutubeIE

class UkColumnIE(InfoExtractor):
    IE_NAME: str
