from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, js_to_json as js_to_json, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class IPrimaIE(InfoExtractor):
    access_token: Incomplete

class IPrimaCNNIE(InfoExtractor): ...
