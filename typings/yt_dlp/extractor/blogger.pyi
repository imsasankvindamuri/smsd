from ..utils import mimetype2ext as mimetype2ext, parse_duration as parse_duration, parse_qs as parse_qs, str_or_none as str_or_none, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class BloggerIE(InfoExtractor):
    IE_NAME: str
