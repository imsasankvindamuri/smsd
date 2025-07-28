from ..utils import classproperty as classproperty, int_or_none as int_or_none, traverse_obj as traverse_obj, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class BrainPOPBaseIE(InfoExtractor): ...
class BrainPOPIE(BrainPOPBaseIE): ...
class BrainPOPLegacyBaseIE(BrainPOPBaseIE): ...
class BrainPOPJrIE(BrainPOPLegacyBaseIE): ...
class BrainPOPELLIE(BrainPOPLegacyBaseIE): ...

class BrainPOPEspIE(BrainPOPLegacyBaseIE):
    IE_DESC: str

class BrainPOPFrIE(BrainPOPLegacyBaseIE):
    IE_DESC: str

class BrainPOPIlIE(BrainPOPLegacyBaseIE):
    IE_DESC: str
