from ..utils import ExtractorError as ExtractorError, dict_get as dict_get, int_or_none as int_or_none, join_nonempty as join_nonempty, merge_dicts as merge_dicts, parse_iso8601 as parse_iso8601, traverse_obj as traverse_obj, try_get as try_get, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class NaverBaseIE(InfoExtractor):
    @staticmethod
    def process_subtitles(vod_data, process_url): ...

class NaverIE(NaverBaseIE): ...

class NaverLiveIE(NaverBaseIE):
    IE_NAME: str

class NaverNowIE(NaverBaseIE):
    IE_NAME: str
