from random import randint
import os

from retrying import retry

from apysc.expression import last_scope
from apysc.file import file_util
from apysc.expression.expression_file_util import LAST_SCOPE_FILE_PATH


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_reset() -> None:
    file_util.save_plain_txt(
        txt='', file_path=LAST_SCOPE_FILE_PATH)
    last_scope.reset()
    assert not os.path.exists(LAST_SCOPE_FILE_PATH)
