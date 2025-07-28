import dataclasses
import functools
import importlib.abc
from .globals import Indirect
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['COMPAT_PACKAGE_NAME', 'PACKAGE_NAME', 'PluginSpec', 'directories', 'load_all_plugins', 'load_plugins', 'register_plugin_spec']

PACKAGE_NAME: str
COMPAT_PACKAGE_NAME: str

@dataclasses.dataclass
class PluginSpec:
    module_name: str
    suffix: str
    destination: Indirect
    plugin_destination: Indirect

class PluginLoader(importlib.abc.Loader):
    def exec_module(self, module) -> None: ...

class PluginFinder(importlib.abc.MetaPathFinder):
    packages: Incomplete
    def __init__(self, *packages) -> None: ...
    def search_locations(self, fullname) -> Generator[Incomplete]: ...
    def find_spec(self, fullname, path=None, target=None): ...
    def invalidate_caches(self) -> None: ...

def directories(): ...
def load_plugins(plugin_spec: PluginSpec): ...
def load_all_plugins() -> None: ...
def register_plugin_spec(plugin_spec: PluginSpec): ...
