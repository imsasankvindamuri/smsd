from . import get_suitable_downloader as get_suitable_downloader
from ..utils import update_url_query as update_url_query, urljoin as urljoin
from .fragment import FragmentFD as FragmentFD

class DashSegmentsFD(FragmentFD):
    FD_NAME: str
    def real_download(self, filename, info_dict): ...
