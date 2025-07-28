from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class CuriosityStreamBaseIE(InfoExtractor): ...

class CuriosityStreamIE(CuriosityStreamBaseIE):
    IE_NAME: str

class CuriosityStreamCollectionBaseIE(CuriosityStreamBaseIE): ...

class CuriosityStreamCollectionsIE(CuriosityStreamCollectionBaseIE):
    IE_NAME: str

class CuriosityStreamSeriesIE(CuriosityStreamCollectionBaseIE):
    IE_NAME: str
