from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, int_or_none as int_or_none, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class StarTVIE(InfoExtractor):
    IE_NAME: str
