from ..utils import smuggle_url as smuggle_url
from .brightcove import BrightcoveLegacyIE as BrightcoveLegacyIE
from .common import InfoExtractor as InfoExtractor

class RMCDecouverteIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str
