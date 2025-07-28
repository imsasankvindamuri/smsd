from . import HlsFD as HlsFD
from ..networking import Request as Request
from ..networking.exceptions import network_exceptions as network_exceptions
from .common import FileDownloader as FileDownloader

class BunnyCdnFD(FileDownloader):
    def real_download(self, filename, info_dict): ...
    def ping_thread(self, stop_event, url, headers, secret, context_id) -> None: ...
