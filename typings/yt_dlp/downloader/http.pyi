from ..networking import Request as Request
from ..networking.exceptions import CertificateVerifyError as CertificateVerifyError, HTTPError as HTTPError, TransportError as TransportError
from ..utils import ContentTooShortError as ContentTooShortError, RetryManager as RetryManager, ThrottledDownload as ThrottledDownload, XAttrMetadataError as XAttrMetadataError, XAttrUnavailableError as XAttrUnavailableError, int_or_none as int_or_none, parse_http_range as parse_http_range, try_call as try_call, write_xattr as write_xattr
from ..utils.networking import HTTPHeaderDict as HTTPHeaderDict
from .common import FileDownloader as FileDownloader
from _typeshed import Incomplete

class HttpFD(FileDownloader):
    source_error: Incomplete
    def real_download(self, filename, info_dict): ...
