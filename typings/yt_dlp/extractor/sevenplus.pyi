from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, try_get as try_get, update_url_query as update_url_query
from .brightcove import BrightcoveNewBaseIE as BrightcoveNewBaseIE

class SevenPlusIE(BrightcoveNewBaseIE):
    IE_NAME: str
