import os
from random import randint

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
