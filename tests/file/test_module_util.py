from typing import List
from apysc.file import module_util


def test_get_module_paths_recursively() -> None:
    module_paths: List[str] = module_util.get_module_paths_recursively(
        dir_path='./apysc/jslib/')
    assert './apysc/jslib/jslib_util.py' in module_paths
    assert './apysc/jslib/__init__.py' not in module_paths
    assert './apysc/jslib/jquery.min.js' not in module_paths

    module_paths = module_util.get_module_paths_recursively(
        dir_path='./tests/')
    assert './tests/file/test_module_util.py' in module_paths
