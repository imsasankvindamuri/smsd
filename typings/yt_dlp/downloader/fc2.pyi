from .common import FileDownloader as FileDownloader
from .external import FFmpegFD as FFmpegFD

class FC2LiveFD(FileDownloader):
    def real_download(self, filename, info_dict): ...
