from ..utils import clean_html as clean_html, float_or_none as float_or_none, int_or_none as int_or_none, parse_qs as parse_qs, try_get as try_get, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class CiscoLiveBaseIE(InfoExtractor):
    RAINFOCUS_API_URL: str
    RAINFOCUS_API_PROFILE_ID: str
    RAINFOCUS_WIDGET_ID: str
    BRIGHTCOVE_URL_TEMPLATE: str
    HEADERS: Incomplete

class CiscoLiveSessionIE(CiscoLiveBaseIE): ...

class CiscoLiveSearchIE(CiscoLiveBaseIE):
    @classmethod
    def suitable(cls, url): ...
