from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, js_to_json as js_to_json, mimetype2ext as mimetype2ext, parse_iso8601 as parse_iso8601, str_or_none as str_or_none, strip_or_none as strip_or_none, traverse_obj as traverse_obj, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class ImgurBaseIE(InfoExtractor):
    @staticmethod
    def get_description(s): ...

class ImgurIE(ImgurBaseIE): ...
class ImgurGalleryBaseIE(ImgurBaseIE): ...

class ImgurGalleryIE(ImgurGalleryBaseIE):
    IE_NAME: str

class ImgurAlbumIE(ImgurGalleryBaseIE):
    IE_NAME: str
