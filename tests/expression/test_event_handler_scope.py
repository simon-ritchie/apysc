from random import randint
import os

from retrying import retry

from apysc.expression import event_handler_scope
from apysc.expression import expression_file_util
from apysc.file import file_util


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_get_current_event_handler_scope_count() -> None:
    file_path: str = expression_file_util.EVENT_HANDLER_SCOPE_COUNT_FILE_PATH
    file_util.remove_file_if_exists(file_path=file_path)

    scope_count: int = \
        event_handler_scope.get_current_event_handler_scope_count()
    assert scope_count == 0

    file_util.save_plain_txt(txt='', file_path=file_path)
    scope_count = event_handler_scope.get_current_event_handler_scope_count()
    assert scope_count == 0

    file_util.save_plain_txt(txt='2', file_path=file_path)
    scope_count = event_handler_scope.get_current_event_handler_scope_count()
    assert scope_count == 2

    file_util.remove_file_if_exists(file_path=file_path)
