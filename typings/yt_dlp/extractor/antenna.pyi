from ..networking import HEADRequest as HEADRequest
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, make_archive_id as make_archive_id, scale_thumbnails_to_max_format_width as scale_thumbnails_to_max_format_width
from .common import InfoExtractor as InfoExtractor

class AntennaBaseIE(InfoExtractor): ...

class AntennaGrWatchIE(AntennaBaseIE):
    IE_NAME: str
    IE_DESC: str

class Ant1NewsGrArticleIE(AntennaBaseIE):
    IE_NAME: str
    IE_DESC: str

class Ant1NewsGrEmbedIE(AntennaBaseIE):
    IE_NAME: str
    IE_DESC: str
