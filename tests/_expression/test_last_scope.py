import os
from random import randint

from retrying import retry

from apysc._expression import last_scope
from apysc._expression.expression_file_util import LAST_SCOPE_FILE_PATH
from apysc._expression.last_scope import LastScope
from apysc._file import file_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_reset() -> None:
    file_util.save_plain_txt(
        txt='', file_path=LAST_SCOPE_FILE_PATH)
    last_scope.reset()
    assert not os.path.exists(LAST_SCOPE_FILE_PATH)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_last_scope() -> None:
    last_scope.reset()
    last_scope_: LastScope = last_scope.get_last_scope()
    assert last_scope_ == last_scope.LastScope.NORMAL

    file_util.save_plain_txt(
        txt='', file_path=LAST_SCOPE_FILE_PATH)
    last_scope_ = last_scope.get_last_scope()
    assert last_scope_ == last_scope.LastScope.NORMAL

    last_scope.set_last_scope(value=last_scope.LastScope.IF)
    last_scope_ = last_scope.get_last_scope()
    assert last_scope_ == last_scope.LastScope.IF


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_set_last_scope() -> None:
    last_scope.reset()
    last_scope.set_last_scope(value=last_scope.LastScope.IF)
    last_scope_: LastScope = last_scope.get_last_scope()
    assert last_scope_ == last_scope.LastScope.IF
