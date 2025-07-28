from ..networking import HEADRequest as HEADRequest
from ..utils import ExtractorError as ExtractorError, UnsupportedError as UnsupportedError, UserNotLive as UserNotLive, determine_ext as determine_ext, filter_dict as filter_dict, format_field as format_field, int_or_none as int_or_none, join_nonempty as join_nonempty, merge_dicts as merge_dicts, mimetype2ext as mimetype2ext, parse_qs as parse_qs, qualities as qualities, srt_subtitles_timecode as srt_subtitles_timecode, str_or_none as str_or_none, traverse_obj as traverse_obj, truncate_string as truncate_string, try_call as try_call, try_get as try_get, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class TikTokBaseIE(InfoExtractor):
    QUALITIES: Incomplete

class TikTokIE(TikTokBaseIE): ...

class TikTokUserIE(TikTokBaseIE):
    IE_NAME: str

class TikTokBaseListIE(TikTokBaseIE): ...

class TikTokSoundIE(TikTokBaseListIE):
    IE_NAME: str

class TikTokEffectIE(TikTokBaseListIE):
    IE_NAME: str

class TikTokTagIE(TikTokBaseListIE):
    IE_NAME: str

class TikTokCollectionIE(TikTokBaseIE):
    IE_NAME: str

class DouyinIE(TikTokBaseIE): ...

class TikTokVMIE(InfoExtractor):
    IE_NAME: str

class TikTokLiveIE(TikTokBaseIE):
    IE_NAME: str
