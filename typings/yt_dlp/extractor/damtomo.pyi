from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, int_or_none as int_or_none, try_get as try_get, unified_strdate as unified_strdate
from .common import InfoExtractor as InfoExtractor

class DamtomoBaseIE(InfoExtractor): ...

class DamtomoVideoIE(DamtomoBaseIE):
    IE_NAME: str

class DamtomoRecordIE(DamtomoBaseIE):
    IE_NAME: str
