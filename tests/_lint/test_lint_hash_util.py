import os
from random import randint

from retrying import retry

from apysc._lint import lint_hash_util
from apysc._lint.lint_hash_util import LintType


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_lint_hash_dir_path() -> None:
    dir_path: str = lint_hash_util.get_lint_hash_dir_path(
        lint_type=LintType.AUTOPEP8)
    assert dir_path == (
        './apysc/_lint/.autopep8/'
    )
    assert os.path.isdir(dir_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_target_module_hash_file_path() -> None:
    file_path: str = lint_hash_util.get_target_module_hash_file_path(
        module_path='./apysc/_display/sprite.py',
        lint_type=LintType.AUTOPEP8)
    expected: str = (
        './apysc/_lint/.autopep8/apysc/_display/sprite.py'
    )
    assert file_path == expected
    assert os.path.isdir(os.path.dirname(file_path))


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_read_target_module_hash() -> None:
    hashed_string: str = lint_hash_util.read_target_module_hash(
        module_path='./apysc/_display/not_existing_module.py')
    assert hashed_string == ''

    hashed_string = lint_hash_util.read_target_module_hash(
        module_path='./apysc/_display/sprite.py')
    assert hashed_string != ''
