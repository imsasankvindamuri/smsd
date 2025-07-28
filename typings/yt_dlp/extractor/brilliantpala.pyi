from ..utils import ExtractorError as ExtractorError, traverse_obj as traverse_obj, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class BrilliantpalaBaseIE(InfoExtractor): ...

class BrilliantpalaElearnIE(BrilliantpalaBaseIE):
    IE_NAME: str
    IE_DESC: str

class BrilliantpalaClassesIE(BrilliantpalaBaseIE):
    IE_NAME: str
    IE_DESC: str
