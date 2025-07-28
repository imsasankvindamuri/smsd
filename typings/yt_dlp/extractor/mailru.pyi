from ..utils import int_or_none as int_or_none, parse_duration as parse_duration, remove_end as remove_end, try_get as try_get, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class MailRuIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class MailRuMusicSearchBaseIE(InfoExtractor): ...

class MailRuMusicIE(MailRuMusicSearchBaseIE):
    IE_NAME: str
    IE_DESC: str

class MailRuMusicSearchIE(MailRuMusicSearchBaseIE):
    IE_NAME: str
    IE_DESC: str
