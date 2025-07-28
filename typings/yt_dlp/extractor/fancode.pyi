from ..utils import ExtractorError as ExtractorError, mimetype2ext as mimetype2ext, parse_iso8601 as parse_iso8601, try_get as try_get
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class FancodeVodIE(InfoExtractor):
    IE_NAME: str
    headers: Incomplete
    def download_gql(self, variable, data, note, fatal: bool = False, headers=...): ...

class FancodeLiveIE(FancodeVodIE):
    IE_NAME: str
