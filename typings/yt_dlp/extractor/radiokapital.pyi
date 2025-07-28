from ..utils import clean_html as clean_html, traverse_obj as traverse_obj, unescapeHTML as unescapeHTML
from .common import InfoExtractor as InfoExtractor

class RadioKapitalBaseIE(InfoExtractor): ...

class RadioKapitalIE(RadioKapitalBaseIE):
    IE_NAME: str

class RadioKapitalShowIE(RadioKapitalBaseIE):
    IE_NAME: str
