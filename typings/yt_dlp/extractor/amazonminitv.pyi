from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, traverse_obj as traverse_obj, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class AmazonMiniTVBaseIE(InfoExtractor): ...
class AmazonMiniTVIE(AmazonMiniTVBaseIE): ...

class AmazonMiniTVSeasonIE(AmazonMiniTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class AmazonMiniTVSeriesIE(AmazonMiniTVBaseIE):
    IE_NAME: str
    IE_DESC: str
