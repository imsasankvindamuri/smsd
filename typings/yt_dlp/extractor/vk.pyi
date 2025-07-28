from ..utils import ExtractorError as ExtractorError, UserNotLive as UserNotLive, clean_html as clean_html, get_element_by_class as get_element_by_class, get_element_html_by_id as get_element_html_by_id, int_or_none as int_or_none, join_nonempty as join_nonempty, parse_qs as parse_qs, parse_resolution as parse_resolution, str_or_none as str_or_none, str_to_int as str_to_int, try_call as try_call, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from ..utils.traversal import require as require, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from .dailymotion import DailymotionIE as DailymotionIE
from .odnoklassniki import OdnoklassnikiIE as OdnoklassnikiIE
from .pladform import PladformIE as PladformIE
from .sibnet import SibnetEmbedIE as SibnetEmbedIE
from .vimeo import VimeoIE as VimeoIE
from .youtube import YoutubeIE as YoutubeIE
from _typeshed import Incomplete
from typing import NamedTuple

class VKBaseIE(InfoExtractor): ...

class VKIE(VKBaseIE):
    IE_NAME: str
    IE_DESC: str

class VKUserVideosIE(VKBaseIE):
    IE_NAME: str
    IE_DESC: str

    class _VIDEO(NamedTuple):
        owner_id: Incomplete
        id: Incomplete

class VKWallPostIE(VKBaseIE):
    IE_NAME: str

    class _AUDIO(NamedTuple):
        id: Incomplete
        owner_id: Incomplete
        url: Incomplete
        title: Incomplete
        performer: Incomplete
        duration: Incomplete
        album_id: Incomplete
        unk: Incomplete
        author_link: Incomplete
        lyrics: Incomplete
        flags: Incomplete
        context: Incomplete
        extra: Incomplete
        hashes: Incomplete
        cover_url: Incomplete
        ads: Incomplete

class VKPlayBaseIE(InfoExtractor): ...
class VKPlayIE(VKPlayBaseIE): ...
class VKPlayLiveIE(VKPlayBaseIE): ...
