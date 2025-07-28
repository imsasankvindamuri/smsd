from ..networking import PATCHRequest as PATCHRequest
from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, make_archive_id as make_archive_id, parse_iso8601 as parse_iso8601, smuggle_url as smuggle_url, try_call as try_call, unsmuggle_url as unsmuggle_url, update_url_query as update_url_query, url_or_none as url_or_none, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj
from .art19 import Art19IE as Art19IE
from .common import InfoExtractor as InfoExtractor

class NebulaBaseIE(InfoExtractor): ...

class NebulaIE(NebulaBaseIE):
    IE_NAME: str

class NebulaClassIE(NebulaBaseIE):
    IE_NAME: str

class NebulaSubscriptionsIE(NebulaBaseIE):
    IE_NAME: str

class NebulaChannelIE(NebulaBaseIE):
    IE_NAME: str
