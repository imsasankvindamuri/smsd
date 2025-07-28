from . import get_suitable_downloader as get_suitable_downloader
from .. import webvtt as webvtt
from ..dependencies import Cryptodome as Cryptodome
from ..utils import bug_reports_message as bug_reports_message, parse_m3u8_attributes as parse_m3u8_attributes, remove_start as remove_start, traverse_obj as traverse_obj, update_url_query as update_url_query, urljoin as urljoin
from .external import FFmpegFD as FFmpegFD
from .fragment import FragmentFD as FragmentFD

class HlsFD(FragmentFD):
    FD_NAME: str
    @classmethod
    def can_download(cls, manifest, info_dict, allow_unplayable_formats: bool = False): ...
    def real_download(self, filename, info_dict): ...
