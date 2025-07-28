from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, age_restricted as age_restricted, clean_html as clean_html, extract_attributes as extract_attributes, int_or_none as int_or_none, traverse_obj as traverse_obj, try_get as try_get, unescapeHTML as unescapeHTML, unsmuggle_url as unsmuggle_url, update_url as update_url, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class DailymotionBaseInfoExtractor(InfoExtractor): ...

class DailymotionIE(DailymotionBaseInfoExtractor):
    IE_NAME: str

class DailymotionPlaylistBaseIE(DailymotionBaseInfoExtractor): ...

class DailymotionPlaylistIE(DailymotionPlaylistBaseIE):
    IE_NAME: str

class DailymotionSearchIE(DailymotionPlaylistBaseIE):
    IE_NAME: str

class DailymotionUserIE(DailymotionPlaylistBaseIE):
    IE_NAME: str
