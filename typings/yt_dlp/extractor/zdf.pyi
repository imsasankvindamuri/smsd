from ..utils import ExtractorError as ExtractorError, ISO639Utils as ISO639Utils, determine_ext as determine_ext, filter_dict as filter_dict, float_or_none as float_or_none, int_or_none as int_or_none, join_nonempty as join_nonempty, make_archive_id as make_archive_id, parse_codecs as parse_codecs, parse_iso8601 as parse_iso8601, parse_qs as parse_qs, smuggle_url as smuggle_url, unified_timestamp as unified_timestamp, unsmuggle_url as unsmuggle_url, url_or_none as url_or_none, urljoin as urljoin, variadic as variadic
from ..utils.traversal import require as require, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class ZDFBaseIE(InfoExtractor): ...

class ZDFIE(ZDFBaseIE):
    IE_NAME: str

class ZDFChannelIE(ZDFBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
