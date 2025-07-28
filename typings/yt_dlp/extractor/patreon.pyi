import functools
from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, KNOWN_EXTENSIONS as KNOWN_EXTENSIONS, clean_html as clean_html, determine_ext as determine_ext, int_or_none as int_or_none, mimetype2ext as mimetype2ext, parse_iso8601 as parse_iso8601, smuggle_url as smuggle_url, str_or_none as str_or_none, url_or_none as url_or_none, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj, value as value
from .common import InfoExtractor as InfoExtractor
from .sproutvideo import VidsIoIE as VidsIoIE
from .vimeo import VimeoIE as VimeoIE

class PatreonBaseIE(InfoExtractor):
    @functools.cached_property
    def patreon_user_agent(self): ...

class PatreonIE(PatreonBaseIE):
    IE_NAME: str

class PatreonCampaignIE(PatreonBaseIE):
    IE_NAME: str
