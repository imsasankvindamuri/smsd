from ..utils import clean_html as clean_html, dict_get as dict_get, int_or_none as int_or_none, parse_duration as parse_duration, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class SkyItBaseIE(InfoExtractor): ...

class SkyItPlayerIE(SkyItBaseIE):
    IE_NAME: str

class SkyItVideoIE(SkyItBaseIE):
    IE_NAME: str

class SkyItVideoLiveIE(SkyItBaseIE):
    IE_NAME: str

class SkyItIE(SkyItBaseIE):
    IE_NAME: str

class SkyItArteIE(SkyItIE):
    IE_NAME: str

class CieloTVItIE(SkyItIE):
    IE_NAME: str

class TV8ItIE(SkyItVideoIE):
    IE_NAME: str

class TV8ItLiveIE(SkyItBaseIE):
    IE_NAME: str
    IE_DESC: str

class TV8ItPlaylistIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
