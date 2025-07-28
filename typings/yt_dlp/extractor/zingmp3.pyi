from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, join_nonempty as join_nonempty, try_call as try_call, url_or_none as url_or_none, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class ZingMp3BaseIE(InfoExtractor): ...

class ZingMp3IE(ZingMp3BaseIE):
    IE_NAME: str
    IE_DESC: str

class ZingMp3AlbumIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3ChartHomeIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3WeekChartIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3ChartMusicVideoIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3UserIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3HubIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3LiveRadioIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3PodcastEpisodeIE(ZingMp3BaseIE):
    IE_NAME: str

class ZingMp3PodcastIE(ZingMp3BaseIE):
    IE_NAME: str
