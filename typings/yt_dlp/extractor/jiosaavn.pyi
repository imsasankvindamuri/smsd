import functools
from ..utils import ISO639Utils as ISO639Utils, InAdvancePagedList as InAdvancePagedList, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, int_or_none as int_or_none, js_to_json as js_to_json, make_archive_id as make_archive_id, orderedSet as orderedSet, smuggle_url as smuggle_url, unified_strdate as unified_strdate, unified_timestamp as unified_timestamp, unsmuggle_url as unsmuggle_url, url_basename as url_basename, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin, variadic as variadic
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class JioSaavnBaseIE(InfoExtractor):
    @functools.cached_property
    def requested_bitrates(self): ...

class JioSaavnSongIE(JioSaavnBaseIE):
    IE_NAME: str

class JioSaavnShowIE(JioSaavnBaseIE):
    IE_NAME: str

class JioSaavnAlbumIE(JioSaavnBaseIE):
    IE_NAME: str

class JioSaavnPlaylistIE(JioSaavnBaseIE):
    IE_NAME: str

class JioSaavnShowPlaylistIE(JioSaavnBaseIE):
    IE_NAME: str

class JioSaavnArtistIE(JioSaavnBaseIE):
    IE_NAME: str
