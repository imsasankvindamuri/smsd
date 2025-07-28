from ..utils import age_restricted as age_restricted, bug_reports_message as bug_reports_message, classproperty as classproperty, variadic as variadic, write_string as write_string
from _typeshed import Incomplete

ALLOWED_CLASSMETHODS: Incomplete

class LazyLoadMetaClass(type):
    def __getattr__(cls, name): ...

class LazyLoadExtractor(metaclass=LazyLoadMetaClass):
    @classproperty
    def real_class(cls): ...
    def __new__(cls, *args, **kwargs): ...
    IE_DESC: Incomplete
    SEARCH_KEY: Incomplete
    age_limit: int
    @classmethod
    def ie_key(cls): ...
    @classmethod
    def suitable(cls, url): ...
    @classmethod
    def working(cls): ...
    @classmethod
    def get_temp_id(cls, url): ...
    @classmethod
    def description(cls, *, markdown: bool = True, search_examples=None): ...
    @classmethod
    def is_suitable(cls, age_limit): ...
    @classmethod
    def supports_login(cls): ...
    @classmethod
    def is_single_video(cls, url): ...

class LazyLoadSearchExtractor(LazyLoadExtractor): ...

class ABCIE(LazyLoadExtractor):
    IE_NAME: str

class ABCIViewIE(LazyLoadExtractor):
    IE_NAME: str

class ABCIViewShowSeriesIE(LazyLoadExtractor):
    IE_NAME: str

class ABCOTVSClipsIE(LazyLoadExtractor):
    IE_NAME: str

class ABCOTVSIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ACastBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ACastChannelIE(ACastBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class ACastIE(ACastBaseIE):
    IE_NAME: str

class ADNBaseIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ADNIE(ADNBaseIE):
    IE_NAME: str
    IE_DESC: str

class ADNSeasonIE(ADNBaseIE):
    IE_NAME: str
    IE_DESC: str

class AMCNetworksIE(LazyLoadExtractor):
    IE_NAME: str

class APAIE(LazyLoadExtractor):
    IE_NAME: str

class ARDBetaMediathekIE(LazyLoadExtractor):
    IE_NAME: str

class ARDIE(LazyLoadExtractor):
    IE_NAME: str

class ARDMediathekCollectionIE(LazyLoadExtractor):
    IE_NAME: str

class ATVAtIE(LazyLoadExtractor):
    IE_NAME: str

class AWAANIE(LazyLoadExtractor):
    IE_NAME: str

class AWAANBaseIE(LazyLoadExtractor):
    IE_NAME: str

class AWAANLiveIE(AWAANBaseIE):
    IE_NAME: str

class AWAANSeasonIE(LazyLoadExtractor):
    IE_NAME: str

class AWAANVideoIE(AWAANBaseIE):
    IE_NAME: str

class AZMedienIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class AbcNewsIE(LazyLoadExtractor):
    IE_NAME: str

class AMPIE(LazyLoadExtractor):
    IE_NAME: str

class AbcNewsVideoIE(AMPIE):
    IE_NAME: str

class AbemaTVBaseIE(LazyLoadExtractor):
    IE_NAME: str

class AbemaTVIE(AbemaTVBaseIE):
    IE_NAME: str

class AbemaTVTitleIE(AbemaTVBaseIE):
    IE_NAME: str

class AcFunVideoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class AcFunBangumiIE(AcFunVideoBaseIE):
    IE_NAME: str

class AcFunVideoIE(AcFunVideoBaseIE):
    IE_NAME: str

class AcademicEarthCourseIE(LazyLoadExtractor):
    IE_NAME: str

class AdobeConnectIE(LazyLoadExtractor):
    IE_NAME: str

class AdobeTVBaseIE(LazyLoadExtractor):
    IE_NAME: str

class AdobeTVPlaylistBaseIE(AdobeTVBaseIE):
    IE_NAME: str

class AdobeTVChannelIE(AdobeTVPlaylistBaseIE):
    IE_NAME: str

class AdobeTVEmbedIE(AdobeTVBaseIE):
    IE_NAME: str

class AdobeTVIE(AdobeTVBaseIE):
    IE_NAME: str

class AdobeTVShowIE(AdobeTVPlaylistBaseIE):
    IE_NAME: str

class AdobeTVVideoIE(AdobeTVBaseIE):
    IE_NAME: str

class AdobePassIE(LazyLoadExtractor):
    IE_NAME: str

class TurnerBaseIE(AdobePassIE):
    IE_NAME: str

class AdultSwimIE(TurnerBaseIE):
    IE_NAME: str

class AeonCoIE(LazyLoadExtractor):
    IE_NAME: str

class AfreecaTVBaseIE(LazyLoadExtractor):
    IE_NAME: str

class AfreecaTVCatchStoryIE(AfreecaTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class AfreecaTVIE(AfreecaTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class AfreecaTVLiveIE(AfreecaTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class AfreecaTVUserIE(AfreecaTVBaseIE):
    IE_NAME: str

class AirTVIE(LazyLoadExtractor):
    IE_NAME: str

class AitubeKZVideoIE(LazyLoadExtractor):
    IE_NAME: str

class AlJazeeraIE(LazyLoadExtractor):
    IE_NAME: str

class AliExpressLiveIE(LazyLoadExtractor):
    IE_NAME: str

class AllocineIE(LazyLoadExtractor):
    IE_NAME: str

class AllstarBaseIE(LazyLoadExtractor):
    IE_NAME: str

class AllstarIE(AllstarBaseIE):
    IE_NAME: str

class AllstarProfileIE(AllstarBaseIE):
    IE_NAME: str

class AlphaPornoIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class Alsace20TVBaseIE(LazyLoadExtractor):
    IE_NAME: str

class Alsace20TVEmbedIE(Alsace20TVBaseIE):
    IE_NAME: str

class Alsace20TVIE(Alsace20TVBaseIE):
    IE_NAME: str

class AltCensoredChannelIE(LazyLoadExtractor):
    IE_NAME: str

class AltCensoredIE(LazyLoadExtractor):
    IE_NAME: str

class AluraIE(LazyLoadExtractor):
    IE_NAME: str

class AluraCourseIE(AluraIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class DPlayBaseIE(LazyLoadExtractor):
    IE_NAME: str

class DiscoveryPlusBaseIE(DPlayBaseIE):
    IE_NAME: str

class AmHistoryChannelIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class AmadeusTVIE(LazyLoadExtractor):
    IE_NAME: str

class AmaraIE(LazyLoadExtractor):
    IE_NAME: str

class AmazonMiniTVBaseIE(LazyLoadExtractor):
    IE_NAME: str

class AmazonMiniTVIE(AmazonMiniTVBaseIE):
    IE_NAME: str

class AmazonMiniTVSeasonIE(AmazonMiniTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class AmazonMiniTVSeriesIE(AmazonMiniTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class AmazonReviewsIE(LazyLoadExtractor):
    IE_NAME: str

class AmazonStoreIE(LazyLoadExtractor):
    IE_NAME: str

class AmericasTestKitchenIE(LazyLoadExtractor):
    IE_NAME: str

class AmericasTestKitchenSeasonIE(LazyLoadExtractor):
    IE_NAME: str

class AnchorFMEpisodeIE(LazyLoadExtractor):
    IE_NAME: str

class AngelIE(LazyLoadExtractor):
    IE_NAME: str

class AnimalPlanetIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class AntennaBaseIE(LazyLoadExtractor):
    IE_NAME: str

class Ant1NewsGrArticleIE(AntennaBaseIE):
    IE_NAME: str
    IE_DESC: str

class Ant1NewsGrEmbedIE(AntennaBaseIE):
    IE_NAME: str
    IE_DESC: str

class AntennaGrWatchIE(AntennaBaseIE):
    IE_NAME: str
    IE_DESC: str

class AnvatoIE(LazyLoadExtractor):
    IE_NAME: str

class AparatIE(LazyLoadExtractor):
    IE_NAME: str

class AppleConnectIE(LazyLoadExtractor):
    IE_NAME: str

class ApplePodcastsIE(LazyLoadExtractor):
    IE_NAME: str

class AppleTrailersIE(LazyLoadExtractor):
    IE_NAME: str

class AppleTrailersSectionIE(LazyLoadExtractor):
    IE_NAME: str

class ArcPublishingIE(LazyLoadExtractor):
    IE_NAME: str

class ArchiveOrgIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ArkenaIE(LazyLoadExtractor):
    IE_NAME: str

class ArnesIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class Art19IE(LazyLoadExtractor):
    IE_NAME: str

class Art19ShowIE(LazyLoadExtractor):
    IE_NAME: str

class ArteTVBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ArteTVCategoryIE(ArteTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class ArteTVEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class ArteTVIE(ArteTVBaseIE):
    IE_NAME: str

class ArteTVPlaylistIE(ArteTVBaseIE):
    IE_NAME: str

class AsobiChannelBaseIE(LazyLoadExtractor):
    IE_NAME: str

class AsobiChannelIE(AsobiChannelBaseIE):
    IE_NAME: str
    IE_DESC: str

class AsobiChannelTagURLIE(AsobiChannelBaseIE):
    IE_NAME: str
    IE_DESC: str

class AsobiStageIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class AtScaleConfEventIE(LazyLoadExtractor):
    IE_NAME: str

class AtresPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class AudiMediaIE(LazyLoadExtractor):
    IE_NAME: str

class AudioBoomIE(LazyLoadExtractor):
    IE_NAME: str

class AudiodraftBaseIE(LazyLoadExtractor):
    IE_NAME: str

class AudiodraftCustomIE(AudiodraftBaseIE):
    IE_NAME: str

class AudiodraftGenericIE(AudiodraftBaseIE):
    IE_NAME: str

class AudiomackAlbumIE(LazyLoadExtractor):
    IE_NAME: str

class AudiomackIE(LazyLoadExtractor):
    IE_NAME: str

class AudiusBaseIE(LazyLoadExtractor):
    IE_NAME: str

class AudiusIE(AudiusBaseIE):
    IE_NAME: str
    IE_DESC: str

class AudiusPlaylistIE(AudiusBaseIE):
    IE_NAME: str
    IE_DESC: str

class AudiusProfileIE(AudiusPlaylistIE):
    IE_NAME: str
    IE_DESC: str

class AudiusTrackIE(AudiusIE):
    IE_NAME: str
    IE_DESC: str

class AxsIE(LazyLoadExtractor):
    IE_NAME: str

class BBCCoUkArticleIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class BBCCoUkIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class BBCCoUkIPlayerPlaylistBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BBCCoUkIPlayerEpisodesIE(BBCCoUkIPlayerPlaylistBaseIE):
    IE_NAME: str

class BBCCoUkIPlayerGroupIE(BBCCoUkIPlayerPlaylistBaseIE):
    IE_NAME: str

class BBCCoUkPlaylistBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BBCCoUkPlaylistIE(BBCCoUkPlaylistBaseIE):
    IE_NAME: str

class BBCIE(BBCCoUkIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class ZattooPlatformBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BBVTVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class BBVTVIE(BBVTVBaseIE):
    IE_NAME: str

class BBVTVLiveIE(BBVTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class BBVTVRecordingsIE(BBVTVBaseIE):
    IE_NAME: str

class BFIPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class BFMTVBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BFMTVArticleIE(BFMTVBaseIE):
    IE_NAME: str

class BFMTVIE(BFMTVBaseIE):
    IE_NAME: str

class BFMTVLiveIE(BFMTVBaseIE):
    IE_NAME: str

class BRIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class BTArticleIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class BTVestlendingenIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class BYUtvIE(LazyLoadExtractor):
    IE_NAME: str

class BaiduVideoIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class BanByeBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BanByeChannelIE(BanByeBaseIE):
    IE_NAME: str

class BanByeIE(BanByeBaseIE):
    IE_NAME: str

class BrightcoveNewBaseIE(AdobePassIE):
    IE_NAME: str

class BandaiChannelIE(BrightcoveNewBaseIE):
    IE_NAME: str

class BandcampIE(LazyLoadExtractor):
    IE_NAME: str

class BandcampAlbumIE(BandcampIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class BandcampUserIE(LazyLoadExtractor):
    IE_NAME: str

class BandcampWeeklyIE(BandcampIE):
    IE_NAME: str

class BandlabBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BandlabIE(BandlabBaseIE):
    IE_NAME: str

class BandlabPlaylistIE(BandlabBaseIE):
    IE_NAME: str

class BannedVideoIE(LazyLoadExtractor):
    IE_NAME: str

class BeaconTvIE(LazyLoadExtractor):
    IE_NAME: str

class BeatBumpPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class BeatBumpVideoIE(LazyLoadExtractor):
    IE_NAME: str

class BeatportIE(LazyLoadExtractor):
    IE_NAME: str

class BeegIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class BehindKinkIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class BellMediaIE(LazyLoadExtractor):
    IE_NAME: str

class MTVServicesInfoExtractor(LazyLoadExtractor):
    IE_NAME: str

class BellatorIE(MTVServicesInfoExtractor):
    IE_NAME: str

class BerufeTVIE(LazyLoadExtractor):
    IE_NAME: str

class BetIE(MTVServicesInfoExtractor):
    IE_NAME: str

class BibelTVBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BibelTVLiveIE(BibelTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class BibelTVSeriesIE(BibelTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class BibelTVVideoIE(BibelTVBaseIE):
    IE_NAME: str
    IE_DESC: str

class BigflixIE(LazyLoadExtractor):
    IE_NAME: str

class BigoIE(LazyLoadExtractor):
    IE_NAME: str

class BildIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class BilibiliBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BiliBiliBangumiIE(BilibiliBaseIE):
    IE_NAME: str

class BiliBiliBangumiMediaIE(BilibiliBaseIE):
    IE_NAME: str

class BiliBiliBangumiSeasonIE(BilibiliBaseIE):
    IE_NAME: str

class BiliBiliDynamicIE(LazyLoadExtractor):
    IE_NAME: str

class BiliBiliIE(BilibiliBaseIE):
    IE_NAME: str

class BiliBiliPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class BiliBiliSearchIE(LazyLoadSearchExtractor):
    IE_NAME: str
    IE_DESC: str
    SEARCH_KEY: str

class BiliIntlBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BiliIntlIE(BiliIntlBaseIE):
    IE_NAME: str

class BiliIntlSeriesIE(BiliIntlBaseIE):
    IE_NAME: str

class BiliLiveIE(LazyLoadExtractor):
    IE_NAME: str

class BilibiliAudioBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BilibiliAudioAlbumIE(BilibiliAudioBaseIE):
    IE_NAME: str

class BilibiliAudioIE(BilibiliAudioBaseIE):
    IE_NAME: str

class BilibiliCategoryIE(LazyLoadExtractor):
    IE_NAME: str

class BilibiliCheeseBaseIE(BilibiliBaseIE):
    IE_NAME: str

class BilibiliCheeseIE(BilibiliCheeseBaseIE):
    IE_NAME: str

class BilibiliCheeseSeasonIE(BilibiliCheeseBaseIE):
    IE_NAME: str

class BilibiliSpaceBaseIE(BilibiliBaseIE):
    IE_NAME: str

class BilibiliSpaceListBaseIE(BilibiliSpaceBaseIE):
    IE_NAME: str

class BilibiliCollectionListIE(BilibiliSpaceListBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class BilibiliFavoritesListIE(BilibiliSpaceListBaseIE):
    IE_NAME: str

class BilibiliPlaylistIE(BilibiliSpaceListBaseIE):
    IE_NAME: str

class BilibiliSeriesListIE(BilibiliSpaceListBaseIE):
    IE_NAME: str

class BilibiliSpaceAudioIE(BilibiliSpaceBaseIE):
    IE_NAME: str

class BilibiliSpaceVideoIE(BilibiliSpaceBaseIE):
    IE_NAME: str

class BilibiliWatchlaterIE(BilibiliSpaceListBaseIE):
    IE_NAME: str

class BioBioChileTVIE(LazyLoadExtractor):
    IE_NAME: str

class BitChuteChannelIE(LazyLoadExtractor):
    IE_NAME: str

class BitChuteIE(LazyLoadExtractor):
    IE_NAME: str

class BlackboardCollaborateIE(LazyLoadExtractor):
    IE_NAME: str

class BleacherReportCMSIE(AMPIE):
    IE_NAME: str

class BleacherReportIE(LazyLoadExtractor):
    IE_NAME: str

class BlerpIE(LazyLoadExtractor):
    IE_NAME: str

class BlobIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class BloggerIE(LazyLoadExtractor):
    IE_NAME: str

class BloombergIE(LazyLoadExtractor):
    IE_NAME: str

class BlueskyIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class BokeCCBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BokeCCIE(BokeCCBaseIE):
    IE_NAME: str
    IE_DESC: str

class BongaCamsIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class BoostyIE(LazyLoadExtractor):
    IE_NAME: str

class BostonGlobeIE(LazyLoadExtractor):
    IE_NAME: str

class BoxCastVideoIE(LazyLoadExtractor):
    IE_NAME: str

class BoxIE(LazyLoadExtractor):
    IE_NAME: str

class BpbIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class BrainPOPBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BrainPOPLegacyBaseIE(BrainPOPBaseIE):
    IE_NAME: str

class BrainPOPELLIE(BrainPOPLegacyBaseIE):
    IE_NAME: str

class BrainPOPEspIE(BrainPOPLegacyBaseIE):
    IE_NAME: str
    IE_DESC: str

class BrainPOPFrIE(BrainPOPLegacyBaseIE):
    IE_NAME: str
    IE_DESC: str

class BrainPOPIE(BrainPOPBaseIE):
    IE_NAME: str

class BrainPOPIlIE(BrainPOPLegacyBaseIE):
    IE_NAME: str
    IE_DESC: str

class BrainPOPJrIE(BrainPOPLegacyBaseIE):
    IE_NAME: str

class ThePlatformBaseIE(AdobePassIE):
    IE_NAME: str

class NBCUniversalBaseIE(ThePlatformBaseIE):
    IE_NAME: str

class BravoTVIE(NBCUniversalBaseIE):
    IE_NAME: str
    age_limit: int

class BreitBartIE(LazyLoadExtractor):
    IE_NAME: str

class BrightcoveLegacyIE(LazyLoadExtractor):
    IE_NAME: str

class BrightcoveNewIE(BrightcoveNewBaseIE):
    IE_NAME: str

class BrilliantpalaBaseIE(LazyLoadExtractor):
    IE_NAME: str

class BrilliantpalaClassesIE(BrilliantpalaBaseIE):
    IE_NAME: str
    IE_DESC: str

class BrilliantpalaElearnIE(BrilliantpalaBaseIE):
    IE_NAME: str
    IE_DESC: str

class BundesligaIE(LazyLoadExtractor):
    IE_NAME: str

class BundestagIE(LazyLoadExtractor):
    IE_NAME: str

class BunnyCdnIE(LazyLoadExtractor):
    IE_NAME: str

class BusinessInsiderIE(LazyLoadExtractor):
    IE_NAME: str

class BuzzFeedIE(LazyLoadExtractor):
    IE_NAME: str

class C56IE(LazyLoadExtractor):
    IE_NAME: str

class CAM4IE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class CBCGemBaseIE(LazyLoadExtractor):
    IE_NAME: str

class CBCGemIE(CBCGemBaseIE):
    IE_NAME: str
    age_limit: int

class CBCGemLiveIE(LazyLoadExtractor):
    IE_NAME: str

class CBCGemPlaylistIE(CBCGemBaseIE):
    IE_NAME: str

class CBCIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class CBCPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class CBCPlayerPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class CBSNewsBaseIE(LazyLoadExtractor):
    IE_NAME: str

class CBSLocalBaseIE(CBSNewsBaseIE):
    IE_NAME: str

class CBSLocalArticleIE(CBSLocalBaseIE):
    IE_NAME: str

class CBSLocalIE(CBSLocalBaseIE):
    IE_NAME: str

class CBSNewsLiveBaseIE(CBSNewsBaseIE):
    IE_NAME: str

class CBSLocalLiveIE(CBSNewsLiveBaseIE):
    IE_NAME: str

class CBSNewsEmbedIE(CBSNewsBaseIE):
    IE_NAME: str

class CBSNewsIE(CBSNewsBaseIE):
    IE_NAME: str
    IE_DESC: str

class CBSNewsLiveIE(CBSNewsLiveBaseIE):
    IE_NAME: str
    IE_DESC: str

class CBSNewsLiveVideoIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class CBSSportsEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class CBSSportsBaseIE(LazyLoadExtractor):
    IE_NAME: str

class CBSSportsIE(CBSSportsBaseIE):
    IE_NAME: str

class CCCIE(LazyLoadExtractor):
    IE_NAME: str

class CCCPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class CCMAIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class CCTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class CDAFolderIE(LazyLoadExtractor):
    IE_NAME: str

class CDAIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class CGTNIE(LazyLoadExtractor):
    IE_NAME: str

class CHZZKLiveIE(LazyLoadExtractor):
    IE_NAME: str

class CHZZKVideoIE(LazyLoadExtractor):
    IE_NAME: str

class CJSWIE(LazyLoadExtractor):
    IE_NAME: str

class CNBCVideoIE(LazyLoadExtractor):
    IE_NAME: str

class CNNIE(LazyLoadExtractor):
    IE_NAME: str

class CNNIndonesiaIE(LazyLoadExtractor):
    IE_NAME: str

class CONtvIE(LazyLoadExtractor):
    IE_NAME: str

class CPACIE(LazyLoadExtractor):
    IE_NAME: str

class CPACPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class CPTwentyFourIE(LazyLoadExtractor):
    IE_NAME: str

class CSpanCongressIE(LazyLoadExtractor):
    IE_NAME: str

class CSpanIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class CTVIE(LazyLoadExtractor):
    IE_NAME: str

class CTVNewsIE(LazyLoadExtractor):
    IE_NAME: str

class CWTVIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class CWTVMovieIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class CaffeineTVIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class CallinIE(LazyLoadExtractor):
    IE_NAME: str

class CaltransIE(LazyLoadExtractor):
    IE_NAME: str

class CamFMEpisodeIE(LazyLoadExtractor):
    IE_NAME: str

class CamFMShowIE(LazyLoadExtractor):
    IE_NAME: str

class CamModelsIE(LazyLoadExtractor):
    IE_NAME: str

class CamdemyFolderIE(LazyLoadExtractor):
    IE_NAME: str

class CamdemyIE(LazyLoadExtractor):
    IE_NAME: str

class CamsodaIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class CamtasiaEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class Canal1IE(LazyLoadExtractor):
    IE_NAME: str

class CanalAlphaIE(LazyLoadExtractor):
    IE_NAME: str

class Canalc2IE(LazyLoadExtractor):
    IE_NAME: str

class CanalplusIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class CanalsurmasIE(LazyLoadExtractor):
    IE_NAME: str

class CaracolTvPlayIE(LazyLoadExtractor):
    IE_NAME: str

class VidyardBaseIE(LazyLoadExtractor):
    IE_NAME: str

class CellebriteIE(VidyardBaseIE):
    IE_NAME: str

class CeskaTelevizeIE(LazyLoadExtractor):
    IE_NAME: str

class CharlieRoseIE(LazyLoadExtractor):
    IE_NAME: str

class ChaturbateIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class ChilloutzoneIE(LazyLoadExtractor):
    IE_NAME: str

class HBOBaseIE(LazyLoadExtractor):
    IE_NAME: str

class CinemaxIE(HBOBaseIE):
    IE_NAME: str

class CinetecaMilanoIE(LazyLoadExtractor):
    IE_NAME: str

class CineverseBaseIE(LazyLoadExtractor):
    IE_NAME: str

class CineverseDetailsIE(CineverseBaseIE):
    IE_NAME: str

class CineverseIE(CineverseBaseIE):
    IE_NAME: str
    age_limit: int

class CiscoLiveBaseIE(LazyLoadExtractor):
    IE_NAME: str

class CiscoLiveSearchIE(CiscoLiveBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class CiscoLiveSessionIE(CiscoLiveBaseIE):
    IE_NAME: str

class CiscoWebexIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class OnetBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ClipRsIE(OnetBaseIE):
    IE_NAME: str

class ClipYouEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class ClipchampIE(LazyLoadExtractor):
    IE_NAME: str

class ClippitIE(LazyLoadExtractor):
    IE_NAME: str

class CloserToTruthIE(LazyLoadExtractor):
    IE_NAME: str

class CloudflareStreamIE(LazyLoadExtractor):
    IE_NAME: str

class CloudyCDNIE(LazyLoadExtractor):
    IE_NAME: str

class ClubicIE(LazyLoadExtractor):
    IE_NAME: str

class ClypIE(LazyLoadExtractor):
    IE_NAME: str

class ComedyCentralIE(MTVServicesInfoExtractor):
    IE_NAME: str

class ComedyCentralTVIE(MTVServicesInfoExtractor):
    IE_NAME: str

class CommonMistakesIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class TeamcocoBaseIE(TurnerBaseIE):
    IE_NAME: str

class ConanClassicIE(TeamcocoBaseIE):
    IE_NAME: str

class CondeNastIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class CookingChannelIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class CoubIE(LazyLoadExtractor):
    IE_NAME: str

class CozyTVIE(LazyLoadExtractor):
    IE_NAME: str

class CrackedIE(LazyLoadExtractor):
    IE_NAME: str

class CrackleIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class CraftsyIE(LazyLoadExtractor):
    IE_NAME: str

class CrooksAndLiarsIE(LazyLoadExtractor):
    IE_NAME: str

class CrowdBunkerChannelIE(LazyLoadExtractor):
    IE_NAME: str

class CrowdBunkerIE(LazyLoadExtractor):
    IE_NAME: str

class CrtvgIE(LazyLoadExtractor):
    IE_NAME: str

class CtsNewsIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class CultureUnpluggedIE(LazyLoadExtractor):
    IE_NAME: str

class CuriosityStreamBaseIE(LazyLoadExtractor):
    IE_NAME: str

class CuriosityStreamCollectionBaseIE(CuriosityStreamBaseIE):
    IE_NAME: str

class CuriosityStreamCollectionsIE(CuriosityStreamCollectionBaseIE):
    IE_NAME: str

class CuriosityStreamIE(CuriosityStreamBaseIE):
    IE_NAME: str

class CuriosityStreamSeriesIE(CuriosityStreamCollectionBaseIE):
    IE_NAME: str

class CybraryBaseIE(LazyLoadExtractor):
    IE_NAME: str

class CybraryCourseIE(CybraryBaseIE):
    IE_NAME: str

class CybraryIE(CybraryBaseIE):
    IE_NAME: str

class DBTVIE(LazyLoadExtractor):
    IE_NAME: str

class DFBIE(LazyLoadExtractor):
    IE_NAME: str

class DHMIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class DLFBaseIE(LazyLoadExtractor):
    IE_NAME: str

class DLFCorpusIE(DLFBaseIE):
    IE_NAME: str
    IE_DESC: str

class DLFIE(DLFBaseIE):
    IE_NAME: str

class DLiveStreamIE(LazyLoadExtractor):
    IE_NAME: str

class DLiveVODIE(LazyLoadExtractor):
    IE_NAME: str

class DPlayIE(DPlayBaseIE):
    IE_NAME: str

class DRBonanzaIE(LazyLoadExtractor):
    IE_NAME: str

class DRTVIE(LazyLoadExtractor):
    IE_NAME: str

class DRTVLiveIE(LazyLoadExtractor):
    IE_NAME: str

class DRTVSeasonIE(LazyLoadExtractor):
    IE_NAME: str

class DRTVSeriesIE(LazyLoadExtractor):
    IE_NAME: str

class DTubeIE(LazyLoadExtractor):
    IE_NAME: str

class DVTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class DWArticleIE(LazyLoadExtractor):
    IE_NAME: str

class DWIE(LazyLoadExtractor):
    IE_NAME: str

class DacastBaseIE(LazyLoadExtractor):
    IE_NAME: str

class DacastPlaylistIE(DacastBaseIE):
    IE_NAME: str

class DacastVODIE(DacastBaseIE):
    IE_NAME: str

class VRTBaseIE(LazyLoadExtractor):
    IE_NAME: str

class DagelijkseKostIE(VRTBaseIE):
    IE_NAME: str
    IE_DESC: str

class DailyMailIE(LazyLoadExtractor):
    IE_NAME: str

class DailyWireBaseIE(LazyLoadExtractor):
    IE_NAME: str

class DailyWireIE(DailyWireBaseIE):
    IE_NAME: str

class DailyWirePodcastIE(DailyWireBaseIE):
    IE_NAME: str

class DailymotionBaseInfoExtractor(LazyLoadExtractor):
    IE_NAME: str

class DailymotionIE(DailymotionBaseInfoExtractor):
    IE_NAME: str
    age_limit: int

class DailymotionPlaylistBaseIE(DailymotionBaseInfoExtractor):
    IE_NAME: str

class DailymotionPlaylistIE(DailymotionPlaylistBaseIE):
    IE_NAME: str

class DailymotionSearchIE(DailymotionPlaylistBaseIE):
    IE_NAME: str

class DailymotionUserIE(DailymotionPlaylistBaseIE):
    IE_NAME: str

class DamtomoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class DamtomoRecordIE(DamtomoBaseIE):
    IE_NAME: str

class DamtomoVideoIE(DamtomoBaseIE):
    IE_NAME: str

class DangalPlayBaseIE(LazyLoadExtractor):
    IE_NAME: str

class DangalPlayIE(DangalPlayBaseIE):
    IE_NAME: str

class DangalPlaySeasonIE(DangalPlayBaseIE):
    IE_NAME: str

class DaumBaseIE(LazyLoadExtractor):
    IE_NAME: str

class DaumClipIE(DaumBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class DaumIE(DaumBaseIE):
    IE_NAME: str

class DaumListIE(LazyLoadExtractor):
    IE_NAME: str

class DaumPlaylistIE(DaumListIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class DaumUserIE(DaumListIE):
    IE_NAME: str

class DaystarClipIE(LazyLoadExtractor):
    IE_NAME: str

class DctpTvIE(LazyLoadExtractor):
    IE_NAME: str

class DemocracynowIE(LazyLoadExtractor):
    IE_NAME: str

class DestinationAmericaIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class DetikEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class DeuxMIE(LazyLoadExtractor):
    IE_NAME: str

class DeuxMNewsIE(LazyLoadExtractor):
    IE_NAME: str

class DigitalConcertHallIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class DigitallySpeakingIE(LazyLoadExtractor):
    IE_NAME: str

class DigitekaIE(LazyLoadExtractor):
    IE_NAME: str

class DigiviewIE(LazyLoadExtractor):
    IE_NAME: str

class DiscogsReleasePlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class DiscoveryLifeIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class DiscoveryNetworksDeIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class DiscoveryPlusIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class DiscoveryPlusIndiaIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class DiscoveryPlusShowBaseIE(DPlayBaseIE):
    IE_NAME: str

class DiscoveryPlusIndiaShowIE(DiscoveryPlusShowBaseIE):
    IE_NAME: str

class DiscoveryPlusItalyIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class DiscoveryPlusItalyShowIE(DiscoveryPlusShowBaseIE):
    IE_NAME: str

class DisneyIE(LazyLoadExtractor):
    IE_NAME: str

class TikTokBaseIE(LazyLoadExtractor):
    IE_NAME: str

class DouyinIE(TikTokBaseIE):
    IE_NAME: str

class DouyuBaseIE(LazyLoadExtractor):
    IE_NAME: str

class DouyuShowIE(DouyuBaseIE):
    IE_NAME: str

class DouyuTVIE(DouyuBaseIE):
    IE_NAME: str
    IE_DESC: str

class DrTalksIE(LazyLoadExtractor):
    IE_NAME: str

class DrTuberIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class ZDFBaseIE(LazyLoadExtractor):
    IE_NAME: str

class DreiSatIE(ZDFBaseIE):
    IE_NAME: str

class DroobleIE(LazyLoadExtractor):
    IE_NAME: str

class DropboxIE(LazyLoadExtractor):
    IE_NAME: str

class DropoutIE(LazyLoadExtractor):
    IE_NAME: str

class DropoutSeasonIE(LazyLoadExtractor):
    IE_NAME: str

class DubokuIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class DubokuPlaylistIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class DumpertIE(LazyLoadExtractor):
    IE_NAME: str

class DuoplayIE(LazyLoadExtractor):
    IE_NAME: str

class TNAFlixNetworkBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TNAEMPFlixBaseIE(TNAFlixNetworkBaseIE):
    IE_NAME: str

class EMPFlixIE(TNAEMPFlixBaseIE):
    IE_NAME: str
    age_limit: int

class ERRJupiterIE(LazyLoadExtractor):
    IE_NAME: str

class ERTFlixBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ERTFlixCodenameIE(ERTFlixBaseIE):
    IE_NAME: str
    IE_DESC: str

class ERTFlixIE(ERTFlixBaseIE):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class ERTWebtvEmbedIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ESPNArticleIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class ESPNCricInfoIE(LazyLoadExtractor):
    IE_NAME: str

class ESPNIE(LazyLoadExtractor):
    IE_NAME: str

class EUScreenIE(LazyLoadExtractor):
    IE_NAME: str

class EWETVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class EWETVIE(EWETVBaseIE):
    IE_NAME: str

class EWETVLiveIE(EWETVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class EWETVRecordingsIE(EWETVBaseIE):
    IE_NAME: str

class EaglePlatformIE(LazyLoadExtractor):
    IE_NAME: str

class EbaumsWorldIE(LazyLoadExtractor):
    IE_NAME: str

class EbayIE(LazyLoadExtractor):
    IE_NAME: str

class EggheadBaseIE(LazyLoadExtractor):
    IE_NAME: str

class EggheadCourseIE(EggheadBaseIE):
    IE_NAME: str
    IE_DESC: str

class EggheadLessonIE(EggheadBaseIE):
    IE_NAME: str
    IE_DESC: str

class EggsBaseIE(LazyLoadExtractor):
    IE_NAME: str

class EggsArtistIE(EggsBaseIE):
    IE_NAME: str

class EggsIE(EggsBaseIE):
    IE_NAME: str

class EightTracksIE(LazyLoadExtractor):
    IE_NAME: str

class EinsUndEinsTVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class EinsUndEinsTVIE(EinsUndEinsTVBaseIE):
    IE_NAME: str

class EinsUndEinsTVLiveIE(EinsUndEinsTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class EinsUndEinsTVRecordingsIE(EinsUndEinsTVBaseIE):
    IE_NAME: str

class EitbIE(LazyLoadExtractor):
    IE_NAME: str

class ElPaisIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ElTreceTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ElementorEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class ElonetIE(LazyLoadExtractor):
    IE_NAME: str

class EmbedlyIE(LazyLoadExtractor):
    IE_NAME: str

class EpiconIE(LazyLoadExtractor):
    IE_NAME: str

class EpiconSeriesIE(LazyLoadExtractor):
    IE_NAME: str

class EpidemicSoundIE(LazyLoadExtractor):
    IE_NAME: str

class EplusIbIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class EpochIE(LazyLoadExtractor):
    IE_NAME: str

class EpornerIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class EroProfileAlbumIE(LazyLoadExtractor):
    IE_NAME: str

class EroProfileIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class ErocastIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class EttuTvIE(LazyLoadExtractor):
    IE_NAME: str

class EuroParlWebstreamIE(LazyLoadExtractor):
    IE_NAME: str

class EuropaIE(LazyLoadExtractor):
    IE_NAME: str

class EuropeanTourIE(LazyLoadExtractor):
    IE_NAME: str

class EurosportIE(LazyLoadExtractor):
    IE_NAME: str

class ExpressenIE(LazyLoadExtractor):
    IE_NAME: str

class EyedoTVIE(LazyLoadExtractor):
    IE_NAME: str

class FC2EmbedIE(LazyLoadExtractor):
    IE_NAME: str

class FC2IE(LazyLoadExtractor):
    IE_NAME: str

class FC2LiveIE(LazyLoadExtractor):
    IE_NAME: str

class FOX9IE(LazyLoadExtractor):
    IE_NAME: str

class FOX9NewsIE(LazyLoadExtractor):
    IE_NAME: str

class FOXIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class FacebookAdsIE(LazyLoadExtractor):
    IE_NAME: str

class FacebookIE(LazyLoadExtractor):
    IE_NAME: str

class FacebookPluginsVideoIE(LazyLoadExtractor):
    IE_NAME: str

class FacebookRedirectURLIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class FacebookReelIE(LazyLoadExtractor):
    IE_NAME: str

class FancodeVodIE(LazyLoadExtractor):
    IE_NAME: str

class FancodeLiveIE(FancodeVodIE):
    IE_NAME: str

class FathomIE(LazyLoadExtractor):
    IE_NAME: str

class FazIE(LazyLoadExtractor):
    IE_NAME: str

class FczenitIE(LazyLoadExtractor):
    IE_NAME: str

class FifaIE(LazyLoadExtractor):
    IE_NAME: str

class FilmOnChannelIE(LazyLoadExtractor):
    IE_NAME: str

class FilmOnIE(LazyLoadExtractor):
    IE_NAME: str

class FilmwebIE(LazyLoadExtractor):
    IE_NAME: str

class FirstTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class FiveTVIE(LazyLoadExtractor):
    IE_NAME: str

class FiveThirtyEightIE(LazyLoadExtractor):
    IE_NAME: str

class FlexTVIE(LazyLoadExtractor):
    IE_NAME: str

class FlickrIE(LazyLoadExtractor):
    IE_NAME: str

class FloatplaneChannelIE(LazyLoadExtractor):
    IE_NAME: str

class FloatplaneBaseIE(LazyLoadExtractor):
    IE_NAME: str

class FloatplaneIE(FloatplaneBaseIE):
    IE_NAME: str

class FolketingetIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class FoodNetworkIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class FootyRoomIE(LazyLoadExtractor):
    IE_NAME: str

class Formula1IE(LazyLoadExtractor):
    IE_NAME: str

class FourTubeBaseIE(LazyLoadExtractor):
    IE_NAME: str

class FourTubeIE(FourTubeBaseIE):
    IE_NAME: str
    age_limit: int

class FoxNewsArticleIE(LazyLoadExtractor):
    IE_NAME: str

class FoxNewsIE(AMPIE):
    IE_NAME: str
    IE_DESC: str

class FoxNewsVideoIE(LazyLoadExtractor):
    IE_NAME: str

class FoxSportsIE(LazyLoadExtractor):
    IE_NAME: str

class FptplayIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class FrancaisFacileIE(LazyLoadExtractor):
    IE_NAME: str

class RadioFranceBaseIE(LazyLoadExtractor):
    IE_NAME: str

class FranceCultureIE(RadioFranceBaseIE):
    IE_NAME: str

class FranceInterIE(LazyLoadExtractor):
    IE_NAME: str

class FranceTVIE(LazyLoadExtractor):
    IE_NAME: str

class FranceTVBaseInfoExtractor(LazyLoadExtractor):
    IE_NAME: str

class FranceTVInfoIE(FranceTVBaseInfoExtractor):
    IE_NAME: str

class FranceTVSiteIE(FranceTVBaseInfoExtractor):
    IE_NAME: str

class FreeTvBaseIE(LazyLoadExtractor):
    IE_NAME: str

class FreeTvIE(FreeTvBaseIE):
    IE_NAME: str

class FreeTvMoviesIE(FreeTvBaseIE):
    IE_NAME: str

class FreesoundIE(LazyLoadExtractor):
    IE_NAME: str

class FreespeechIE(LazyLoadExtractor):
    IE_NAME: str

class FrontendMastersBaseIE(LazyLoadExtractor):
    IE_NAME: str

class FrontendMastersPageBaseIE(FrontendMastersBaseIE):
    IE_NAME: str

class FrontendMastersCourseIE(FrontendMastersPageBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class FrontendMastersIE(FrontendMastersBaseIE):
    IE_NAME: str

class FrontendMastersLessonIE(FrontendMastersPageBaseIE):
    IE_NAME: str

class FujiTVFODPlus7IE(LazyLoadExtractor):
    IE_NAME: str

class FunkIE(LazyLoadExtractor):
    IE_NAME: str

class Funker530IE(LazyLoadExtractor):
    IE_NAME: str

class FuxIE(FourTubeBaseIE):
    IE_NAME: str
    age_limit: int

class FuyinTVIE(LazyLoadExtractor):
    IE_NAME: str

class GBNewsIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class GDCVaultIE(LazyLoadExtractor):
    IE_NAME: str

class GMANetworkVideoIE(LazyLoadExtractor):
    IE_NAME: str

class GPUTechConfIE(LazyLoadExtractor):
    IE_NAME: str

class GabIE(LazyLoadExtractor):
    IE_NAME: str

class GabTVIE(LazyLoadExtractor):
    IE_NAME: str

class GaiaIE(LazyLoadExtractor):
    IE_NAME: str

class GameDevTVDashboardIE(LazyLoadExtractor):
    IE_NAME: str

class GameJoltBaseIE(LazyLoadExtractor):
    IE_NAME: str

class GameJoltPostListBaseIE(GameJoltBaseIE):
    IE_NAME: str

class GameJoltCommunityIE(GameJoltPostListBaseIE):
    IE_NAME: str

class GameJoltGameIE(GameJoltPostListBaseIE):
    IE_NAME: str

class GameJoltGameSoundtrackIE(GameJoltBaseIE):
    IE_NAME: str

class GameJoltIE(GameJoltBaseIE):
    IE_NAME: str

class GameJoltSearchIE(GameJoltPostListBaseIE):
    IE_NAME: str

class GameJoltUserIE(GameJoltPostListBaseIE):
    IE_NAME: str

class GameSpotIE(LazyLoadExtractor):
    IE_NAME: str

class GameStarIE(LazyLoadExtractor):
    IE_NAME: str

class GaskrankIE(LazyLoadExtractor):
    IE_NAME: str

class GazetaIE(LazyLoadExtractor):
    IE_NAME: str

class GediDigitalIE(LazyLoadExtractor):
    IE_NAME: str

class GeniusIE(LazyLoadExtractor):
    IE_NAME: str

class GeniusLyricsIE(LazyLoadExtractor):
    IE_NAME: str

class GermanupaIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class GetCourseRuIE(LazyLoadExtractor):
    IE_NAME: str

class GetCourseRuPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class GettrBaseIE(LazyLoadExtractor):
    IE_NAME: str

class GettrIE(GettrBaseIE):
    IE_NAME: str

class GettrStreamingIE(GettrBaseIE):
    IE_NAME: str

class GiantBombIE(LazyLoadExtractor):
    IE_NAME: str

class GlattvisionTVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class GlattvisionTVIE(GlattvisionTVBaseIE):
    IE_NAME: str

class GlattvisionTVLiveIE(GlattvisionTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class GlattvisionTVRecordingsIE(GlattvisionTVBaseIE):
    IE_NAME: str

class GlideIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class GlobalPlayerBaseIE(LazyLoadExtractor):
    IE_NAME: str

class GlobalPlayerAudioEpisodeIE(GlobalPlayerBaseIE):
    IE_NAME: str

class GlobalPlayerAudioIE(GlobalPlayerBaseIE):
    IE_NAME: str

class GlobalPlayerLiveIE(GlobalPlayerBaseIE):
    IE_NAME: str

class GlobalPlayerLivePlaylistIE(GlobalPlayerBaseIE):
    IE_NAME: str

class GlobalPlayerVideoIE(GlobalPlayerBaseIE):
    IE_NAME: str

class GloboArticleIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class GloboIE(LazyLoadExtractor):
    IE_NAME: str

class GlomexBaseIE(LazyLoadExtractor):
    IE_NAME: str

class GlomexEmbedIE(GlomexBaseIE):
    IE_NAME: str
    IE_DESC: str

class GlomexIE(GlomexBaseIE):
    IE_NAME: str
    IE_DESC: str

class GoDiscoveryIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class GoIE(AdobePassIE):
    IE_NAME: str
    age_limit: int

class GoPlayIE(LazyLoadExtractor):
    IE_NAME: str

class GoProIE(LazyLoadExtractor):
    IE_NAME: str

class GoToStageIE(LazyLoadExtractor):
    IE_NAME: str

class GodResourceIE(LazyLoadExtractor):
    IE_NAME: str

class GodTubeIE(LazyLoadExtractor):
    IE_NAME: str

class GofileIE(LazyLoadExtractor):
    IE_NAME: str

class GolemIE(LazyLoadExtractor):
    IE_NAME: str

class GoodGameIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class GoogleDriveFolderIE(LazyLoadExtractor):
    IE_NAME: str

class GoogleDriveIE(LazyLoadExtractor):
    IE_NAME: str

class GooglePodcastsBaseIE(LazyLoadExtractor):
    IE_NAME: str

class GooglePodcastsFeedIE(GooglePodcastsBaseIE):
    IE_NAME: str

class GooglePodcastsIE(GooglePodcastsBaseIE):
    IE_NAME: str

class GoogleSearchIE(LazyLoadSearchExtractor):
    IE_NAME: str
    IE_DESC: str
    SEARCH_KEY: str

class GoshgayIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class GraspopIE(LazyLoadExtractor):
    IE_NAME: str

class GronkhFeedIE(LazyLoadExtractor):
    IE_NAME: str

class GronkhIE(LazyLoadExtractor):
    IE_NAME: str

class GronkhVodsIE(LazyLoadExtractor):
    IE_NAME: str

class GrouponIE(LazyLoadExtractor):
    IE_NAME: str

class HBOIE(HBOBaseIE):
    IE_NAME: str

class HGTVComShowIE(LazyLoadExtractor):
    IE_NAME: str

class HGTVDeIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class HGTVUsaIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class HKETVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class HRFernsehenIE(LazyLoadExtractor):
    IE_NAME: str

class HRTiBaseIE(LazyLoadExtractor):
    IE_NAME: str

class HRTiIE(HRTiBaseIE):
    IE_NAME: str
    age_limit: int

class HRTiPlaylistIE(HRTiBaseIE):
    IE_NAME: str

class HSEShowBaseIE(LazyLoadExtractor):
    IE_NAME: str

class HSEProductIE(HSEShowBaseIE):
    IE_NAME: str

class HSEShowIE(HSEShowBaseIE):
    IE_NAME: str

class HTML5MediaEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class HarpodeonIE(LazyLoadExtractor):
    IE_NAME: str

class HearThisAtIE(LazyLoadExtractor):
    IE_NAME: str

class HeiseIE(LazyLoadExtractor):
    IE_NAME: str

class HellPornoIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class NPODataMidEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class HetKlokhuisIE(NPODataMidEmbedIE):
    IE_NAME: str

class HiDiveIE(LazyLoadExtractor):
    IE_NAME: str

class HistoricFilmsIE(LazyLoadExtractor):
    IE_NAME: str

class HitRecordIE(LazyLoadExtractor):
    IE_NAME: str

class HollywoodReporterIE(LazyLoadExtractor):
    IE_NAME: str

class HollywoodReporterPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class HolodexIE(LazyLoadExtractor):
    IE_NAME: str

class HotNewHipHopIE(LazyLoadExtractor):
    IE_NAME: str

class HotStarBaseIE(LazyLoadExtractor):
    IE_NAME: str

class HotStarIE(HotStarBaseIE):
    IE_NAME: str
    IE_DESC: str

class HotStarPrefixIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class HotStarSeriesIE(HotStarBaseIE):
    IE_NAME: str

class HrefLiRedirectIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class HuajiaoIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class HuffPostIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class HungamaBaseIE(LazyLoadExtractor):
    IE_NAME: str

class HungamaAlbumPlaylistIE(HungamaBaseIE):
    IE_NAME: str

class HungamaIE(HungamaBaseIE):
    IE_NAME: str

class HungamaSongIE(LazyLoadExtractor):
    IE_NAME: str

class HuyaLiveIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class HuyaVideoIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class HypemIE(LazyLoadExtractor):
    IE_NAME: str

class HytaleIE(LazyLoadExtractor):
    IE_NAME: str

class IGNBaseIE(LazyLoadExtractor):
    IE_NAME: str

class IGNArticleIE(IGNBaseIE):
    IE_NAME: str

class IGNIE(IGNBaseIE):
    IE_NAME: str

class IGNVideoIE(IGNBaseIE):
    IE_NAME: str

class IHeartRadioBaseIE(LazyLoadExtractor):
    IE_NAME: str

class IHeartRadioIE(IHeartRadioBaseIE):
    IE_NAME: str

class IHeartRadioPodcastIE(IHeartRadioBaseIE):
    IE_NAME: str

class IPrimaCNNIE(LazyLoadExtractor):
    IE_NAME: str

class IPrimaIE(LazyLoadExtractor):
    IE_NAME: str

class ITProTVBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ITProTVCourseIE(ITProTVBaseIE):
    IE_NAME: str

class ITProTVIE(ITProTVBaseIE):
    IE_NAME: str

class ITVBTCCIE(LazyLoadExtractor):
    IE_NAME: str

class ITVIE(LazyLoadExtractor):
    IE_NAME: str

class IVXPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class IcareusIE(LazyLoadExtractor):
    IE_NAME: str

class IchinanaLiveClipIE(LazyLoadExtractor):
    IE_NAME: str

class IchinanaLiveIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class IchinanaLiveVODIE(LazyLoadExtractor):
    IE_NAME: str

class IdolPlusIE(LazyLoadExtractor):
    IE_NAME: str

class TencentBaseIE(LazyLoadExtractor):
    IE_NAME: str

class WeTvBaseIE(TencentBaseIE):
    IE_NAME: str

class IflixBaseIE(WeTvBaseIE):
    IE_NAME: str

class IflixEpisodeIE(IflixBaseIE):
    IE_NAME: str

class IflixSeriesIE(IflixBaseIE):
    IE_NAME: str

class IlPostIE(LazyLoadExtractor):
    IE_NAME: str

class IltalehtiIE(LazyLoadExtractor):
    IE_NAME: str

class ImdbIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ImdbListIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ImgurBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ImgurGalleryBaseIE(ImgurBaseIE):
    IE_NAME: str

class ImgurAlbumIE(ImgurGalleryBaseIE):
    IE_NAME: str

class ImgurGalleryIE(ImgurGalleryBaseIE):
    IE_NAME: str

class ImgurIE(ImgurBaseIE):
    IE_NAME: str

class InaIE(LazyLoadExtractor):
    IE_NAME: str

class IncIE(LazyLoadExtractor):
    IE_NAME: str

class IndavideoEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class InfoQIE(BokeCCBaseIE):
    IE_NAME: str

class InstagramBaseIE(LazyLoadExtractor):
    IE_NAME: str

class InstagramIE(InstagramBaseIE):
    IE_NAME: str

class InstagramIOSIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class InstagramStoryIE(InstagramBaseIE):
    IE_NAME: str

class InstagramPlaylistBaseIE(InstagramBaseIE):
    IE_NAME: str

class InstagramTagIE(InstagramPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class InstagramUserIE(InstagramPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class InternazionaleIE(LazyLoadExtractor):
    IE_NAME: str

class InternetVideoArchiveIE(LazyLoadExtractor):
    IE_NAME: str

class InvestigationDiscoveryIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class IqAlbumIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class IqIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class IqiyiIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class IslamChannelIE(LazyLoadExtractor):
    IE_NAME: str

class IslamChannelSeriesIE(LazyLoadExtractor):
    IE_NAME: str

class IsraelNationalNewsIE(LazyLoadExtractor):
    IE_NAME: str

class IviCompilationIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class IviIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class IvideonIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class IvooxIE(LazyLoadExtractor):
    IE_NAME: str

class IwaraBaseIE(LazyLoadExtractor):
    IE_NAME: str

class IwaraIE(IwaraBaseIE):
    IE_NAME: str
    age_limit: int

class IwaraPlaylistIE(IwaraBaseIE):
    IE_NAME: str

class IwaraUserIE(IwaraBaseIE):
    IE_NAME: str

class IxiguaIE(LazyLoadExtractor):
    IE_NAME: str

class IzleseneIE(LazyLoadExtractor):
    IE_NAME: str

class JStreamIE(LazyLoadExtractor):
    IE_NAME: str

class JTBCIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class JTBCProgramIE(LazyLoadExtractor):
    IE_NAME: str

class JWPlatformIE(LazyLoadExtractor):
    IE_NAME: str

class JamendoIE(LazyLoadExtractor):
    IE_NAME: str

class JamendoAlbumIE(JamendoIE):
    IE_NAME: str

class JeuxVideoIE(LazyLoadExtractor):
    IE_NAME: str

class JioSaavnBaseIE(LazyLoadExtractor):
    IE_NAME: str

class JioSaavnAlbumIE(JioSaavnBaseIE):
    IE_NAME: str

class JioSaavnArtistIE(JioSaavnBaseIE):
    IE_NAME: str

class JioSaavnPlaylistIE(JioSaavnBaseIE):
    IE_NAME: str

class JioSaavnShowIE(JioSaavnBaseIE):
    IE_NAME: str

class JioSaavnShowPlaylistIE(JioSaavnBaseIE):
    IE_NAME: str

class JioSaavnSongIE(JioSaavnBaseIE):
    IE_NAME: str

class JojIE(LazyLoadExtractor):
    IE_NAME: str

class JoqrAgIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class JoveIE(LazyLoadExtractor):
    IE_NAME: str

class KTHIE(LazyLoadExtractor):
    IE_NAME: str

class KakaoIE(LazyLoadExtractor):
    IE_NAME: str

class KalturaIE(LazyLoadExtractor):
    IE_NAME: str

class KankaNewsIE(LazyLoadExtractor):
    IE_NAME: str

class KaraoketvIE(LazyLoadExtractor):
    IE_NAME: str

class KatsomoIE(LazyLoadExtractor):
    IE_NAME: str

class KelbyOneIE(LazyLoadExtractor):
    IE_NAME: str

class Kenh14PlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class Kenh14VideoIE(LazyLoadExtractor):
    IE_NAME: str

class KhanAcademyBaseIE(LazyLoadExtractor):
    IE_NAME: str

class KhanAcademyIE(KhanAcademyBaseIE):
    IE_NAME: str

class KhanAcademyUnitIE(KhanAcademyBaseIE):
    IE_NAME: str

class KickBaseIE(LazyLoadExtractor):
    IE_NAME: str

class KickClipIE(KickBaseIE):
    IE_NAME: str
    age_limit: int

class KickIE(KickBaseIE):
    IE_NAME: str
    age_limit: int
    @classmethod
    def suitable(cls, url): ...

class KickStarterIE(LazyLoadExtractor):
    IE_NAME: str

class KickVODIE(KickBaseIE):
    IE_NAME: str

class KickerIE(LazyLoadExtractor):
    IE_NAME: str

class KikaIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class KikaPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class KinjaEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class KinoPoiskIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class UnsupportedInfoExtractor(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class KnownDRMIE(UnsupportedInfoExtractor):
    IE_NAME: str
    IE_DESC: bool

class KnownPiracyIE(UnsupportedInfoExtractor):
    IE_NAME: str
    IE_DESC: bool

class KommunetvIE(LazyLoadExtractor):
    IE_NAME: str

class JixieBaseIE(LazyLoadExtractor):
    IE_NAME: str

class KompasVideoIE(JixieBaseIE):
    IE_NAME: str

class KooIE(LazyLoadExtractor):
    IE_NAME: str

class KrasViewIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class Ku6IE(LazyLoadExtractor):
    IE_NAME: str

class KukuluLiveIE(LazyLoadExtractor):
    IE_NAME: str

class KuwoAlbumIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class KuwoCategoryIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class KuwoChartIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class KuwoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class KuwoIE(KuwoBaseIE):
    IE_NAME: str
    IE_DESC: str

class KuwoMvIE(KuwoBaseIE):
    IE_NAME: str
    IE_DESC: str

class KuwoSingerIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class LA7IE(LazyLoadExtractor):
    IE_NAME: str

class LA7PodcastEpisodeIE(LazyLoadExtractor):
    IE_NAME: str

class LA7PodcastIE(LA7PodcastEpisodeIE):
    IE_NAME: str

class LBRYBaseIE(LazyLoadExtractor):
    IE_NAME: str

class LBRYChannelIE(LBRYBaseIE):
    IE_NAME: str
    IE_DESC: str

class LBRYIE(LBRYBaseIE):
    IE_NAME: str
    IE_DESC: str

class LBRYPlaylistIE(LBRYBaseIE):
    IE_NAME: str
    IE_DESC: str

class LCIIE(LazyLoadExtractor):
    IE_NAME: str

class LEGOIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class LRTBaseIE(LazyLoadExtractor):
    IE_NAME: str

class LRTRadioIE(LRTBaseIE):
    IE_NAME: str

class LRTStreamIE(LRTBaseIE):
    IE_NAME: str

class LRTVODIE(LRTBaseIE):
    IE_NAME: str

class LSMLREmbedIE(LazyLoadExtractor):
    IE_NAME: str

class LSMLTVEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class LSMReplayIE(LazyLoadExtractor):
    IE_NAME: str

class LaXarxaMesIE(LazyLoadExtractor):
    IE_NAME: str

class LaracastsBaseIE(LazyLoadExtractor):
    IE_NAME: str

class LaracastsIE(LaracastsBaseIE):
    IE_NAME: str

class LaracastsPlaylistIE(LaracastsBaseIE):
    IE_NAME: str

class LastFMIE(LazyLoadExtractor):
    IE_NAME: str

class LastFMPlaylistBaseIE(LazyLoadExtractor):
    IE_NAME: str

class LastFMPlaylistIE(LastFMPlaylistBaseIE):
    IE_NAME: str

class LastFMUserIE(LastFMPlaylistBaseIE):
    IE_NAME: str

class LcpIE(LazyLoadExtractor):
    IE_NAME: str

class LcpPlayIE(ArkenaIE):
    IE_NAME: str

class LeFigaroVideoEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class LeFigaroVideoSectionIE(LazyLoadExtractor):
    IE_NAME: str

class LeIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class LePlaylistIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class LearningOnScreenIE(LazyLoadExtractor):
    IE_NAME: str

class Lecture2GoIE(LazyLoadExtractor):
    IE_NAME: str

class LecturioBaseIE(LazyLoadExtractor):
    IE_NAME: str

class LecturioCourseIE(LecturioBaseIE):
    IE_NAME: str

class LecturioDeCourseIE(LecturioBaseIE):
    IE_NAME: str

class LecturioIE(LecturioBaseIE):
    IE_NAME: str

class LemondeIE(LazyLoadExtractor):
    IE_NAME: str

class LentaIE(LazyLoadExtractor):
    IE_NAME: str

class LetvCloudIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class LiTVIE(LazyLoadExtractor):
    IE_NAME: str

class LibraryOfCongressIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class LibsynIE(LazyLoadExtractor):
    IE_NAME: str

class LifeEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class LifeNewsIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class LikeeIE(LazyLoadExtractor):
    IE_NAME: str

class LikeeUserIE(LazyLoadExtractor):
    IE_NAME: str

class LimelightBaseIE(LazyLoadExtractor):
    IE_NAME: str

class LimelightChannelIE(LimelightBaseIE):
    IE_NAME: str

class LimelightChannelListIE(LimelightBaseIE):
    IE_NAME: str

class LimelightMediaIE(LimelightBaseIE):
    IE_NAME: str

class LinkedInBaseIE(LazyLoadExtractor):
    IE_NAME: str

class LinkedInEventsIE(LinkedInBaseIE):
    IE_NAME: str

class LinkedInIE(LinkedInBaseIE):
    IE_NAME: str

class LinkedInLearningBaseIE(LinkedInBaseIE):
    IE_NAME: str

class LinkedInLearningCourseIE(LinkedInLearningBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class LinkedInLearningIE(LinkedInLearningBaseIE):
    IE_NAME: str

class Liputan6IE(LazyLoadExtractor):
    IE_NAME: str

class ListenNotesIE(LazyLoadExtractor):
    IE_NAME: str

class LiveJournalIE(LazyLoadExtractor):
    IE_NAME: str

class LivestreamIE(LazyLoadExtractor):
    IE_NAME: str

class LivestreamOriginalIE(LazyLoadExtractor):
    IE_NAME: str

class LivestreamShortenerIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class LivestreamfailsIE(LazyLoadExtractor):
    IE_NAME: str

class LnkIE(LazyLoadExtractor):
    IE_NAME: str

class LocoIE(LazyLoadExtractor):
    IE_NAME: str

class LoomFolderIE(LazyLoadExtractor):
    IE_NAME: str

class LoomIE(LazyLoadExtractor):
    IE_NAME: str

class NuevoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class LoveHomePornIE(NuevoBaseIE):
    IE_NAME: str
    age_limit: int

class LumniIE(FranceTVBaseInfoExtractor):
    IE_NAME: str

class LyndaBaseIE(LazyLoadExtractor):
    IE_NAME: str

class LyndaCourseIE(LyndaBaseIE):
    IE_NAME: str
    IE_DESC: str

class LyndaIE(LyndaBaseIE):
    IE_NAME: str
    IE_DESC: str

class MBNIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MDRIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MGTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MLBArticleIE(LazyLoadExtractor):
    IE_NAME: str

class MLBBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MLBIE(MLBBaseIE):
    IE_NAME: str

class MLBTVIE(LazyLoadExtractor):
    IE_NAME: str

class MLBVideoIE(MLBBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class MLSSoccerIE(LazyLoadExtractor):
    IE_NAME: str

class MNetTVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class MNetTVIE(MNetTVBaseIE):
    IE_NAME: str

class MNetTVLiveIE(MNetTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class MNetTVRecordingsIE(MNetTVBaseIE):
    IE_NAME: str

class MSNIE(LazyLoadExtractor):
    IE_NAME: str

class MTVDEIE(MTVServicesInfoExtractor):
    IE_NAME: str

class MTVIE(MTVServicesInfoExtractor):
    IE_NAME: str

class CMTIE(MTVIE):
    IE_NAME: str

class MTVItaliaIE(MTVServicesInfoExtractor):
    IE_NAME: str

class MTVItaliaProgrammaIE(MTVItaliaIE):
    IE_NAME: str

class MTVJapanIE(MTVServicesInfoExtractor):
    IE_NAME: str

class MTVServicesEmbeddedIE(MTVServicesInfoExtractor):
    IE_NAME: str

class MTVUutisetArticleIE(LazyLoadExtractor):
    IE_NAME: str

class MTVVideoIE(MTVServicesInfoExtractor):
    IE_NAME: str

class MaarivIE(LazyLoadExtractor):
    IE_NAME: str

class MagellanTVIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class MagentaMusikIE(LazyLoadExtractor):
    IE_NAME: str

class MailRuIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MailRuMusicSearchBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MailRuMusicIE(MailRuMusicSearchBaseIE):
    IE_NAME: str
    IE_DESC: str

class MailRuMusicSearchIE(MailRuMusicSearchBaseIE):
    IE_NAME: str
    IE_DESC: str

class MainStreamingIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MangomoloBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MangomoloLiveIE(MangomoloBaseIE):
    IE_NAME: str

class MangomoloVideoIE(MangomoloBaseIE):
    IE_NAME: str

class ManotoTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ManotoTVLiveIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ManotoTVShowIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ManyVidsIE(LazyLoadExtractor):
    IE_NAME: str

class MaoriTVIE(LazyLoadExtractor):
    IE_NAME: str

class MarkizaIE(LazyLoadExtractor):
    IE_NAME: str

class MarkizaPageIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class MassengeschmackTVIE(LazyLoadExtractor):
    IE_NAME: str

class MastersIE(LazyLoadExtractor):
    IE_NAME: str

class MatchTVIE(LazyLoadExtractor):
    IE_NAME: str

class MaveIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class MeWatchIE(LazyLoadExtractor):
    IE_NAME: str

class MedalTVIE(LazyLoadExtractor):
    IE_NAME: str

class MediaKlikkIE(LazyLoadExtractor):
    IE_NAME: str

class MediaStreamBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MediaStreamIE(MediaStreamBaseIE):
    IE_NAME: str

class MediaWorksNZVODIE(LazyLoadExtractor):
    IE_NAME: str

class MediaiteIE(LazyLoadExtractor):
    IE_NAME: str

class MedialaanIE(LazyLoadExtractor):
    IE_NAME: str

class MediasetIE(ThePlatformBaseIE):
    IE_NAME: str

class MediasetShowIE(MediasetIE):
    IE_NAME: str

class MediasiteCatalogIE(LazyLoadExtractor):
    IE_NAME: str

class MediasiteIE(LazyLoadExtractor):
    IE_NAME: str

class MediasiteNamedCatalogIE(LazyLoadExtractor):
    IE_NAME: str

class MediciIE(LazyLoadExtractor):
    IE_NAME: str

class MegaTVComBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MegaTVComEmbedIE(MegaTVComBaseIE):
    IE_NAME: str
    IE_DESC: str

class MegaTVComIE(MegaTVComBaseIE):
    IE_NAME: str
    IE_DESC: str

class MegaphoneIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MeipaiIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MelonVODIE(LazyLoadExtractor):
    IE_NAME: str

class MetacriticIE(LazyLoadExtractor):
    IE_NAME: str

class TelecincoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MiTeleIE(TelecincoBaseIE):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class MicrosoftBuildIE(LazyLoadExtractor):
    IE_NAME: str

class MicrosoftEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class MicrosoftMediusBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MicrosoftLearnEpisodeIE(MicrosoftMediusBaseIE):
    IE_NAME: str

class MicrosoftLearnPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class MicrosoftLearnSessionIE(LazyLoadExtractor):
    IE_NAME: str

class MicrosoftMediusIE(MicrosoftMediusBaseIE):
    IE_NAME: str

class MicrosoftStreamIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MindsBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MindsFeedBaseIE(MindsBaseIE):
    IE_NAME: str

class MindsChannelIE(MindsFeedBaseIE):
    IE_NAME: str

class MindsGroupIE(MindsFeedBaseIE):
    IE_NAME: str

class MindsIE(MindsBaseIE):
    IE_NAME: str

class MinotoIE(LazyLoadExtractor):
    IE_NAME: str

class MirrativBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MirrativIE(MirrativBaseIE):
    IE_NAME: str

class MirrativUserIE(MirrativBaseIE):
    IE_NAME: str

class MirrorCoUKIE(LazyLoadExtractor):
    IE_NAME: str

class MixchArchiveIE(LazyLoadExtractor):
    IE_NAME: str

class MixchIE(LazyLoadExtractor):
    IE_NAME: str

class MixchMovieIE(LazyLoadExtractor):
    IE_NAME: str

class MixcloudBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MixcloudIE(MixcloudBaseIE):
    IE_NAME: str

class MixcloudPlaylistBaseIE(MixcloudBaseIE):
    IE_NAME: str

class MixcloudPlaylistIE(MixcloudPlaylistBaseIE):
    IE_NAME: str

class MixcloudUserIE(MixcloudPlaylistBaseIE):
    IE_NAME: str

class MmsIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class MochaVideoIE(LazyLoadExtractor):
    IE_NAME: str

class MojevideoIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MojvideoIE(LazyLoadExtractor):
    IE_NAME: str

class MonsterSirenHypergryphMusicIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MonstercatIE(LazyLoadExtractor):
    IE_NAME: str

class MotherlessPaginatedIE(LazyLoadExtractor):
    IE_NAME: str

class MotherlessGalleryIE(MotherlessPaginatedIE):
    IE_NAME: str

class MotherlessGroupIE(MotherlessPaginatedIE):
    IE_NAME: str

class MotherlessIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class MotherlessUploaderIE(MotherlessPaginatedIE):
    IE_NAME: str

class MotorsportIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MovieFapIE(TNAFlixNetworkBaseIE):
    IE_NAME: str
    age_limit: int

class MoviepilotIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MoviewPlayIE(JixieBaseIE):
    IE_NAME: str

class MoviezineIE(LazyLoadExtractor):
    IE_NAME: str

class MovingImageIE(LazyLoadExtractor):
    IE_NAME: str

class MuenchenTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class RozhlasBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MujRozhlasIE(RozhlasBaseIE):
    IE_NAME: str

class MurrtubeIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class MurrtubeUserIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class MuseAIIE(LazyLoadExtractor):
    IE_NAME: str

class MuseScoreIE(LazyLoadExtractor):
    IE_NAME: str

class MusicdexBaseIE(LazyLoadExtractor):
    IE_NAME: str

class MusicdexAlbumIE(MusicdexBaseIE):
    IE_NAME: str

class MusicdexPageIE(MusicdexBaseIE):
    IE_NAME: str

class MusicdexArtistIE(MusicdexPageIE):
    IE_NAME: str

class MusicdexPlaylistIE(MusicdexPageIE):
    IE_NAME: str

class MusicdexSongIE(MusicdexBaseIE):
    IE_NAME: str

class Mx3BaseIE(LazyLoadExtractor):
    IE_NAME: str

class Mx3IE(Mx3BaseIE):
    IE_NAME: str

class Mx3NeoIE(Mx3BaseIE):
    IE_NAME: str

class Mx3VolksmusikIE(Mx3BaseIE):
    IE_NAME: str

class MxplayerIE(LazyLoadExtractor):
    IE_NAME: str

class MxplayerShowIE(LazyLoadExtractor):
    IE_NAME: str

class MySpaceAlbumIE(LazyLoadExtractor):
    IE_NAME: str

class MySpaceIE(LazyLoadExtractor):
    IE_NAME: str

class MySpassIE(LazyLoadExtractor):
    IE_NAME: str

class MyVideoGeIE(LazyLoadExtractor):
    IE_NAME: str

class MyVidsterIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class MzaaloIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class N1InfoAssetIE(LazyLoadExtractor):
    IE_NAME: str

class N1InfoIIE(LazyLoadExtractor):
    IE_NAME: str

class NBACVPBaseIE(TurnerBaseIE):
    IE_NAME: str

class NBABaseIE(NBACVPBaseIE):
    IE_NAME: str

class NBAChannelIE(NBABaseIE):
    IE_NAME: str

class NBAEmbedIE(NBABaseIE):
    IE_NAME: str

class NBAIE(NBABaseIE):
    IE_NAME: str

class NBAWatchBaseIE(NBACVPBaseIE):
    IE_NAME: str

class NBAWatchCollectionIE(NBAWatchBaseIE):
    IE_NAME: str

class NBAWatchEmbedIE(NBAWatchBaseIE):
    IE_NAME: str

class NBAWatchIE(NBAWatchBaseIE):
    IE_NAME: str

class NBCIE(NBCUniversalBaseIE):
    IE_NAME: str
    age_limit: int

class NBCOlympicsIE(LazyLoadExtractor):
    IE_NAME: str

class NBCOlympicsStreamIE(AdobePassIE):
    IE_NAME: str

class NBCSportsIE(LazyLoadExtractor):
    IE_NAME: str

class NBCSportsStreamIE(AdobePassIE):
    IE_NAME: str

class NBCSportsVPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class NBCStationsIE(LazyLoadExtractor):
    IE_NAME: str

class NDREmbedBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NDREmbedIE(NDREmbedBaseIE):
    IE_NAME: str

class NDRBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NDRIE(NDRBaseIE):
    IE_NAME: str
    IE_DESC: str

class NDTVIE(LazyLoadExtractor):
    IE_NAME: str

class NFBBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NFBIE(NFBBaseIE):
    IE_NAME: str
    IE_DESC: str

class NFBSeriesIE(NFBBaseIE):
    IE_NAME: str
    IE_DESC: str

class NFHSNetworkIE(LazyLoadExtractor):
    IE_NAME: str

class NFLBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NFLArticleIE(NFLBaseIE):
    IE_NAME: str

class NFLIE(NFLBaseIE):
    IE_NAME: str

class NFLPlusEpisodeIE(NFLBaseIE):
    IE_NAME: str

class NFLPlusReplayIE(NFLBaseIE):
    IE_NAME: str

class NHLBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NHLIE(NHLBaseIE):
    IE_NAME: str

class NJoyEmbedIE(NDREmbedBaseIE):
    IE_NAME: str

class NJoyIE(NDRBaseIE):
    IE_NAME: str
    IE_DESC: str

class NOSNLArticleIE(LazyLoadExtractor):
    IE_NAME: str

class NPOIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class NPOPlaylistBaseIE(NPOIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class AndereTijdenIE(NPOPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class NPOLiveIE(LazyLoadExtractor):
    IE_NAME: str

class NPORadioFragmentIE(LazyLoadExtractor):
    IE_NAME: str

class NPORadioIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class NRKBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NRKIE(NRKBaseIE):
    IE_NAME: str

class NRKPlaylistBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NRKPlaylistIE(NRKPlaylistBaseIE):
    IE_NAME: str

class NRKRadioPodkastIE(LazyLoadExtractor):
    IE_NAME: str

class NRKSkoleIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class NRKTVEpisodeIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class NRKTVEpisodesIE(NRKPlaylistBaseIE):
    IE_NAME: str

class NRKTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class NRKTVDirekteIE(NRKTVIE):
    IE_NAME: str
    IE_DESC: str

class NRKTVSerieBaseIE(NRKBaseIE):
    IE_NAME: str

class NRKTVSeasonIE(NRKTVSerieBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class NRKTVSeriesIE(NRKTVSerieBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class NRLTVIE(LazyLoadExtractor):
    IE_NAME: str

class NTSLiveIE(LazyLoadExtractor):
    IE_NAME: str

class StreaksBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NTVCoJpCUIE(StreaksBaseIE):
    IE_NAME: str
    IE_DESC: str

class NTVDeIE(LazyLoadExtractor):
    IE_NAME: str

class NTVRuIE(LazyLoadExtractor):
    IE_NAME: str

class NYTimesBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NYTimesArticleIE(NYTimesBaseIE):
    IE_NAME: str

class NYTimesCookingIE(NYTimesBaseIE):
    IE_NAME: str

class NYTimesCookingRecipeIE(LazyLoadExtractor):
    IE_NAME: str

class NYTimesIE(NYTimesBaseIE):
    IE_NAME: str

class NZHeraldIE(LazyLoadExtractor):
    IE_NAME: str

class NZOnScreenIE(LazyLoadExtractor):
    IE_NAME: str

class NZZIE(LazyLoadExtractor):
    IE_NAME: str

class NateIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class NateProgramIE(LazyLoadExtractor):
    IE_NAME: str

class NationalGeographicTVIE(FOXIE):
    IE_NAME: str
    age_limit: int

class NationalGeographicVideoIE(LazyLoadExtractor):
    IE_NAME: str

class NaverBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NaverIE(NaverBaseIE):
    IE_NAME: str

class NaverLiveIE(NaverBaseIE):
    IE_NAME: str

class NaverNowIE(NaverBaseIE):
    IE_NAME: str

class NebulaBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NebulaChannelIE(NebulaBaseIE):
    IE_NAME: str

class NebulaClassIE(NebulaBaseIE):
    IE_NAME: str

class NebulaIE(NebulaBaseIE):
    IE_NAME: str

class NebulaSubscriptionsIE(NebulaBaseIE):
    IE_NAME: str

class NekoHackerIE(LazyLoadExtractor):
    IE_NAME: str

class NerdCubedFeedIE(LazyLoadExtractor):
    IE_NAME: str

class NestClipIE(LazyLoadExtractor):
    IE_NAME: str

class NestIE(LazyLoadExtractor):
    IE_NAME: str

class NetEaseMusicBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NetEaseMusicAlbumIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicDjRadioIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicListIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicMvIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicProgramIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicSingerIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetPlusTVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class NetPlusTVIE(NetPlusTVBaseIE):
    IE_NAME: str

class NetPlusTVLiveIE(NetPlusTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class NetPlusTVRecordingsIE(NetPlusTVBaseIE):
    IE_NAME: str

class NetverseBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NetverseIE(NetverseBaseIE):
    IE_NAME: str

class NetversePlaylistIE(NetverseBaseIE):
    IE_NAME: str

class NetverseSearchIE(LazyLoadSearchExtractor):
    IE_NAME: str
    SEARCH_KEY: str

class NetzkinoIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class NewgroundsIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class NewgroundsPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class NewgroundsUserIE(LazyLoadExtractor):
    IE_NAME: str

class NewsPicksIE(LazyLoadExtractor):
    IE_NAME: str

class NewsyIE(LazyLoadExtractor):
    IE_NAME: str

class NextMediaIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class AppleDailyIE(NextMediaIE):
    IE_NAME: str
    IE_DESC: str

class NextMediaActionNewsIE(NextMediaIE):
    IE_NAME: str
    IE_DESC: str

class NextTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class NexxEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class NexxIE(LazyLoadExtractor):
    IE_NAME: str

class NhkForSchoolBangumiIE(LazyLoadExtractor):
    IE_NAME: str

class NhkForSchoolProgramListIE(LazyLoadExtractor):
    IE_NAME: str

class NhkForSchoolSubjectIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class NhkRadioNewsPageIE(LazyLoadExtractor):
    IE_NAME: str

class NhkRadiruIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class NhkRadiruLiveIE(LazyLoadExtractor):
    IE_NAME: str

class NhkBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NhkVodIE(NhkBaseIE):
    IE_NAME: str

class NhkVodProgramIE(NhkBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class NickBrIE(MTVServicesInfoExtractor):
    IE_NAME: str

class NickDeIE(MTVServicesInfoExtractor):
    IE_NAME: str

class NickIE(MTVServicesInfoExtractor):
    IE_NAME: str

class NickRuIE(MTVServicesInfoExtractor):
    IE_NAME: str

class NiconicoChannelPlusBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NiconicoChannelPlusChannelBaseIE(NiconicoChannelPlusBaseIE):
    IE_NAME: str

class NiconicoChannelPlusChannelLivesIE(NiconicoChannelPlusChannelBaseIE):
    IE_NAME: str
    IE_DESC: str

class NiconicoChannelPlusChannelVideosIE(NiconicoChannelPlusChannelBaseIE):
    IE_NAME: str
    IE_DESC: str

class NiconicoChannelPlusIE(NiconicoChannelPlusBaseIE):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class NiconicoPlaylistBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NiconicoHistoryIE(NiconicoPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class NiconicoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NiconicoIE(NiconicoBaseIE):
    IE_NAME: str
    IE_DESC: str

class NiconicoLiveIE(NiconicoBaseIE):
    IE_NAME: str
    IE_DESC: str

class NiconicoPlaylistIE(NiconicoPlaylistBaseIE):
    IE_NAME: str

class NiconicoSeriesIE(NiconicoPlaylistBaseIE):
    IE_NAME: str

class NiconicoUserIE(LazyLoadExtractor):
    IE_NAME: str

class NicovideoSearchBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NicovideoSearchDateIE(NicovideoSearchBaseIE, LazyLoadSearchExtractor):
    IE_NAME: str
    IE_DESC: str
    SEARCH_KEY: str

class NicovideoSearchIE(NicovideoSearchBaseIE, LazyLoadSearchExtractor):
    IE_NAME: str
    IE_DESC: str
    SEARCH_KEY: str

class NicovideoSearchURLIE(NicovideoSearchBaseIE):
    IE_NAME: str
    IE_DESC: str

class NicovideoTagURLIE(NicovideoSearchBaseIE):
    IE_NAME: str
    IE_DESC: str

class NinaProtocolIE(LazyLoadExtractor):
    IE_NAME: str

class NineCNineMediaIE(LazyLoadExtractor):
    IE_NAME: str

class NineGagIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class NineNewsIE(LazyLoadExtractor):
    IE_NAME: str

class NineNowIE(LazyLoadExtractor):
    IE_NAME: str

class NintendoIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class NitterIE(LazyLoadExtractor):
    IE_NAME: str

class NobelPrizeIE(LazyLoadExtractor):
    IE_NAME: str

class NoicePodcastIE(LazyLoadExtractor):
    IE_NAME: str

class NonkTubeIE(NuevoBaseIE):
    IE_NAME: str
    age_limit: int

class NoodleMagazineIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class NoovoIE(LazyLoadExtractor):
    IE_NAME: str

class NovaEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class NovaIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class NovaPlayIE(LazyLoadExtractor):
    IE_NAME: str

class NownessBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NownessIE(NownessBaseIE):
    IE_NAME: str

class NownessPlaylistIE(NownessBaseIE):
    IE_NAME: str

class NownessSeriesIE(NownessBaseIE):
    IE_NAME: str

class NozIE(LazyLoadExtractor):
    IE_NAME: str

class NprIE(LazyLoadExtractor):
    IE_NAME: str

class NubilesPornIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class NuumBaseIE(LazyLoadExtractor):
    IE_NAME: str

class NuumLiveIE(NuumBaseIE):
    IE_NAME: str

class NuumMediaIE(NuumBaseIE):
    IE_NAME: str

class NuumTabIE(NuumBaseIE):
    IE_NAME: str

class NuvidIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class OCWMITIE(LazyLoadExtractor):
    IE_NAME: str

class ORFFM4StoryIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ORFIPTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ORFONIE(LazyLoadExtractor):
    IE_NAME: str

class ORFPodcastIE(LazyLoadExtractor):
    IE_NAME: str

class ORFRadioIE(LazyLoadExtractor):
    IE_NAME: str

class OdnoklassnikiIE(LazyLoadExtractor):
    IE_NAME: str

class OfTVIE(LazyLoadExtractor):
    IE_NAME: str

class OfTVPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class OktoberfestTVIE(LazyLoadExtractor):
    IE_NAME: str

class OlympicsReplayIE(LazyLoadExtractor):
    IE_NAME: str

class On24IE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class OnDemandChinaEpisodeIE(LazyLoadExtractor):
    IE_NAME: str

class OnDemandKoreaIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class OnDemandKoreaProgramIE(LazyLoadExtractor):
    IE_NAME: str

class OneFootballIE(LazyLoadExtractor):
    IE_NAME: str

class OneNewsNZIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class OnePlacePodcastIE(LazyLoadExtractor):
    IE_NAME: str

class OnetChannelIE(OnetBaseIE):
    IE_NAME: str

class OnetIE(OnetBaseIE):
    IE_NAME: str

class OnetMVPIE(OnetBaseIE):
    IE_NAME: str

class OnetPlIE(LazyLoadExtractor):
    IE_NAME: str

class OnionStudiosIE(LazyLoadExtractor):
    IE_NAME: str

class OpenRecBaseIE(LazyLoadExtractor):
    IE_NAME: str

class OpenRecCaptureIE(OpenRecBaseIE):
    IE_NAME: str

class OpenRecIE(OpenRecBaseIE):
    IE_NAME: str

class OpenRecMovieIE(OpenRecBaseIE):
    IE_NAME: str

class OpencastBaseIE(LazyLoadExtractor):
    IE_NAME: str

class OpencastIE(OpencastBaseIE):
    IE_NAME: str

class OpencastPlaylistIE(OpencastBaseIE):
    IE_NAME: str

class OraTVIE(LazyLoadExtractor):
    IE_NAME: str

class OsnatelTVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class OsnatelTVIE(OsnatelTVBaseIE):
    IE_NAME: str

class OsnatelTVLiveIE(OsnatelTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class OsnatelTVRecordingsIE(OsnatelTVBaseIE):
    IE_NAME: str

class OutsideTVIE(LazyLoadExtractor):
    IE_NAME: str

class OwnCloudIE(LazyLoadExtractor):
    IE_NAME: str

class PBSIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class PBSKidsIE(LazyLoadExtractor):
    IE_NAME: str

class PGATourIE(LazyLoadExtractor):
    IE_NAME: str

class PRXBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PRXAccountIE(PRXBaseIE):
    IE_NAME: str

class PRXSeriesIE(PRXBaseIE):
    IE_NAME: str

class PRXSeriesSearchIE(PRXBaseIE, LazyLoadSearchExtractor):
    IE_NAME: str
    IE_DESC: str
    SEARCH_KEY: str

class PRXStoriesSearchIE(PRXBaseIE, LazyLoadSearchExtractor):
    IE_NAME: str
    IE_DESC: str
    SEARCH_KEY: str

class PRXStoryIE(PRXBaseIE):
    IE_NAME: str

class PacktPubBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PacktPubCourseIE(PacktPubBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PacktPubIE(PacktPubBaseIE):
    IE_NAME: str

class PalcoMP3BaseIE(LazyLoadExtractor):
    IE_NAME: str

class PalcoMP3ArtistIE(PalcoMP3BaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PalcoMP3IE(PalcoMP3BaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PalcoMP3VideoIE(PalcoMP3BaseIE):
    IE_NAME: str

class PanoptoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PanoptoIE(PanoptoBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PanoptoListIE(PanoptoBaseIE):
    IE_NAME: str

class PanoptoPlaylistIE(PanoptoBaseIE):
    IE_NAME: str

class ParamountNetworkIE(MTVServicesInfoExtractor):
    IE_NAME: str

class ParamountPlusSeriesIE(LazyLoadExtractor):
    IE_NAME: str

class ParamountPressExpressIE(LazyLoadExtractor):
    IE_NAME: str

class ParlerIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class RedBeeBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ParliamentLiveUKIE(RedBeeBaseIE):
    IE_NAME: str
    IE_DESC: str

class ParlviewIE(LazyLoadExtractor):
    IE_NAME: str

class PartiBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PartiLivestreamIE(PartiBaseIE):
    IE_NAME: str

class PartiVideoIE(PartiBaseIE):
    IE_NAME: str

class PatreonBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PatreonCampaignIE(PatreonBaseIE):
    IE_NAME: str

class PatreonIE(PatreonBaseIE):
    IE_NAME: str

class PearVideoIE(LazyLoadExtractor):
    IE_NAME: str

class PeekVidsBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PeekVidsIE(PeekVidsBaseIE):
    IE_NAME: str
    age_limit: int

class PeerTVIE(LazyLoadExtractor):
    IE_NAME: str

class PeerTubeIE(LazyLoadExtractor):
    IE_NAME: str

class PeerTubePlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class PelotonIE(LazyLoadExtractor):
    IE_NAME: str

class PelotonLiveIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class PerformGroupIE(LazyLoadExtractor):
    IE_NAME: str

class PeriscopeBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PeriscopeIE(PeriscopeBaseIE):
    IE_NAME: str
    IE_DESC: str

class PeriscopeUserIE(PeriscopeBaseIE):
    IE_NAME: str
    IE_DESC: str

class PhilharmonieDeParisIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class PhoenixIE(ZDFBaseIE):
    IE_NAME: str

class PhotobucketIE(LazyLoadExtractor):
    IE_NAME: str

class PiaLiveIE(LazyLoadExtractor):
    IE_NAME: str

class PiaproIE(LazyLoadExtractor):
    IE_NAME: str

class PicartoIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PicartoVodIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class PikselIE(LazyLoadExtractor):
    IE_NAME: str

class PinkbikeIE(LazyLoadExtractor):
    IE_NAME: str

class PinterestBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PinterestCollectionIE(PinterestBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PinterestIE(PinterestBaseIE):
    IE_NAME: str

class PiramideTVChannelIE(LazyLoadExtractor):
    IE_NAME: str

class PiramideTVIE(LazyLoadExtractor):
    IE_NAME: str

class PixivSketchBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PixivSketchIE(PixivSketchBaseIE):
    IE_NAME: str
    age_limit: int

class PixivSketchUserIE(PixivSketchBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PlVideoIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class PladformIE(LazyLoadExtractor):
    IE_NAME: str

class PlanetMarathiIE(LazyLoadExtractor):
    IE_NAME: str

class PlatziBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PlatziCourseIE(PlatziBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PlatziIE(PlatziBaseIE):
    IE_NAME: str

class PlayPlusTVIE(LazyLoadExtractor):
    IE_NAME: str

class PlaySuisseIE(LazyLoadExtractor):
    IE_NAME: str

class PlayVidsIE(PeekVidsBaseIE):
    IE_NAME: str
    age_limit: int

class PlaytvakIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class PlaywireIE(LazyLoadExtractor):
    IE_NAME: str

class PluralsightBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PluralsightCourseIE(PluralsightBaseIE):
    IE_NAME: str

class PluralsightIE(PluralsightBaseIE):
    IE_NAME: str

class PlutoTVIE(LazyLoadExtractor):
    IE_NAME: str

class PodbayFMChannelIE(LazyLoadExtractor):
    IE_NAME: str

class PodbayFMIE(LazyLoadExtractor):
    IE_NAME: str

class PodchaserIE(LazyLoadExtractor):
    IE_NAME: str

class PodomaticIE(LazyLoadExtractor):
    IE_NAME: str

class PokerGoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PokerGoCollectionIE(PokerGoBaseIE):
    IE_NAME: str

class PokerGoIE(PokerGoBaseIE):
    IE_NAME: str

class PolsatGoIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class PolskieRadioAuditionIE(LazyLoadExtractor):
    IE_NAME: str

class PolskieRadioCategoryIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PolskieRadioBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PolskieRadioIE(PolskieRadioBaseIE):
    IE_NAME: str

class PolskieRadioLegacyIE(PolskieRadioBaseIE):
    IE_NAME: str

class PolskieRadioPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class PolskieRadioPodcastBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PolskieRadioPodcastIE(PolskieRadioPodcastBaseIE):
    IE_NAME: str

class PolskieRadioPodcastListIE(PolskieRadioPodcastBaseIE):
    IE_NAME: str

class PopcornTVIE(LazyLoadExtractor):
    IE_NAME: str

class PopcorntimesIE(LazyLoadExtractor):
    IE_NAME: str

class PornFlipIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class PornHubBaseIE(LazyLoadExtractor):
    IE_NAME: str

class PornHubIE(PornHubBaseIE):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class PornHubPlaylistBaseIE(PornHubBaseIE):
    IE_NAME: str

class PornHubPagedPlaylistBaseIE(PornHubPlaylistBaseIE):
    IE_NAME: str

class PornHubPagedVideoListIE(PornHubPagedPlaylistBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PornHubPlaylistIE(PornHubPlaylistBaseIE):
    IE_NAME: str

class PornHubUserIE(PornHubPlaylistBaseIE):
    IE_NAME: str

class PornHubUserVideosUploadIE(PornHubPagedPlaylistBaseIE):
    IE_NAME: str

class PornTopIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class PornTubeIE(FourTubeBaseIE):
    IE_NAME: str
    age_limit: int

class PornboxIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class PornerBrosIE(FourTubeBaseIE):
    IE_NAME: str
    age_limit: int

class PornoVoisinesIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class PornoXOIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class PornotubeIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class Pr0grammIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class PrankCastIE(LazyLoadExtractor):
    IE_NAME: str

class PrankCastPostIE(LazyLoadExtractor):
    IE_NAME: str

class PremiershipRugbyIE(LazyLoadExtractor):
    IE_NAME: str

class PressTVIE(LazyLoadExtractor):
    IE_NAME: str

class ProSiebenSat1BaseIE(LazyLoadExtractor):
    IE_NAME: str

class ProSiebenSat1IE(ProSiebenSat1BaseIE):
    IE_NAME: str
    IE_DESC: str

class ProjectVeritasIE(LazyLoadExtractor):
    IE_NAME: str

class PuhuTVIE(LazyLoadExtractor):
    IE_NAME: str

class PuhuTVSerieIE(LazyLoadExtractor):
    IE_NAME: str

class Puls4IE(ProSiebenSat1BaseIE):
    IE_NAME: str

class PyvideoIE(LazyLoadExtractor):
    IE_NAME: str

class QDanceIE(LazyLoadExtractor):
    IE_NAME: str

class QQPlaylistBaseIE(LazyLoadExtractor):
    IE_NAME: str

class QQMusicAlbumIE(QQPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicBaseIE(LazyLoadExtractor):
    IE_NAME: str

class QQMusicIE(QQMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicPlaylistIE(QQPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicSingerIE(QQMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicToplistIE(QQPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicVideoIE(QQMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class QingTingIE(LazyLoadExtractor):
    IE_NAME: str

class QuantumTVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class QuantumTVIE(QuantumTVBaseIE):
    IE_NAME: str

class QuantumTVLiveIE(QuantumTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class QuantumTVRecordingsIE(QuantumTVBaseIE):
    IE_NAME: str

class QuotedHTMLIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class R7ArticleIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class R7IE(LazyLoadExtractor):
    IE_NAME: str

class RCSBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RCSEmbedsIE(RCSBaseIE):
    IE_NAME: str

class RCSIE(RCSBaseIE):
    IE_NAME: str

class RCSVariousIE(RCSBaseIE):
    IE_NAME: str

class RCTIPlusBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RCTIPlusIE(RCTIPlusBaseIE):
    IE_NAME: str

class RCTIPlusSeriesIE(RCTIPlusBaseIE):
    IE_NAME: str
    age_limit: int
    @classmethod
    def suitable(cls, url): ...

class RCTIPlusTVIE(RCTIPlusBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class RDSIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class RENTVArticleIE(LazyLoadExtractor):
    IE_NAME: str

class RENTVIE(LazyLoadExtractor):
    IE_NAME: str

class RMCDecouverteIE(LazyLoadExtractor):
    IE_NAME: str

class RTBFIE(RedBeeBaseIE):
    IE_NAME: str

class RTDocumentryIE(LazyLoadExtractor):
    IE_NAME: str

class RTDocumentryPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class RTL2IE(LazyLoadExtractor):
    IE_NAME: str

class RTLLuBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RTLLuArticleIE(RTLLuBaseIE):
    IE_NAME: str

class RTLLuLiveIE(RTLLuBaseIE):
    IE_NAME: str

class RTLLuRadioIE(RTLLuBaseIE):
    IE_NAME: str

class RTLLuTeleVODIE(RTLLuBaseIE):
    IE_NAME: str

class RTNewsIE(LazyLoadExtractor):
    IE_NAME: str

class RTPIE(LazyLoadExtractor):
    IE_NAME: str

class RTRFMIE(LazyLoadExtractor):
    IE_NAME: str

class RTVCPlayBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RTVCKalturaIE(RTVCPlayBaseIE):
    IE_NAME: str

class RTVCPlayEmbedIE(RTVCPlayBaseIE):
    IE_NAME: str

class RTVCPlayIE(RTVCPlayBaseIE):
    IE_NAME: str

class RTVEBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RTVEALaCartaIE(RTVEBaseIE):
    IE_NAME: str
    IE_DESC: str

class RTVEAudioIE(RTVEBaseIE):
    IE_NAME: str
    IE_DESC: str

class RTVELiveIE(RTVEBaseIE):
    IE_NAME: str
    IE_DESC: str

class RTVETelevisionIE(LazyLoadExtractor):
    IE_NAME: str

class RTVSIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class RTVSLOIE(LazyLoadExtractor):
    IE_NAME: str

class RTVSLOShowIE(LazyLoadExtractor):
    IE_NAME: str

class RUTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class RadLiveIE(LazyLoadExtractor):
    IE_NAME: str

class RadLiveChannelIE(RadLiveIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class RadLiveSeasonIE(RadLiveIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class RadikoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RadikoIE(RadikoBaseIE):
    IE_NAME: str

class RadikoRadioIE(RadikoBaseIE):
    IE_NAME: str

class Radio1BeIE(VRTBaseIE):
    IE_NAME: str

class RadioCanadaAudioVideoIE(LazyLoadExtractor):
    IE_NAME: str

class RadioCanadaIE(LazyLoadExtractor):
    IE_NAME: str

class RadioComercialIE(LazyLoadExtractor):
    IE_NAME: str

class RadioComercialPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class RadioDeIE(LazyLoadExtractor):
    IE_NAME: str

class RadioFranceIE(LazyLoadExtractor):
    IE_NAME: str

class RadioFranceLiveIE(RadioFranceBaseIE):
    IE_NAME: str

class RadioFrancePlaylistBaseIE(RadioFranceBaseIE):
    IE_NAME: str

class RadioFrancePodcastIE(RadioFrancePlaylistBaseIE):
    IE_NAME: str

class RadioFranceProfileIE(RadioFrancePlaylistBaseIE):
    IE_NAME: str

class RadioFranceProgramScheduleIE(RadioFranceBaseIE):
    IE_NAME: str

class RadioJavanIE(LazyLoadExtractor):
    IE_NAME: str

class RadioKapitalBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RadioKapitalIE(RadioKapitalBaseIE):
    IE_NAME: str

class RadioKapitalShowIE(RadioKapitalBaseIE):
    IE_NAME: str

class RadioRadicaleIE(LazyLoadExtractor):
    IE_NAME: str

class RadioZetPodcastIE(LazyLoadExtractor):
    IE_NAME: str

class RaiBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RaiIE(RaiBaseIE):
    IE_NAME: str

class RaiNewsIE(RaiBaseIE):
    IE_NAME: str

class RaiCulturaIE(RaiNewsIE):
    IE_NAME: str

class RaiPlayIE(RaiBaseIE):
    IE_NAME: str

class RaiPlayLiveIE(RaiPlayIE):
    IE_NAME: str

class RaiPlayPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class RaiPlaySoundIE(RaiBaseIE):
    IE_NAME: str

class RaiPlaySoundLiveIE(RaiPlaySoundIE):
    IE_NAME: str

class RaiPlaySoundPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class RaiSudtirolIE(RaiBaseIE):
    IE_NAME: str

class RayWenderlichCourseIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class RayWenderlichIE(LazyLoadExtractor):
    IE_NAME: str

class RbgTumCourseIE(LazyLoadExtractor):
    IE_NAME: str

class RbgTumIE(LazyLoadExtractor):
    IE_NAME: str

class RbgTumNewCourseIE(LazyLoadExtractor):
    IE_NAME: str

class RedBullIE(LazyLoadExtractor):
    IE_NAME: str

class RedBullTVIE(LazyLoadExtractor):
    IE_NAME: str

class RedBullEmbedIE(RedBullTVIE):
    IE_NAME: str

class RedBullTVRrnContentIE(LazyLoadExtractor):
    IE_NAME: str

class RedCDNLivxIE(LazyLoadExtractor):
    IE_NAME: str

class RedGifsBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RedGifsIE(RedGifsBaseIE):
    IE_NAME: str
    age_limit: int

class RedGifsSearchIE(RedGifsBaseIE):
    IE_NAME: str
    IE_DESC: str

class RedGifsUserIE(RedGifsBaseIE):
    IE_NAME: str
    IE_DESC: str

class RedTubeIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class RedditIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class RestudyIE(LazyLoadExtractor):
    IE_NAME: str

class ReutersIE(LazyLoadExtractor):
    IE_NAME: str

class ReverbNationIE(LazyLoadExtractor):
    IE_NAME: str

class RheinMainTVIE(LazyLoadExtractor):
    IE_NAME: str

class RideHomeIE(LazyLoadExtractor):
    IE_NAME: str

class RinseFMBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RinseFMArtistPlaylistIE(RinseFMBaseIE):
    IE_NAME: str

class RinseFMIE(RinseFMBaseIE):
    IE_NAME: str

class RockstarGamesIE(LazyLoadExtractor):
    IE_NAME: str

class RokfinPlaylistBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RokfinChannelIE(RokfinPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RokfinIE(LazyLoadExtractor):
    IE_NAME: str

class RokfinSearchIE(LazyLoadSearchExtractor):
    IE_NAME: str
    IE_DESC: str
    SEARCH_KEY: str

class RokfinStackIE(RokfinPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RoosterTeethBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RoosterTeethIE(RoosterTeethBaseIE):
    IE_NAME: str

class RoosterTeethSeriesIE(RoosterTeethBaseIE):
    IE_NAME: str

class RottenTomatoesIE(LazyLoadExtractor):
    IE_NAME: str

class RoyaLiveIE(LazyLoadExtractor):
    IE_NAME: str

class RozhlasIE(LazyLoadExtractor):
    IE_NAME: str

class RozhlasVltavaIE(RozhlasBaseIE):
    IE_NAME: str

class RteBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RteIE(RteBaseIE):
    IE_NAME: str
    IE_DESC: str

class RteRadioIE(RteBaseIE):
    IE_NAME: str
    IE_DESC: str

class RtlNlIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class RtmpIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class RudoVideoIE(LazyLoadExtractor):
    IE_NAME: str

class Rule34VideoIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class RumbleChannelIE(LazyLoadExtractor):
    IE_NAME: str

class RumbleEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class RumbleIE(LazyLoadExtractor):
    IE_NAME: str

class RuptlyIE(LazyLoadExtractor):
    IE_NAME: str

class RutubeBaseIE(LazyLoadExtractor):
    IE_NAME: str

class RutubePlaylistBaseIE(RutubeBaseIE):
    IE_NAME: str

class RutubeChannelIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubeEmbedIE(RutubeBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubeIE(RutubeBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubeMovieIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubePersonIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubePlaylistIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubeTagsIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RuutuIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class RuvIE(LazyLoadExtractor):
    IE_NAME: str

class RuvSpilaIE(LazyLoadExtractor):
    IE_NAME: str

class S4CIE(LazyLoadExtractor):
    IE_NAME: str

class S4CSeriesIE(LazyLoadExtractor):
    IE_NAME: str

class SAKTVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class SAKTVIE(SAKTVBaseIE):
    IE_NAME: str

class SAKTVLiveIE(SAKTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class SAKTVRecordingsIE(SAKTVBaseIE):
    IE_NAME: str

class SBSCoKrAllvodProgramIE(LazyLoadExtractor):
    IE_NAME: str

class SBSCoKrIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class SBSCoKrProgramsVodIE(LazyLoadExtractor):
    IE_NAME: str

class SBSIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class SCTEBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SCTECourseIE(SCTEBaseIE):
    IE_NAME: str

class SCTEIE(SCTEBaseIE):
    IE_NAME: str

class SRGSSRIE(LazyLoadExtractor):
    IE_NAME: str

class RTSIE(SRGSSRIE):
    IE_NAME: str
    IE_DESC: str

class SRGSSRPlayIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ARDMediathekBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SRMediathekIE(ARDMediathekBaseIE):
    IE_NAME: str
    IE_DESC: str

class STVPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class SVTBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SVTPageIE(SVTBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class SVTPlayIE(SVTBaseIE):
    IE_NAME: str
    IE_DESC: str

class SVTSeriesIE(SVTBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class SYVDKIE(LazyLoadExtractor):
    IE_NAME: str

class SafariBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SafariApiIE(SafariBaseIE):
    IE_NAME: str

class SafariCourseIE(SafariBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class SafariIE(SafariBaseIE):
    IE_NAME: str
    IE_DESC: str

class SaitosanIE(LazyLoadExtractor):
    IE_NAME: str

class SaltTVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class SaltTVIE(SaltTVBaseIE):
    IE_NAME: str

class SaltTVLiveIE(SaltTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class SaltTVRecordingsIE(SaltTVBaseIE):
    IE_NAME: str

class SampleFocusIE(LazyLoadExtractor):
    IE_NAME: str

class SangiinIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class SangiinInstructionIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class SapoIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class SaucePlusIE(FloatplaneBaseIE):
    IE_NAME: str
    IE_DESC: str

class SchoolTVIE(NPODataMidEmbedIE):
    IE_NAME: str

class ScienceChannelIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class Screen9IE(LazyLoadExtractor):
    IE_NAME: str

class ScreenRecIE(LazyLoadExtractor):
    IE_NAME: str

class ScreencastIE(LazyLoadExtractor):
    IE_NAME: str

class ScreencastOMaticIE(LazyLoadExtractor):
    IE_NAME: str

class ScreencastifyIE(LazyLoadExtractor):
    IE_NAME: str

class ScrippsNetworksIE(LazyLoadExtractor):
    IE_NAME: str

class AWSIE(LazyLoadExtractor):
    IE_NAME: str

class ScrippsNetworksWatchIE(AWSIE):
    IE_NAME: str

class ScrolllerIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class SejmIE(LazyLoadExtractor):
    IE_NAME: str

class SenIE(LazyLoadExtractor):
    IE_NAME: str

class SenalColombiaLiveIE(LazyLoadExtractor):
    IE_NAME: str

class SenateGovIE(LazyLoadExtractor):
    IE_NAME: str

class SenateISVPIE(LazyLoadExtractor):
    IE_NAME: str

class SendtoNewsIE(LazyLoadExtractor):
    IE_NAME: str

class ServusIE(LazyLoadExtractor):
    IE_NAME: str

class SevenPlusIE(BrightcoveNewBaseIE):
    IE_NAME: str

class SexuIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class SeznamZpravyArticleIE(LazyLoadExtractor):
    IE_NAME: str

class SeznamZpravyIE(LazyLoadExtractor):
    IE_NAME: str

class ShahidBaseIE(AWSIE):
    IE_NAME: str

class ShahidIE(ShahidBaseIE):
    IE_NAME: str

class ShahidShowIE(ShahidBaseIE):
    IE_NAME: str

class SharePointIE(LazyLoadExtractor):
    IE_NAME: str

class ShareVideosEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class ShemarooMeIE(LazyLoadExtractor):
    IE_NAME: str

class ShowRoomLiveIE(LazyLoadExtractor):
    IE_NAME: str

class ShugiinItvBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ShugiinItvLiveIE(ShugiinItvBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class ShugiinItvLiveRoomIE(ShugiinItvBaseIE):
    IE_NAME: str
    IE_DESC: str

class ShugiinItvVodIE(ShugiinItvBaseIE):
    IE_NAME: str
    IE_DESC: str

class SibnetEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class SimplecastBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SimplecastEpisodeIE(SimplecastBaseIE):
    IE_NAME: str

class SimplecastIE(SimplecastBaseIE):
    IE_NAME: str

class SimplecastPodcastIE(SimplecastBaseIE):
    IE_NAME: str

class SinaIE(LazyLoadExtractor):
    IE_NAME: str

class SixPlayIE(LazyLoadExtractor):
    IE_NAME: str

class SkebIE(LazyLoadExtractor):
    IE_NAME: str

class SkyItBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SkyItIE(SkyItBaseIE):
    IE_NAME: str

class CieloTVItIE(SkyItIE):
    IE_NAME: str

class SkyItArteIE(SkyItIE):
    IE_NAME: str

class SkyItPlayerIE(SkyItBaseIE):
    IE_NAME: str

class SkyItVideoIE(SkyItBaseIE):
    IE_NAME: str

class SkyItVideoLiveIE(SkyItBaseIE):
    IE_NAME: str

class SkyNewsAUIE(LazyLoadExtractor):
    IE_NAME: str

class SkyNewsArabiaBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SkyNewsArabiaArticleIE(SkyNewsArabiaBaseIE):
    IE_NAME: str

class SkyNewsArabiaIE(SkyNewsArabiaBaseIE):
    IE_NAME: str

class SkyBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SkyNewsIE(SkyBaseIE):
    IE_NAME: str

class SkyNewsStoryIE(SkyBaseIE):
    IE_NAME: str

class SkySportsIE(SkyBaseIE):
    IE_NAME: str

class SkySportsNewsIE(SkyBaseIE):
    IE_NAME: str

class SkylineWebcamsIE(LazyLoadExtractor):
    IE_NAME: str

class SlidesLiveIE(LazyLoadExtractor):
    IE_NAME: str

class SlideshareIE(LazyLoadExtractor):
    IE_NAME: str

class SlutloadIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class SmotrimIE(LazyLoadExtractor):
    IE_NAME: str

class SnapchatSpotlightIE(LazyLoadExtractor):
    IE_NAME: str

class SnotrIE(LazyLoadExtractor):
    IE_NAME: str

class SoftWhiteUnderbellyIE(LazyLoadExtractor):
    IE_NAME: str

class SohuIE(LazyLoadExtractor):
    IE_NAME: str

class SohuVIE(LazyLoadExtractor):
    IE_NAME: str

class SonyLIVIE(LazyLoadExtractor):
    IE_NAME: str

class SonyLIVSeriesIE(LazyLoadExtractor):
    IE_NAME: str

class SoundcloudEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class SoundcloudBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SoundcloudIE(SoundcloudBaseIE):
    IE_NAME: str

class SoundcloudPlaylistBaseIE(SoundcloudBaseIE):
    IE_NAME: str

class SoundcloudPlaylistIE(SoundcloudPlaylistBaseIE):
    IE_NAME: str

class SoundcloudPagedPlaylistBaseIE(SoundcloudBaseIE):
    IE_NAME: str

class SoundcloudRelatedIE(SoundcloudPagedPlaylistBaseIE):
    IE_NAME: str

class SoundcloudSearchIE(SoundcloudBaseIE, LazyLoadSearchExtractor):
    IE_NAME: str
    IE_DESC: str
    SEARCH_KEY: str

class SoundcloudSetIE(SoundcloudPlaylistBaseIE):
    IE_NAME: str

class SoundcloudTrackStationIE(SoundcloudPagedPlaylistBaseIE):
    IE_NAME: str

class SoundcloudUserIE(SoundcloudPagedPlaylistBaseIE):
    IE_NAME: str

class SoundcloudUserPermalinkIE(SoundcloudPagedPlaylistBaseIE):
    IE_NAME: str

class SoundgasmIE(LazyLoadExtractor):
    IE_NAME: str

class SoundgasmProfileIE(LazyLoadExtractor):
    IE_NAME: str

class SouthParkIE(MTVServicesInfoExtractor):
    IE_NAME: str

class SouthParkDeIE(SouthParkIE):
    IE_NAME: str

class SouthParkDkIE(SouthParkIE):
    IE_NAME: str

class SouthParkEsIE(SouthParkIE):
    IE_NAME: str

class SouthParkLatIE(SouthParkIE):
    IE_NAME: str

class SouthParkNlIE(SouthParkIE):
    IE_NAME: str

class SovietsClosetBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SovietsClosetIE(SovietsClosetBaseIE):
    IE_NAME: str

class SovietsClosetPlaylistIE(SovietsClosetBaseIE):
    IE_NAME: str

class SpankBangIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class SpankBangPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class SpiegelIE(LazyLoadExtractor):
    IE_NAME: str

class Sport5IE(LazyLoadExtractor):
    IE_NAME: str

class SportBoxIE(LazyLoadExtractor):
    IE_NAME: str

class SportDeutschlandIE(LazyLoadExtractor):
    IE_NAME: str

class SpotifyBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SpotifyIE(SpotifyBaseIE):
    IE_NAME: str
    IE_DESC: str

class SpotifyShowIE(SpotifyBaseIE):
    IE_NAME: str
    IE_DESC: str

class SpreakerIE(LazyLoadExtractor):
    IE_NAME: str

class SpreakerShowIE(LazyLoadExtractor):
    IE_NAME: str

class SpringboardPlatformIE(LazyLoadExtractor):
    IE_NAME: str

class SproutVideoIE(LazyLoadExtractor):
    IE_NAME: str

class WrestleUniverseBaseIE(LazyLoadExtractor):
    IE_NAME: str

class StacommuBaseIE(WrestleUniverseBaseIE):
    IE_NAME: str

class StacommuLiveIE(StacommuBaseIE):
    IE_NAME: str

class StacommuVODIE(StacommuBaseIE):
    IE_NAME: str

class StagePlusVODConcertIE(LazyLoadExtractor):
    IE_NAME: str

class StanfordOpenClassroomIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class StarTVIE(LazyLoadExtractor):
    IE_NAME: str

class StarTrekIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class SteamCommunityBroadcastIE(LazyLoadExtractor):
    IE_NAME: str

class SteamIE(LazyLoadExtractor):
    IE_NAME: str

class StitcherBaseIE(LazyLoadExtractor):
    IE_NAME: str

class StitcherIE(StitcherBaseIE):
    IE_NAME: str

class StitcherShowIE(StitcherBaseIE):
    IE_NAME: str

class StoryFireBaseIE(LazyLoadExtractor):
    IE_NAME: str

class StoryFireIE(StoryFireBaseIE):
    IE_NAME: str

class StoryFireSeriesIE(StoryFireBaseIE):
    IE_NAME: str

class StoryFireUserIE(StoryFireBaseIE):
    IE_NAME: str

class StreaksIE(StreaksBaseIE):
    IE_NAME: str

class StreamCZIE(LazyLoadExtractor):
    IE_NAME: str

class StreamableIE(LazyLoadExtractor):
    IE_NAME: str

class StreetVoiceIE(LazyLoadExtractor):
    IE_NAME: str

class StretchInternetIE(LazyLoadExtractor):
    IE_NAME: str

class StripchatIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class SubsplashBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SubsplashIE(SubsplashBaseIE):
    IE_NAME: str

class SubsplashPlaylistIE(SubsplashBaseIE):
    IE_NAME: str

class SubstackIE(LazyLoadExtractor):
    IE_NAME: str

class SunPornoIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class SverigesRadioBaseIE(LazyLoadExtractor):
    IE_NAME: str

class SverigesRadioEpisodeIE(SverigesRadioBaseIE):
    IE_NAME: str

class SverigesRadioPublicationIE(SverigesRadioBaseIE):
    IE_NAME: str

class SwearnetEpisodeIE(VidyardBaseIE):
    IE_NAME: str

class SyfyIE(NBCUniversalBaseIE):
    IE_NAME: str
    age_limit: int

class SztvHuIE(LazyLoadExtractor):
    IE_NAME: str

class TBSIE(TurnerBaseIE):
    IE_NAME: str

class TBSJPEpisodeIE(LazyLoadExtractor):
    IE_NAME: str

class TBSJPPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class TBSJPProgramIE(LazyLoadExtractor):
    IE_NAME: str

class TF1IE(LazyLoadExtractor):
    IE_NAME: str

class TFOIE(LazyLoadExtractor):
    IE_NAME: str

class TLCIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class TMZIE(LazyLoadExtractor):
    IE_NAME: str

class TNAFlixIE(TNAEMPFlixBaseIE):
    IE_NAME: str
    age_limit: int

class TNAFlixNetworkEmbedIE(TNAFlixNetworkBaseIE):
    IE_NAME: str
    age_limit: int

class TOnlineIE(LazyLoadExtractor):
    IE_NAME: str

class TV24UAVideoIE(LazyLoadExtractor):
    IE_NAME: str

class TV2ArticleIE(LazyLoadExtractor):
    IE_NAME: str

class TV2DKBornholmPlayIE(LazyLoadExtractor):
    IE_NAME: str

class TV2DKIE(LazyLoadExtractor):
    IE_NAME: str

class TV2HuIE(LazyLoadExtractor):
    IE_NAME: str

class TV2HuSeriesIE(LazyLoadExtractor):
    IE_NAME: str

class TV2IE(LazyLoadExtractor):
    IE_NAME: str

class TV4IE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class TV5MondePlusIE(LazyLoadExtractor):
    IE_NAME: str

class TV5UnisBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TV5UnisIE(TV5UnisBaseIE):
    IE_NAME: str
    age_limit: int

class TV5UnisVideoIE(TV5UnisBaseIE):
    IE_NAME: str

class TV8ItIE(SkyItVideoIE):
    IE_NAME: str

class TV8ItLiveIE(SkyItBaseIE):
    IE_NAME: str
    IE_DESC: str

class TV8ItPlaylistIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class TVAIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class TVANouvellesArticleIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class TVANouvellesIE(LazyLoadExtractor):
    IE_NAME: str

class TVCArticleIE(LazyLoadExtractor):
    IE_NAME: str

class TVCIE(LazyLoadExtractor):
    IE_NAME: str

class TVIPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class TVLandIE(MTVServicesInfoExtractor):
    IE_NAME: str

class TVN24IE(LazyLoadExtractor):
    IE_NAME: str

class TVNoeIE(LazyLoadExtractor):
    IE_NAME: str

class TVOpenGrBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TVOpenGrEmbedIE(TVOpenGrBaseIE):
    IE_NAME: str
    IE_DESC: str

class TVOpenGrWatchIE(TVOpenGrBaseIE):
    IE_NAME: str
    IE_DESC: str

class TVPEmbedIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class TVPIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class TVPStreamIE(LazyLoadExtractor):
    IE_NAME: str

class TVPVODBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TVPVODSeriesIE(TVPVODBaseIE):
    IE_NAME: str
    age_limit: int

class TVPVODVideoIE(TVPVODBaseIE):
    IE_NAME: str
    age_limit: int

class TVPlayHomeIE(LazyLoadExtractor):
    IE_NAME: str

class TVPlayIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class TVPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class TVerIE(StreaksBaseIE):
    IE_NAME: str

class TagesschauIE(LazyLoadExtractor):
    IE_NAME: str

class TapTapBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TapTapAppIE(TapTapBaseIE):
    IE_NAME: str

class TapTapIntlBaseIE(TapTapBaseIE):
    IE_NAME: str

class TapTapAppIntlIE(TapTapIntlBaseIE):
    IE_NAME: str

class TapTapMomentIE(TapTapBaseIE):
    IE_NAME: str

class TapTapPostIntlIE(TapTapIntlBaseIE):
    IE_NAME: str

class TassIE(LazyLoadExtractor):
    IE_NAME: str

class TeachableBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TeachableCourseIE(TeachableBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class TeachableIE(TeachableBaseIE):
    IE_NAME: str

class TeacherTubeIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class TeacherTubeUserIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class TeachingChannelIE(LazyLoadExtractor):
    IE_NAME: str

class TeamTreeHouseIE(LazyLoadExtractor):
    IE_NAME: str

class TeamcocoIE(TeamcocoBaseIE):
    IE_NAME: str

class TechTVMITIE(LazyLoadExtractor):
    IE_NAME: str

class TedEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class TedBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TedPlaylistIE(TedBaseIE):
    IE_NAME: str

class TedSeriesIE(TedBaseIE):
    IE_NAME: str

class TedTalkIE(TedBaseIE):
    IE_NAME: str

class Tele13IE(LazyLoadExtractor):
    IE_NAME: str

class Tele5IE(DiscoveryPlusBaseIE):
    IE_NAME: str

class TeleBruxellesIE(LazyLoadExtractor):
    IE_NAME: str

class TeleMBIE(LazyLoadExtractor):
    IE_NAME: str

class TeleQuebecEmissionIE(LazyLoadExtractor):
    IE_NAME: str

class TeleQuebecBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TeleQuebecIE(TeleQuebecBaseIE):
    IE_NAME: str

class TeleQuebecLiveIE(TeleQuebecBaseIE):
    IE_NAME: str

class TeleQuebecSquatIE(LazyLoadExtractor):
    IE_NAME: str

class TeleQuebecVideoIE(TeleQuebecBaseIE):
    IE_NAME: str

class TeleTaskIE(LazyLoadExtractor):
    IE_NAME: str

class TelecaribePlayIE(LazyLoadExtractor):
    IE_NAME: str

class TelecincoIE(TelecincoBaseIE):
    IE_NAME: str
    IE_DESC: str

class TelegraafIE(LazyLoadExtractor):
    IE_NAME: str

class TelegramEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class TelemundoIE(LazyLoadExtractor):
    IE_NAME: str

class TelewebionIE(LazyLoadExtractor):
    IE_NAME: str

class TempoIE(LazyLoadExtractor):
    IE_NAME: str

class TenPlayIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class TenPlaySeasonIE(LazyLoadExtractor):
    IE_NAME: str

class TennisTVIE(LazyLoadExtractor):
    IE_NAME: str

class TestURLIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class TheGuardianPodcastIE(LazyLoadExtractor):
    IE_NAME: str

class TheGuardianPodcastPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class TheHoleTvIE(LazyLoadExtractor):
    IE_NAME: str

class TheInterceptIE(LazyLoadExtractor):
    IE_NAME: str

class ThePlatformFeedIE(ThePlatformBaseIE):
    IE_NAME: str

class CBSBaseIE(ThePlatformFeedIE):
    IE_NAME: str

class CBSIE(CBSBaseIE):
    IE_NAME: str

class CorusIE(ThePlatformFeedIE):
    IE_NAME: str

class ParamountPlusIE(CBSBaseIE):
    IE_NAME: str

class ThePlatformIE(ThePlatformBaseIE):
    IE_NAME: str

class AENetworksBaseIE(ThePlatformIE):
    IE_NAME: str

class AENetworksListBaseIE(AENetworksBaseIE):
    IE_NAME: str

class AENetworksCollectionIE(AENetworksListBaseIE):
    IE_NAME: str

class AENetworksIE(AENetworksBaseIE):
    IE_NAME: str
    IE_DESC: str

class AENetworksShowIE(AENetworksListBaseIE):
    IE_NAME: str

class BiographyIE(AENetworksBaseIE):
    IE_NAME: str

class HistoryPlayerIE(AENetworksBaseIE):
    IE_NAME: str

class HistoryTopicIE(AENetworksBaseIE):
    IE_NAME: str
    IE_DESC: str

class NBCNewsIE(ThePlatformIE):
    IE_NAME: str

class TheStarIE(LazyLoadExtractor):
    IE_NAME: str

class TheSunIE(LazyLoadExtractor):
    IE_NAME: str

class TheWeatherChannelIE(ThePlatformIE):
    IE_NAME: str

class TheaterComplexTownBaseIE(StacommuBaseIE):
    IE_NAME: str

class TheaterComplexTownPPVIE(TheaterComplexTownBaseIE):
    IE_NAME: str

class TheaterComplexTownVODIE(TheaterComplexTownBaseIE):
    IE_NAME: str

class ThisAmericanLifeIE(LazyLoadExtractor):
    IE_NAME: str

class ThisOldHouseIE(LazyLoadExtractor):
    IE_NAME: str

class ThisVidIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class ThisVidPlaylistBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ThisVidMemberIE(ThisVidPlaylistBaseIE):
    IE_NAME: str

class ThisVidPlaylistIE(ThisVidPlaylistBaseIE):
    IE_NAME: str
    age_limit: int

class ThreeQSDNIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ThreeSpeakIE(LazyLoadExtractor):
    IE_NAME: str

class ThreeSpeakUserIE(LazyLoadExtractor):
    IE_NAME: str

class TikTokCollectionIE(TikTokBaseIE):
    IE_NAME: str

class TikTokBaseListIE(TikTokBaseIE):
    IE_NAME: str

class TikTokEffectIE(TikTokBaseListIE):
    IE_NAME: str

class TikTokIE(TikTokBaseIE):
    IE_NAME: str

class TikTokLiveIE(TikTokBaseIE):
    IE_NAME: str

class TikTokSoundIE(TikTokBaseListIE):
    IE_NAME: str

class TikTokTagIE(TikTokBaseListIE):
    IE_NAME: str

class TikTokUserIE(TikTokBaseIE):
    IE_NAME: str

class TikTokVMIE(LazyLoadExtractor):
    IE_NAME: str

class ToggleIE(LazyLoadExtractor):
    IE_NAME: str

class ToggoIE(LazyLoadExtractor):
    IE_NAME: str

class TokFMAuditionIE(LazyLoadExtractor):
    IE_NAME: str

class TokFMPodcastIE(LazyLoadExtractor):
    IE_NAME: str

class ToonGogglesIE(LazyLoadExtractor):
    IE_NAME: str

class TouTvIE(RadioCanadaIE):
    IE_NAME: str

class ToutiaoIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ToypicsIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class ToypicsUserIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class TrailerAddictIE(LazyLoadExtractor):
    IE_NAME: str

class TravelChannelIE(DiscoveryPlusBaseIE):
    IE_NAME: str

class TrillerBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TrillerIE(TrillerBaseIE):
    IE_NAME: str

class TrillerShortIE(LazyLoadExtractor):
    IE_NAME: str

class TrillerUserIE(TrillerBaseIE):
    IE_NAME: str

class TrovoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TrovoChannelBaseIE(TrovoBaseIE):
    IE_NAME: str

class TrovoChannelClipIE(TrovoChannelBaseIE):
    IE_NAME: str
    IE_DESC: str

class TrovoChannelVodIE(TrovoChannelBaseIE):
    IE_NAME: str
    IE_DESC: str

class TrovoIE(TrovoBaseIE):
    IE_NAME: str

class TrovoVodIE(TrovoBaseIE):
    IE_NAME: str

class TrtCocukVideoIE(LazyLoadExtractor):
    IE_NAME: str

class TrtWorldIE(LazyLoadExtractor):
    IE_NAME: str

class TruNewsIE(LazyLoadExtractor):
    IE_NAME: str

class TruTVIE(TurnerBaseIE):
    IE_NAME: str

class TrueIDIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class TruthIE(LazyLoadExtractor):
    IE_NAME: str

class Tube8IE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class TubeTuGrazBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TubeTuGrazIE(TubeTuGrazBaseIE):
    IE_NAME: str
    IE_DESC: str

class TubeTuGrazSeriesIE(TubeTuGrazBaseIE):
    IE_NAME: str

class TubiTvIE(LazyLoadExtractor):
    IE_NAME: str

class TubiTvShowIE(LazyLoadExtractor):
    IE_NAME: str

class TumblrIE(LazyLoadExtractor):
    IE_NAME: str

class TuneInBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TuneInPodcastEpisodeIE(TuneInBaseIE):
    IE_NAME: str

class TuneInPodcastIE(TuneInBaseIE):
    IE_NAME: str

class TuneInShortenerIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class TuneInStationIE(TuneInBaseIE):
    IE_NAME: str

class TvigleIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str
    age_limit: int

class TvwIE(LazyLoadExtractor):
    IE_NAME: str

class TvwTvChannelsIE(LazyLoadExtractor):
    IE_NAME: str

class TweakersIE(LazyLoadExtractor):
    IE_NAME: str

class TwentyFourSevenSportsIE(CBSSportsBaseIE):
    IE_NAME: str

class TwentyMinutenIE(LazyLoadExtractor):
    IE_NAME: str

class TwentyThreeVideoIE(LazyLoadExtractor):
    IE_NAME: str

class TwitCastingIE(LazyLoadExtractor):
    IE_NAME: str

class TwitCastingLiveIE(LazyLoadExtractor):
    IE_NAME: str

class TwitCastingUserIE(LazyLoadExtractor):
    IE_NAME: str

class TwitchBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TwitchClipsIE(TwitchBaseIE):
    IE_NAME: str

class TwitchCollectionIE(TwitchBaseIE):
    IE_NAME: str

class TwitchPlaylistBaseIE(TwitchBaseIE):
    IE_NAME: str

class TwitchVideosBaseIE(TwitchPlaylistBaseIE):
    IE_NAME: str

class TwitchStreamIE(TwitchVideosBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class TwitchVideosClipsIE(TwitchPlaylistBaseIE):
    IE_NAME: str

class TwitchVideosCollectionsIE(TwitchPlaylistBaseIE):
    IE_NAME: str

class TwitchVideosIE(TwitchVideosBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class TwitchVodIE(TwitchBaseIE):
    IE_NAME: str

class TwitterBaseIE(LazyLoadExtractor):
    IE_NAME: str

class TwitterAmplifyIE(TwitterBaseIE):
    IE_NAME: str

class TwitterBroadcastIE(TwitterBaseIE, PeriscopeBaseIE):
    IE_NAME: str

class TwitterCardIE(LazyLoadExtractor):
    IE_NAME: str

class TwitterIE(TwitterBaseIE):
    IE_NAME: str
    age_limit: int

class TwitterShortenerIE(TwitterBaseIE):
    IE_NAME: str

class TwitterSpacesIE(TwitterBaseIE):
    IE_NAME: str

class TxxxIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class UDNEmbedIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class ImgGamingBaseIE(LazyLoadExtractor):
    IE_NAME: str

class UFCArabiaIE(ImgGamingBaseIE):
    IE_NAME: str

class UFCTVIE(ImgGamingBaseIE):
    IE_NAME: str

class UKTVPlayIE(LazyLoadExtractor):
    IE_NAME: str

class UMGDeIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class UOLIE(LazyLoadExtractor):
    IE_NAME: str

class URPlayIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class USANetworkIE(NBCIE):
    IE_NAME: str

class USATodayIE(LazyLoadExtractor):
    IE_NAME: str

class UdemyIE(LazyLoadExtractor):
    IE_NAME: str

class UdemyCourseIE(UdemyIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class UkColumnIE(LazyLoadExtractor):
    IE_NAME: str

class UlizaPlayerIE(LazyLoadExtractor):
    IE_NAME: str

class UlizaPortalIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class UnicodeBOMIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class UnistraIE(LazyLoadExtractor):
    IE_NAME: str

class UnityIE(LazyLoadExtractor):
    IE_NAME: str

class UplynkBaseIE(LazyLoadExtractor):
    IE_NAME: str

class UplynkIE(UplynkBaseIE):
    IE_NAME: str

class UplynkPreplayIE(UplynkBaseIE):
    IE_NAME: str

class UrortIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class UstreamChannelIE(LazyLoadExtractor):
    IE_NAME: str

class UstreamIE(LazyLoadExtractor):
    IE_NAME: str

class UstudioEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class UstudioIE(LazyLoadExtractor):
    IE_NAME: str

class UtreonIE(LazyLoadExtractor):
    IE_NAME: str

class VH1IE(MTVServicesInfoExtractor):
    IE_NAME: str

class VimeoBaseInfoExtractor(LazyLoadExtractor):
    IE_NAME: str

class VHXEmbedIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VKBaseIE(LazyLoadExtractor):
    IE_NAME: str

class VKIE(VKBaseIE):
    IE_NAME: str
    IE_DESC: str

class VKPlayBaseIE(LazyLoadExtractor):
    IE_NAME: str

class VKPlayIE(VKPlayBaseIE):
    IE_NAME: str

class VKPlayLiveIE(VKPlayBaseIE):
    IE_NAME: str

class VKUserVideosIE(VKBaseIE):
    IE_NAME: str
    IE_DESC: str

class VKWallPostIE(VKBaseIE):
    IE_NAME: str

class VODPlIE(OnetBaseIE):
    IE_NAME: str

class VODPlatformIE(LazyLoadExtractor):
    IE_NAME: str

class VPROIE(NPOPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class VQQBaseIE(TencentBaseIE):
    IE_NAME: str

class VQQSeriesIE(VQQBaseIE):
    IE_NAME: str

class VQQVideoIE(VQQBaseIE):
    IE_NAME: str

class VRTIE(VRTBaseIE):
    IE_NAME: str
    IE_DESC: str

class VTMIE(LazyLoadExtractor):
    IE_NAME: str

class VTVGoIE(LazyLoadExtractor):
    IE_NAME: str

class VTVIE(LazyLoadExtractor):
    IE_NAME: str

class VTXTVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class VTXTVIE(VTXTVBaseIE):
    IE_NAME: str

class VTXTVLiveIE(VTXTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class VTXTVRecordingsIE(VTXTVBaseIE):
    IE_NAME: str

class VVVVIDIE(LazyLoadExtractor):
    IE_NAME: str

class VVVVIDShowIE(VVVVIDIE):
    IE_NAME: str

class Varzesh3IE(LazyLoadExtractor):
    IE_NAME: str

class Vbox7IE(LazyLoadExtractor):
    IE_NAME: str

class VeoIE(LazyLoadExtractor):
    IE_NAME: str

class VestiIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class VevoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class VevoIE(VevoBaseIE):
    IE_NAME: str
    age_limit: int

class VevoPlaylistIE(VevoBaseIE):
    IE_NAME: str

class ViMPPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class ViceBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ViceArticleIE(ViceBaseIE):
    IE_NAME: str
    age_limit: int

class ViceIE(ViceBaseIE, AdobePassIE):
    IE_NAME: str
    age_limit: int

class ViceShowIE(ViceBaseIE):
    IE_NAME: str

class VidLiiIE(LazyLoadExtractor):
    IE_NAME: str

class ViddlerIE(LazyLoadExtractor):
    IE_NAME: str

class VideaIE(LazyLoadExtractor):
    IE_NAME: str

class VideoDetectiveIE(LazyLoadExtractor):
    IE_NAME: str

class VideoKenBaseIE(LazyLoadExtractor):
    IE_NAME: str

class VideoKenCategoryIE(VideoKenBaseIE):
    IE_NAME: str

class VideoKenIE(VideoKenBaseIE):
    IE_NAME: str

class VideoKenPlayerIE(VideoKenBaseIE):
    IE_NAME: str

class VideoKenPlaylistIE(VideoKenBaseIE):
    IE_NAME: str

class VideoKenTopicIE(VideoKenBaseIE):
    IE_NAME: str

class VideoPressIE(LazyLoadExtractor):
    IE_NAME: str

class VideocampusSachsenIE(LazyLoadExtractor):
    IE_NAME: str

class VideofyMeIE(LazyLoadExtractor):
    IE_NAME: str

class VideomoreIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class VideomoreBaseIE(LazyLoadExtractor):
    IE_NAME: str

class VideomoreSeasonIE(VideomoreBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class VideomoreVideoIE(VideomoreBaseIE):
    IE_NAME: str
    age_limit: int
    @classmethod
    def suitable(cls, url): ...

class VidflexIE(LazyLoadExtractor):
    IE_NAME: str

class VidioBaseIE(LazyLoadExtractor):
    IE_NAME: str

class VidioIE(VidioBaseIE):
    IE_NAME: str

class VidioLiveIE(VidioBaseIE):
    IE_NAME: str

class VidioPremierIE(VidioBaseIE):
    IE_NAME: str

class VidlyIE(LazyLoadExtractor):
    IE_NAME: str

class VidsIoIE(LazyLoadExtractor):
    IE_NAME: str

class VidyardIE(VidyardBaseIE):
    IE_NAME: str

class ViewLiftBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ViewLiftEmbedIE(ViewLiftBaseIE):
    IE_NAME: str

class ViewLiftIE(ViewLiftBaseIE):
    IE_NAME: str
    age_limit: int
    @classmethod
    def suitable(cls, url): ...

class ViewSourceIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: bool

class ViideaIE(LazyLoadExtractor):
    IE_NAME: str

class VimeoAlbumIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoChannelIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoEventIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoGroupsIE(VimeoChannelIE):
    IE_NAME: str

class VimeoIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoLikesIE(VimeoChannelIE):
    IE_NAME: str
    IE_DESC: str

class VimeoOndemandIE(VimeoIE):
    IE_NAME: str

class VimeoProIE(VimeoBaseInfoExtractor):
    IE_NAME: str

class VimeoReviewIE(VimeoBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class VimeoUserIE(VimeoChannelIE):
    IE_NAME: str

class VimeoWatchLaterIE(VimeoChannelIE):
    IE_NAME: str
    IE_DESC: str

class VimmIE(LazyLoadExtractor):
    IE_NAME: str

class VimmRecordingIE(LazyLoadExtractor):
    IE_NAME: str

class ViouslyIE(LazyLoadExtractor):
    IE_NAME: str

class ViqeoIE(LazyLoadExtractor):
    IE_NAME: str

class ViuBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ViuIE(ViuBaseIE):
    IE_NAME: str

class ViuOTTIE(LazyLoadExtractor):
    IE_NAME: str

class ViuOTTIndonesiaBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ViuOTTIndonesiaIE(ViuOTTIndonesiaBaseIE):
    IE_NAME: str
    age_limit: int

class ViuPlaylistIE(ViuBaseIE):
    IE_NAME: str

class VocarooIE(LazyLoadExtractor):
    IE_NAME: str

class VoicyBaseIE(LazyLoadExtractor):
    IE_NAME: str

class VoicyChannelIE(VoicyBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class VoicyIE(VoicyBaseIE):
    IE_NAME: str

class VolejTVIE(LazyLoadExtractor):
    IE_NAME: str

class VoxMediaIE(LazyLoadExtractor):
    IE_NAME: str

class VoxMediaVolumeIE(LazyLoadExtractor):
    IE_NAME: str

class VrSquarePlaylistBaseIE(LazyLoadExtractor):
    IE_NAME: str

class VrSquareChannelIE(VrSquarePlaylistBaseIE):
    IE_NAME: str

class VrSquareIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class VrSquareSearchIE(VrSquarePlaylistBaseIE):
    IE_NAME: str

class VrSquareSectionIE(VrSquarePlaylistBaseIE):
    IE_NAME: str

class VrtNUIE(VRTBaseIE):
    IE_NAME: str
    IE_DESC: str

class VuClipIE(LazyLoadExtractor):
    IE_NAME: str

class WDRElefantIE(LazyLoadExtractor):
    IE_NAME: str

class WDRIE(LazyLoadExtractor):
    IE_NAME: str

class WDRMobileIE(LazyLoadExtractor):
    IE_NAME: str

class WDRPageIE(WDRIE):
    IE_NAME: str

class WNLIE(NPOPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class WPPilotBaseIE(LazyLoadExtractor):
    IE_NAME: str

class WPPilotChannelsIE(WPPilotBaseIE):
    IE_NAME: str

class WPPilotIE(WPPilotBaseIE):
    IE_NAME: str

class WSJArticleIE(LazyLoadExtractor):
    IE_NAME: str

class WSJIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class WWEBaseIE(LazyLoadExtractor):
    IE_NAME: str

class WWEIE(WWEBaseIE):
    IE_NAME: str

class WallaIE(LazyLoadExtractor):
    IE_NAME: str

class WalyTVBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class WalyTVIE(WalyTVBaseIE):
    IE_NAME: str

class WalyTVLiveIE(WalyTVBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class WalyTVRecordingsIE(WalyTVBaseIE):
    IE_NAME: str

class WashingtonPostArticleIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class WashingtonPostIE(LazyLoadExtractor):
    IE_NAME: str

class WatIE(LazyLoadExtractor):
    IE_NAME: str

class WatchESPNIE(AdobePassIE):
    IE_NAME: str

class WeTvEpisodeIE(WeTvBaseIE):
    IE_NAME: str

class WeTvSeriesIE(WeTvBaseIE):
    IE_NAME: str

class WeVidiIE(LazyLoadExtractor):
    IE_NAME: str

class WebOfStoriesIE(LazyLoadExtractor):
    IE_NAME: str

class WebOfStoriesPlaylistIE(LazyLoadExtractor):
    IE_NAME: str

class WebcameraplIE(LazyLoadExtractor):
    IE_NAME: str

class WebcasterFeedIE(LazyLoadExtractor):
    IE_NAME: str

class WebcasterIE(LazyLoadExtractor):
    IE_NAME: str

class WeiboBaseIE(LazyLoadExtractor):
    IE_NAME: str

class WeiboIE(WeiboBaseIE):
    IE_NAME: str

class WeiboUserIE(WeiboBaseIE):
    IE_NAME: str

class WeiboVideoIE(WeiboBaseIE):
    IE_NAME: str

class WeiqiTVIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class WeverseBaseIE(LazyLoadExtractor):
    IE_NAME: str

class WeverseIE(WeverseBaseIE):
    IE_NAME: str

class WeverseLiveIE(WeverseBaseIE):
    IE_NAME: str

class WeverseTabBaseIE(WeverseBaseIE):
    IE_NAME: str

class WeverseLiveTabIE(WeverseTabBaseIE):
    IE_NAME: str

class WeverseMediaIE(WeverseBaseIE):
    IE_NAME: str

class WeverseMediaTabIE(WeverseTabBaseIE):
    IE_NAME: str

class WeverseMomentIE(WeverseBaseIE):
    IE_NAME: str

class WeyyakIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class WhoWatchIE(LazyLoadExtractor):
    IE_NAME: str

class WhypIE(LazyLoadExtractor):
    IE_NAME: str

class WikimediaIE(LazyLoadExtractor):
    IE_NAME: str

class WimTVIE(LazyLoadExtractor):
    IE_NAME: str

class WimbledonIE(LazyLoadExtractor):
    IE_NAME: str

class WinSportsVideoIE(MediaStreamBaseIE):
    IE_NAME: str

class WistiaBaseIE(LazyLoadExtractor):
    IE_NAME: str

class WistiaChannelIE(WistiaBaseIE):
    IE_NAME: str

class WistiaIE(WistiaBaseIE):
    IE_NAME: str

class WistiaPlaylistIE(WistiaBaseIE):
    IE_NAME: str

class WordpressMiniAudioPlayerEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class WordpressPlaylistEmbedIE(LazyLoadExtractor):
    IE_NAME: str

class WorldStarHipHopIE(LazyLoadExtractor):
    IE_NAME: str

class WrestleUniversePPVIE(WrestleUniverseBaseIE):
    IE_NAME: str

class WrestleUniverseVODIE(WrestleUniverseBaseIE):
    IE_NAME: str

class WyborczaPodcastIE(LazyLoadExtractor):
    IE_NAME: str

class WyborczaVideoIE(LazyLoadExtractor):
    IE_NAME: str

class WykopBaseIE(LazyLoadExtractor):
    IE_NAME: str

class WykopDigCommentIE(WykopBaseIE):
    IE_NAME: str

class WykopDigIE(WykopBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class WykopPostCommentIE(WykopBaseIE):
    IE_NAME: str

class WykopPostIE(WykopBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class XHamsterEmbedIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class XHamsterIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class XHamsterUserIE(LazyLoadExtractor):
    IE_NAME: str

class XMinusIE(LazyLoadExtractor):
    IE_NAME: str

class XNXXIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class XVideosIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class XVideosQuickiesIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class XXXYMoviesIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class XanimuIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class XboxClipsIE(LazyLoadExtractor):
    IE_NAME: str

class XiaoHongShuIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class XimalayaBaseIE(LazyLoadExtractor):
    IE_NAME: str

class XimalayaAlbumIE(XimalayaBaseIE):
    IE_NAME: str
    IE_DESC: str

class XimalayaIE(XimalayaBaseIE):
    IE_NAME: str
    IE_DESC: str

class XinpianchangIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class XstreamIE(LazyLoadExtractor):
    IE_NAME: str

class VGTVIE(XstreamIE):
    IE_NAME: str
    IE_DESC: str

class YahooIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class AolIE(YahooIE):
    IE_NAME: str
    IE_DESC: str

class YahooJapanNewsIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class YahooSearchIE(LazyLoadSearchExtractor):
    IE_NAME: str
    IE_DESC: str
    SEARCH_KEY: str

class YandexDiskIE(LazyLoadExtractor):
    IE_NAME: str

class YandexMusicBaseIE(LazyLoadExtractor):
    IE_NAME: str

class YandexMusicPlaylistBaseIE(YandexMusicBaseIE):
    IE_NAME: str

class YandexMusicAlbumIE(YandexMusicPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class YandexMusicArtistBaseIE(YandexMusicPlaylistBaseIE):
    IE_NAME: str

class YandexMusicArtistAlbumsIE(YandexMusicArtistBaseIE):
    IE_NAME: str
    IE_DESC: str

class YandexMusicArtistTracksIE(YandexMusicArtistBaseIE):
    IE_NAME: str
    IE_DESC: str

class YandexMusicPlaylistIE(YandexMusicPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class YandexMusicTrackIE(YandexMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class YandexVideoIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class YandexVideoPreviewIE(LazyLoadExtractor):
    IE_NAME: str

class YapFilesIE(LazyLoadExtractor):
    IE_NAME: str

class YappyIE(LazyLoadExtractor):
    IE_NAME: str

class YappyProfileIE(LazyLoadExtractor):
    IE_NAME: str

class YleAreenaIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class YouJizzIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class YouNowChannelIE(LazyLoadExtractor):
    IE_NAME: str

class YouNowLiveIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class YouNowMomentIE(LazyLoadExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class YouPornListBaseIE(LazyLoadExtractor):
    IE_NAME: str

class YouPornCategoryIE(YouPornListBaseIE):
    IE_NAME: str
    IE_DESC: str

class YouPornChannelIE(YouPornListBaseIE):
    IE_NAME: str
    IE_DESC: str

class YouPornCollectionIE(YouPornListBaseIE):
    IE_NAME: str
    IE_DESC: str

class YouPornIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class YouPornStarIE(YouPornListBaseIE):
    IE_NAME: str
    IE_DESC: str

class YouPornTagIE(YouPornListBaseIE):
    IE_NAME: str
    IE_DESC: str

class YouPornVideosIE(YouPornListBaseIE):
    IE_NAME: str
    IE_DESC: str

class YoukuIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class YoukuShowIE(LazyLoadExtractor):
    IE_NAME: str

class YoutubeBaseInfoExtractor(LazyLoadExtractor):
    IE_NAME: str

class YoutubeTabBaseInfoExtractor(YoutubeBaseInfoExtractor):
    IE_NAME: str

class YoutubeClipIE(YoutubeTabBaseInfoExtractor):
    IE_NAME: str

class YoutubeConsentRedirectIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: bool

class YoutubeFavouritesIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeFeedsInfoExtractor(YoutubeBaseInfoExtractor):
    IE_NAME: str

class YoutubeHistoryIE(YoutubeFeedsInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str
    age_limit: int
    @classmethod
    def suitable(cls, url): ...

class YoutubeLivestreamEmbedIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeMusicSearchURLIE(YoutubeTabBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeNotificationsIE(YoutubeTabBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubePlaylistIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class YoutubeRecommendedIE(YoutubeFeedsInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeSearchDateIE(YoutubeTabBaseInfoExtractor, LazyLoadSearchExtractor):
    IE_NAME: str
    IE_DESC: str
    SEARCH_KEY: str

class YoutubeSearchIE(YoutubeTabBaseInfoExtractor, LazyLoadSearchExtractor):
    IE_NAME: str
    IE_DESC: str
    SEARCH_KEY: str

class YoutubeSearchURLIE(YoutubeTabBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeShortsAudioPivotIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeSubscriptionsIE(YoutubeFeedsInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeTabIE(YoutubeTabBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class YoutubeTruncatedIDIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: bool

class YoutubeTruncatedURLIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: bool

class YoutubeWatchLaterIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeWebArchiveIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeYtBeIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class YoutubeYtUserIE(YoutubeBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str

class ZDFChannelIE(ZDFBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class ZDFIE(ZDFBaseIE):
    IE_NAME: str

class ZaikoBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ZaikoETicketIE(ZaikoBaseIE):
    IE_NAME: str

class ZaikoIE(ZaikoBaseIE):
    IE_NAME: str

class ZapiksIE(LazyLoadExtractor):
    IE_NAME: str

class ZattooBaseIE(ZattooPlatformBaseIE):
    IE_NAME: str

class ZattooIE(ZattooBaseIE):
    IE_NAME: str

class ZattooLiveIE(ZattooBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class ZattooMoviesIE(ZattooBaseIE):
    IE_NAME: str

class ZattooRecordingsIE(ZattooBaseIE):
    IE_NAME: str

class Zee5IE(LazyLoadExtractor):
    IE_NAME: str

class Zee5SeriesIE(LazyLoadExtractor):
    IE_NAME: str

class ZeeNewsIE(LazyLoadExtractor):
    IE_NAME: str

class ZenPornIE(LazyLoadExtractor):
    IE_NAME: str
    age_limit: int

class ZenYandexBaseIE(LazyLoadExtractor):
    IE_NAME: str

class ZenYandexChannelIE(ZenYandexBaseIE):
    IE_NAME: str

class ZenYandexIE(ZenYandexBaseIE):
    IE_NAME: str
    IE_DESC: str

class ZetlandDKArticleIE(LazyLoadExtractor):
    IE_NAME: str

class ZhihuIE(LazyLoadExtractor):
    IE_NAME: str

class ZingMp3BaseIE(LazyLoadExtractor):
    IE_NAME: str

class ZingMp3AlbumIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3ChartHomeIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3ChartMusicVideoIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3HubIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3IE(ZingMp3BaseIE):
    IE_NAME: str
    IE_DESC: str

class ZingMp3LiveRadioIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3PodcastEpisodeIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3PodcastIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3UserIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3WeekChartIE(ZingMp3BaseIE):
    IE_NAME: str

class ZoomIE(LazyLoadExtractor):
    IE_NAME: str

class ZypeIE(LazyLoadExtractor):
    IE_NAME: str

class GenericIE(LazyLoadExtractor):
    IE_NAME: str
    IE_DESC: str
    age_limit: int
