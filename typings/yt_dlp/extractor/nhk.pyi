from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, filter_dict as filter_dict, get_element_by_class as get_element_by_class, int_or_none as int_or_none, join_nonempty as join_nonempty, parse_duration as parse_duration, remove_end as remove_end, traverse_obj as traverse_obj, try_call as try_call, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class NhkBaseIE(InfoExtractor): ...
class NhkVodIE(NhkBaseIE): ...

class NhkVodProgramIE(NhkBaseIE):
    @classmethod
    def suitable(cls, url): ...

class NhkForSchoolBangumiIE(InfoExtractor): ...

class NhkForSchoolSubjectIE(InfoExtractor):
    IE_DESC: str
    KNOWN_SUBJECTS: Incomplete

class NhkForSchoolProgramListIE(InfoExtractor): ...

class NhkRadiruIE(InfoExtractor):
    IE_DESC: str

class NhkRadioNewsPageIE(InfoExtractor): ...
class NhkRadiruLiveIE(InfoExtractor): ...
