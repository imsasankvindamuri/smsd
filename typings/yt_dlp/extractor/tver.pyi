from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, join_nonempty as join_nonempty, make_archive_id as make_archive_id, smuggle_url as smuggle_url, str_or_none as str_or_none, strip_or_none as strip_or_none, update_url_query as update_url_query
from ..utils.traversal import require as require, traverse_obj as traverse_obj
from .streaks import StreaksBaseIE as StreaksBaseIE

class TVerIE(StreaksBaseIE):
    BRIGHTCOVE_URL_TEMPLATE: str
