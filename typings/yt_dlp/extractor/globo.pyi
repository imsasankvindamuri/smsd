from ..utils import determine_ext as determine_ext, filter_dict as filter_dict, float_or_none as float_or_none, int_or_none as int_or_none, orderedSet as orderedSet, str_or_none as str_or_none, try_get as try_get, url_or_none as url_or_none
from ..utils.traversal import subs_list_to_dict as subs_list_to_dict, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class GloboIE(InfoExtractor): ...

class GloboArticleIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
