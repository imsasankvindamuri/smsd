from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, int_or_none as int_or_none, join_nonempty as join_nonempty, js_to_json as js_to_json, str_or_none as str_or_none, strip_jsonp as strip_jsonp, traverse_obj as traverse_obj, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class QQMusicBaseIE(InfoExtractor):
    @property
    def is_logged_in(self): ...

class QQMusicIE(QQMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicSingerIE(QQMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQPlaylistBaseIE(InfoExtractor): ...

class QQMusicAlbumIE(QQPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicToplistIE(QQPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicPlaylistIE(QQPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class QQMusicVideoIE(QQMusicBaseIE):
    IE_NAME: str
    IE_DESC: str
