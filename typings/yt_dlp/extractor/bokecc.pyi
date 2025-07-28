from ..utils import ExtractorError as ExtractorError
from .common import InfoExtractor as InfoExtractor

class BokeCCBaseIE(InfoExtractor): ...

class BokeCCIE(BokeCCBaseIE):
    IE_DESC: str
