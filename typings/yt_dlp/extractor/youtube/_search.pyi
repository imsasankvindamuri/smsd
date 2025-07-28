from ...utils import join_nonempty as join_nonempty, parse_qs as parse_qs
from ..common import SearchInfoExtractor as SearchInfoExtractor
from ._tab import YoutubeTabBaseInfoExtractor as YoutubeTabBaseInfoExtractor
from _typeshed import Incomplete

class YoutubeSearchIE(YoutubeTabBaseInfoExtractor, SearchInfoExtractor):
    IE_DESC: str
    IE_NAME: str

class YoutubeSearchDateIE(YoutubeTabBaseInfoExtractor, SearchInfoExtractor):
    IE_NAME: Incomplete
    IE_DESC: str

class YoutubeSearchURLIE(YoutubeTabBaseInfoExtractor):
    IE_DESC: str
    IE_NAME: Incomplete

class YoutubeMusicSearchURLIE(YoutubeTabBaseInfoExtractor):
    IE_DESC: str
    IE_NAME: str
