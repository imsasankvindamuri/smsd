from ..networking import Request as Request
from ..networking.websocket import WebSocketResponse as WebSocketResponse
from ..utils import DownloadError as DownloadError, str_or_none as str_or_none, truncate_string as truncate_string
from ..utils.traversal import traverse_obj as traverse_obj
from .common import FileDownloader as FileDownloader
from .external import FFmpegFD as FFmpegFD

class NiconicoLiveFD(FileDownloader):
    def real_download(self, filename, info_dict): ...
