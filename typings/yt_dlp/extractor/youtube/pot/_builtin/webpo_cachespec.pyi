from yt_dlp.extractor.youtube.pot._provider import BuiltinIEContentProvider as BuiltinIEContentProvider
from yt_dlp.extractor.youtube.pot.cache import CacheProviderWritePolicy as CacheProviderWritePolicy, PoTokenCacheSpec as PoTokenCacheSpec, PoTokenCacheSpecProvider as PoTokenCacheSpecProvider, register_spec as register_spec
from yt_dlp.extractor.youtube.pot.provider import PoTokenRequest as PoTokenRequest
from yt_dlp.extractor.youtube.pot.utils import ContentBindingType as ContentBindingType, get_webpo_content_binding as get_webpo_content_binding
from yt_dlp.utils import traverse_obj as traverse_obj

class WebPoPCSP(PoTokenCacheSpecProvider, BuiltinIEContentProvider):
    PROVIDER_NAME: str
    def generate_cache_spec(self, request: PoTokenRequest) -> PoTokenCacheSpec | None: ...
