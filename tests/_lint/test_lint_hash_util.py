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
        './_lint/.autopep8/'
    )
    assert os.path.isdir(dir_path)
