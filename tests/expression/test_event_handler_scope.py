from random import randint
import os

from retrying import retry

from apysc.expression import event_handler_scope
from apysc.expression import expression_file_util
from apysc.file import file_util


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_current_scope_is_event_handler() -> None:
    file_util.remove_file_if_exists(
        file_path=expression_file_util.IS_EVENT_HANDLER_SCOPE_FILE_PATH)
    result: bool = event_handler_scope.current_scope_is_event_handler()
    assert not result

    file_util.save_plain_txt(
        txt='',
        file_path=expression_file_util.IS_EVENT_HANDLER_SCOPE_FILE_PATH)
    result = event_handler_scope.current_scope_is_event_handler()
    assert result

    file_util.remove_file_if_exists(
        file_path=expression_file_util.IS_EVENT_HANDLER_SCOPE_FILE_PATH)
