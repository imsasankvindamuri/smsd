from ..dependencies import websockets as websockets
from .common import FileDownloader as FileDownloader
from .external import FFmpegFD as FFmpegFD

class FFmpegSinkFD(FileDownloader):
    def real_download(self, filename, info_dict): ...
    async def real_connection(self, sink, info_dict) -> None: ...

class WebSocketFragmentFD(FFmpegSinkFD):
    async def real_connection(self, sink, info_dict) -> None: ...
