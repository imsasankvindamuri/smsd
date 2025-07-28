from ..utils import determine_ext as determine_ext, get_elements_text_and_html_by_attribute as get_elements_text_and_html_by_attribute, scale_thumbnails_to_max_format_width as scale_thumbnails_to_max_format_width
from .common import InfoExtractor as InfoExtractor

class TVOpenGrBaseIE(InfoExtractor): ...

class TVOpenGrWatchIE(TVOpenGrBaseIE):
    IE_NAME: str
    IE_DESC: str

class TVOpenGrEmbedIE(TVOpenGrBaseIE):
    IE_NAME: str
    IE_DESC: str
