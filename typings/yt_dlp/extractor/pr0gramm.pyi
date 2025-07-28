from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, make_archive_id as make_archive_id, mimetype2ext as mimetype2ext, str_or_none as str_or_none, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class Pr0grammIE(InfoExtractor):
    BASE_URL: str
