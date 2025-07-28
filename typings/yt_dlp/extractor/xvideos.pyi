from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, determine_ext as determine_ext, int_or_none as int_or_none, parse_duration as parse_duration
from .common import InfoExtractor as InfoExtractor

class XVideosIE(InfoExtractor): ...

class XVideosQuickiesIE(InfoExtractor):
    IE_NAME: str
