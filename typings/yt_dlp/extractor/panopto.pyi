from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, bug_reports_message as bug_reports_message, get_first as get_first, int_or_none as int_or_none, parse_qs as parse_qs, srt_subtitles_timecode as srt_subtitles_timecode, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class PanoptoBaseIE(InfoExtractor):
    BASE_URL_RE: str

class PanoptoIE(PanoptoBaseIE):
    @classmethod
    def suitable(cls, url): ...

class PanoptoPlaylistIE(PanoptoBaseIE): ...
class PanoptoListIE(PanoptoBaseIE): ...
