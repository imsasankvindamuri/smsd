from ..utils import OnDemandPagedList as OnDemandPagedList, bug_reports_message as bug_reports_message, determine_ext as determine_ext, int_or_none as int_or_none, join_nonempty as join_nonempty, jwt_decode_hs256 as jwt_decode_hs256, make_archive_id as make_archive_id, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, remove_start as remove_start, str_or_none as str_or_none, unified_strdate as unified_strdate, update_url_query as update_url_query, url_or_none as url_or_none, xpath_text as xpath_text
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class ARDMediathekBaseIE(InfoExtractor): ...
class ARDIE(InfoExtractor): ...

class ARDBetaMediathekIE(InfoExtractor):
    IE_NAME: str

class ARDMediathekCollectionIE(InfoExtractor): ...
