from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, UnsupportedError as UnsupportedError, clean_html as clean_html, extract_attributes as extract_attributes, format_field as format_field, get_element_by_class as get_element_by_class, get_elements_html_by_class as get_elements_html_by_class, int_or_none as int_or_none, join_nonempty as join_nonempty, parse_count as parse_count, parse_iso8601 as parse_iso8601, traverse_obj as traverse_obj, unescapeHTML as unescapeHTML, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete
from collections.abc import Generator

class RumbleEmbedIE(InfoExtractor): ...
class RumbleIE(InfoExtractor): ...

class RumbleChannelIE(InfoExtractor):
    def entries(self, url, playlist_id) -> Generator[Incomplete]: ...
