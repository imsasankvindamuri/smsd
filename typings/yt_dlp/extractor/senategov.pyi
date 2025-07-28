from ..utils import ExtractorError as ExtractorError, UnsupportedError as UnsupportedError, make_archive_id as make_archive_id, remove_end as remove_end, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class SenateISVPIE(InfoExtractor):
    IE_NAME: str

class SenateGovIE(InfoExtractor):
    IE_NAME: str
