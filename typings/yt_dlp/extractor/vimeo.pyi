from ..networking import HEADRequest as HEADRequest, Request as Request
from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, determine_ext as determine_ext, filter_dict as filter_dict, get_element_by_class as get_element_by_class, int_or_none as int_or_none, join_nonempty as join_nonempty, js_to_json as js_to_json, jwt_decode_hs256 as jwt_decode_hs256, merge_dicts as merge_dicts, parse_filesize as parse_filesize, parse_iso8601 as parse_iso8601, parse_qs as parse_qs, qualities as qualities, smuggle_url as smuggle_url, str_or_none as str_or_none, traverse_obj as traverse_obj, try_get as try_get, unified_timestamp as unified_timestamp, unsmuggle_url as unsmuggle_url, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urlhandle_detect_ext as urlhandle_detect_ext, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class VimeoBaseInfoExtractor(InfoExtractor): ...

class VimeoIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoOndemandIE(VimeoIE):
    IE_NAME: str

class VimeoChannelIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoUserIE(VimeoChannelIE):
    IE_NAME: str

class VimeoAlbumIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoGroupsIE(VimeoChannelIE):
    IE_NAME: str

class VimeoReviewIE(VimeoBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class VimeoWatchLaterIE(VimeoChannelIE):
    IE_NAME: str
    IE_DESC: str

class VimeoLikesIE(VimeoChannelIE):
    IE_NAME: str
    IE_DESC: str

class VHXEmbedIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoProIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoEventIE(VimeoBaseInfoExtractor):
    IE_NAME: str
