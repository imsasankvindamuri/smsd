from ..utils import OnDemandPagedList as OnDemandPagedList, int_or_none as int_or_none, merge_dicts as merge_dicts, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, parse_qs as parse_qs, try_get as try_get, update_url_query as update_url_query, urljoin as urljoin
from .turner import TurnerBaseIE as TurnerBaseIE

class NBACVPBaseIE(TurnerBaseIE): ...
class NBAWatchBaseIE(NBACVPBaseIE): ...

class NBAWatchEmbedIE(NBAWatchBaseIE):
    IE_NAME: str

class NBAWatchIE(NBAWatchBaseIE):
    IE_NAME: str

class NBAWatchCollectionIE(NBAWatchBaseIE):
    IE_NAME: str

class NBABaseIE(NBACVPBaseIE): ...

class NBAEmbedIE(NBABaseIE):
    IE_NAME: str

class NBAIE(NBABaseIE):
    IE_NAME: str

class NBAChannelIE(NBABaseIE):
    IE_NAME: str
