import os
from random import randint
from typing import List

from retrying import retry

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
