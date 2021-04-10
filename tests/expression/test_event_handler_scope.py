import os

from apysc.expression import event_handler_scope
from apysc.expression import expression_file_util
from apysc.file import file_util


def test_enter_event_handler_scope() -> None:
    file_util.remove_file_if_exists(
        file_path=expression_file_util.IS_EVENT_HANDLER_SCOPE_FILE_PATH)

    event_handler_scope.enter_event_handler_scope()
    assert os.path.isfile(
        expression_file_util.IS_EVENT_HANDLER_SCOPE_FILE_PATH)

    file_util.remove_file_if_exists(
        file_path=expression_file_util.IS_EVENT_HANDLER_SCOPE_FILE_PATH)
