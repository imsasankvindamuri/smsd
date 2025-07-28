from ..utils import int_or_none as int_or_none, make_archive_id as make_archive_id, parse_iso8601 as parse_iso8601, str_or_none as str_or_none, traverse_obj as traverse_obj, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class KhanAcademyBaseIE(InfoExtractor): ...

class KhanAcademyIE(KhanAcademyBaseIE):
    IE_NAME: str

class KhanAcademyUnitIE(KhanAcademyBaseIE):
    IE_NAME: str
