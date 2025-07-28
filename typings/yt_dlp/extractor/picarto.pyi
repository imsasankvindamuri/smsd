from ..utils import ExtractorError as ExtractorError, str_or_none as str_or_none, traverse_obj as traverse_obj, update_url as update_url
from .common import InfoExtractor as InfoExtractor

class PicartoIE(InfoExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PicartoVodIE(InfoExtractor):
    IE_NAME: str
