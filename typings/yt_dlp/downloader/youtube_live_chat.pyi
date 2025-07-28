from ..networking.exceptions import HTTPError as HTTPError
from ..utils import RegexNotFoundError as RegexNotFoundError, RetryManager as RetryManager, dict_get as dict_get, int_or_none as int_or_none, try_get as try_get
from ..utils.networking import HTTPHeaderDict as HTTPHeaderDict
from .fragment import FragmentFD as FragmentFD

class YoutubeLiveChatFD(FragmentFD):
    def real_download(self, filename, info_dict): ...
    @staticmethod
    def parse_live_timestamp(action): ...
