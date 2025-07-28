from ...utils import ExtractorError as ExtractorError, classproperty as classproperty, parse_qs as parse_qs, update_url_query as update_url_query, url_or_none as url_or_none
from ._base import YoutubeBaseInfoExtractor as YoutubeBaseInfoExtractor
from ._tab import YoutubeTabIE as YoutubeTabIE

class YoutubeYtBeIE(YoutubeBaseInfoExtractor):
    IE_DESC: str

class YoutubeLivestreamEmbedIE(YoutubeBaseInfoExtractor):
    IE_DESC: str

class YoutubeYtUserIE(YoutubeBaseInfoExtractor):
    IE_DESC: str
    IE_NAME: str

class YoutubeFavouritesIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeFeedsInfoExtractor(YoutubeBaseInfoExtractor):
    @classproperty
    def IE_NAME(cls): ...

class YoutubeWatchLaterIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeRecommendedIE(YoutubeFeedsInfoExtractor):
    IE_DESC: str

class YoutubeSubscriptionsIE(YoutubeFeedsInfoExtractor):
    IE_DESC: str

class YoutubeHistoryIE(YoutubeFeedsInfoExtractor):
    IE_DESC: str

class YoutubeShortsAudioPivotIE(YoutubeBaseInfoExtractor):
    IE_DESC: str
    IE_NAME: str

class YoutubeConsentRedirectIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: bool
