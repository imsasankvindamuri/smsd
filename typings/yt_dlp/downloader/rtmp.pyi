from ..utils import Popen as Popen, check_executable as check_executable, encodeArgument as encodeArgument, get_exe_version as get_exe_version
from .common import FileDownloader as FileDownloader

def rtmpdump_version(): ...

class RtmpFD(FileDownloader):
    def real_download(self, filename, info_dict): ...
