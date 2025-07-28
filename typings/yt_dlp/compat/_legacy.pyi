import base64
import collections
import getpass
import html.entities
import html.parser
import http.client
import http.cookiejar
import http.cookies
import http.server
import itertools
import shlex
import shutil
import socket
import tokenize
import urllib
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as etree
from . import compat_HTMLParseError as compat_HTMLParseError, compat_expanduser as compat_expanduser
from ..networking.exceptions import HTTPError as compat_HTTPError
from .compat_utils import passthrough_module as passthrough_module
from _typeshed import Incomplete

def compat_ctypes_WINFUNCTYPE(*args, **kwargs): ...
def compat_setenv(key, value, env=...) -> None: ...
compat_base64_b64decode = base64.b64decode
compat_basestring = str
compat_casefold: Incomplete
compat_chr = chr
compat_collections_abc = collections.abc
compat_cookiejar = http.cookiejar
compat_http_cookiejar = http.cookiejar
compat_cookiejar_Cookie = http.cookiejar.Cookie
compat_http_cookiejar_Cookie = http.cookiejar.Cookie
compat_cookies = http.cookies
compat_http_cookies = http.cookies
compat_cookies_SimpleCookie = http.cookies.SimpleCookie
compat_http_cookies_SimpleCookie = http.cookies.SimpleCookie
compat_etree_Element = etree.Element
compat_xml_etree_ElementTree_Element = etree.Element
compat_etree_register_namespace = etree.register_namespace
compat_xml_etree_register_namespace = etree.register_namespace
compat_filter = filter
compat_get_terminal_size = shutil.get_terminal_size
compat_getenv: Incomplete
compat_getpass = getpass.getpass
compat_getpass_getpass = getpass.getpass
compat_html_entities = html.entities
compat_html_entities_html5: Incomplete
compat_html_parser_HTMLParseError = compat_HTMLParseError
compat_HTMLParser = html.parser.HTMLParser
compat_html_parser_HTMLParser = html.parser.HTMLParser
compat_http_client = http.client
compat_http_server = http.server
compat_input = input
compat_integer_types: Incomplete
compat_itertools_count = itertools.count
compat_kwargs: Incomplete
compat_map = map
compat_numeric_types: Incomplete
compat_os_path_expanduser = compat_expanduser
compat_os_path_realpath: Incomplete
compat_print = print
compat_shlex_split = shlex.split
compat_socket_create_connection = socket.create_connection
compat_Struct: Incomplete
compat_struct_pack: Incomplete
compat_struct_unpack: Incomplete
compat_subprocess_get_DEVNULL: Incomplete
compat_tokenize_tokenize = tokenize.tokenize
compat_urllib_error = urllib.error
compat_urllib_HTTPError = compat_HTTPError
compat_urllib_parse = urllib.parse
compat_urllib_parse_parse_qs = urllib.parse.parse_qs
compat_urllib_parse_quote: Incomplete
compat_urllib_parse_quote_plus: Incomplete
compat_urllib_parse_unquote_plus = urllib.parse.unquote_plus
compat_urllib_parse_unquote_to_bytes = urllib.parse.unquote_to_bytes
compat_urllib_parse_urlunparse: Incomplete
compat_urllib_request = urllib.request
compat_urllib_request_DataHandler = urllib.request.DataHandler
compat_urllib_response = urllib.response
compat_urlretrieve = urllib.request.urlretrieve
compat_urllib_request_urlretrieve = urllib.request.urlretrieve
compat_xml_parse_error = etree.ParseError
compat_xml_etree_ElementTree_ParseError = etree.ParseError
compat_xpath: Incomplete
compat_zip = zip
workaround_optparse_bug9161: Incomplete
compat_str = str
compat_b64decode = base64.b64decode
compat_urlparse = urllib.parse
compat_parse_qs = urllib.parse.parse_qs
compat_urllib_parse_unquote = urllib.parse.unquote
compat_urllib_parse_urlencode = urllib.parse.urlencode
compat_urllib_parse_urlparse: Incomplete
legacy: Incomplete
