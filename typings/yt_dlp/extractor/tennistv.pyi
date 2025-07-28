from ..utils import ExtractorError as ExtractorError, random_uuidv4 as random_uuidv4, unified_timestamp as unified_timestamp, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class TennisTVIE(InfoExtractor):
    access_token: Incomplete
    refresh_token: Incomplete
    def get_token(self, video_id, payload) -> None: ...
