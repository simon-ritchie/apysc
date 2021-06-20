from random import randint
from typing import List

from retrying import retry

from apysc._file import module_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_module_paths_recursively() -> None:
    module_paths: List[str] = module_util.get_module_paths_recursively(
        dir_path='./apysc/jslib/')
    assert './apysc/jslib/jslib_util.py' in module_paths
    assert './apysc/jslib/__init__.py' not in module_paths
    assert './apysc/jslib/jquery.min.js' not in module_paths

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
