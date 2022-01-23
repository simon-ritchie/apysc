import os
from random import randint
from types import ModuleType
from typing import Any
from typing import List

from retrying import retry

from apysc._display import sprite
from apysc._display.sprite import Sprite
from apysc._file import module_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_module_paths_recursively() -> None:
    module_paths: List[str] = module_util.get_module_paths_recursively(
        dir_path='./apysc/_jslib/')
    assert './apysc/_jslib/jslib_util.py' in module_paths
    assert './apysc/_jslib/__init__.py' not in module_paths
    assert './apysc/_jslib/jquery.min.js' not in module_paths

    module_paths = module_util.get_module_paths_recursively(
        dir_path='./tests/')
    assert './tests/_file/test_module_util.py' in module_paths


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_save_tmp_module_and_run_script() -> None:
    script: str = (
        'from apysc import Int'
        '\nprint(Int(10))'
    )
    stdout: str = module_util.save_tmp_module_and_run_script(script=script)
    assert stdout == '10\n'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_save_tmp_module() -> None:
    script: str = 'print(100)'
    saved_module_path: str = module_util.save_tmp_module(script=script)
    with open(saved_module_path, 'r') as f:
        saved_script: str = f.read()
    os.remove(saved_module_path)
    assert saved_script == 'print(100)'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_read_target_path_module() -> None:
    module: ModuleType = module_util.read_target_path_module(
        module_path='./apysc/_file/module_util.py')
    assert module == module_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__read_module_or_class() -> None:
    module_or_class: Any = module_util.read_module_or_class_from_package_path(
        module_or_class_package_path='apysc._display.sprite')
    assert module_or_class == sprite

    module_or_class = module_util.read_module_or_class_from_package_path(
        module_or_class_package_path='apysc._display.sprite.Sprite')
    assert module_or_class == Sprite
