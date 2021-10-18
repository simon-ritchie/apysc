import os
from random import randint
from typing import List

from retrying import retry

import apply_lints_and_build_docs
from apply_lints_and_build_docs import LintCommand
from apysc._file import file_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_run_lint_command() -> None:
    lint_command: LintCommand = {
        'command': 'ls -l',
        'lint_name': 'test',
    }
    stdout: str = apply_lints_and_build_docs.run_lint_command(
        lint_command=lint_command)
    assert 'apysc' in stdout


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_tmp_py_module() -> None:
    file_util.save_plain_txt(txt='\n', file_path='./tmp_123.py')
    apply_lints_and_build_docs._remove_tmp_py_module()
    assert not os.path.exists('./tmp_123.py')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_run_command() -> None:
    stdout: str = apply_lints_and_build_docs.run_command(command='ls')
    assert 'apysc' in stdout


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_root_dir_module_paths() -> None:
    module_paths: List[str] = apply_lints_and_build_docs.\
        _get_root_dir_module_paths()
    expected_paths: List[str] = [
        './apply_lints_and_build_docs.py',
        './build.py',
    ]
    for expected in expected_paths:
        assert expected in module_paths

    unexpected_paths: List[str] = [
        './__init__.py',
        './apysc',
        './requirements.txt',
    ]
    for unexpected in unexpected_paths:
        assert unexpected not in module_paths


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_module_paths() -> None:
    module_paths: List[str] = apply_lints_and_build_docs._get_module_paths()
    expected_paths: List[str] = [
        './apysc/_display/sprite.py',
        './docs_src/source/conf.py',
        './tests/_display/test_sprite.py',
        './test_projects/draw_rect/main.py',
        './build.py',
    ]
    for expected in expected_paths:
        assert expected in module_paths
        assert expected.endswith('.py')
