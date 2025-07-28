from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, traverse_obj as traverse_obj, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class PixivSketchBaseIE(InfoExtractor): ...

class PixivSketchIE(PixivSketchBaseIE):
    IE_NAME: str

class PixivSketchUserIE(PixivSketchBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
