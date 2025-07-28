from ..utils import check_executable as check_executable
from .common import FileDownloader as FileDownloader

class RtspFD(FileDownloader):
    def real_download(self, filename, info_dict): ...
