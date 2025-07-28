from ..aes import aes_ecb_encrypt as aes_ecb_encrypt, pkcs7_padding as pkcs7_padding
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, join_nonempty as join_nonempty, str_or_none as str_or_none, strftime_or_none as strftime_or_none, traverse_obj as traverse_obj, unified_strdate as unified_strdate, url_or_none as url_or_none, urljoin as urljoin, variadic as variadic
from .common import InfoExtractor as InfoExtractor

class NetEaseMusicBaseIE(InfoExtractor): ...

class NetEaseMusicIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicAlbumIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str

class NetEaseMusicSingerIE(NetEaseMusicBaseIE):
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

class NetEaseMusicDjRadioIE(NetEaseMusicBaseIE):
    IE_NAME: str
    IE_DESC: str
