from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, str_or_none as str_or_none, traverse_obj as traverse_obj, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class PelotonIE(InfoExtractor):
    IE_NAME: str

class PelotonLiveIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
