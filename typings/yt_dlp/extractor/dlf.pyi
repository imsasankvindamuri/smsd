from ..utils import determine_ext as determine_ext, extract_attributes as extract_attributes, int_or_none as int_or_none, traverse_obj as traverse_obj, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class DLFBaseIE(InfoExtractor): ...

class DLFIE(DLFBaseIE):
    IE_NAME: str

class DLFCorpusIE(DLFBaseIE):
    IE_NAME: str
    IE_DESC: str
