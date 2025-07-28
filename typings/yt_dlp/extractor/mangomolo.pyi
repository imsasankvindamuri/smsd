from ..utils import classproperty as classproperty, int_or_none as int_or_none
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class MangomoloBaseIE(InfoExtractor): ...

class MangomoloVideoIE(MangomoloBaseIE):
    IE_NAME: Incomplete

class MangomoloLiveIE(MangomoloBaseIE):
    IE_NAME: Incomplete
