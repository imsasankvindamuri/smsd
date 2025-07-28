from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, extract_attributes as extract_attributes, int_or_none as int_or_none, parse_qs as parse_qs, smuggle_url as smuggle_url, unescapeHTML as unescapeHTML, unsmuggle_url as unsmuggle_url
from .common import InfoExtractor as InfoExtractor

class GlomexBaseIE(InfoExtractor): ...

class GlomexIE(GlomexBaseIE):
    IE_NAME: str
    IE_DESC: str

class GlomexEmbedIE(GlomexBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def build_player_url(cls, video_id, integration, origin_url=None): ...
