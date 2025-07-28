from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, smuggle_url as smuggle_url, traverse_obj as traverse_obj, unsmuggle_url as unsmuggle_url, update_url_query as update_url_query
from .common import InfoExtractor as InfoExtractor

class UplynkBaseIE(InfoExtractor): ...

class UplynkIE(UplynkBaseIE):
    IE_NAME: str

class UplynkPreplayIE(UplynkBaseIE):
    IE_NAME: str
