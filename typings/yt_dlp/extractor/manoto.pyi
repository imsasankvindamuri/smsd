from ..utils import clean_html as clean_html, int_or_none as int_or_none, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class ManotoTVIE(InfoExtractor):
    IE_DESC: str

class ManotoTVShowIE(InfoExtractor):
    IE_DESC: str

class ManotoTVLiveIE(InfoExtractor):
    IE_DESC: str
