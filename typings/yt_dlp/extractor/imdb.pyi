from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, mimetype2ext as mimetype2ext, qualities as qualities, traverse_obj as traverse_obj, try_get as try_get, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class ImdbIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class ImdbListIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
