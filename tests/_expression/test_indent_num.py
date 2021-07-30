from random import randint

from retrying import retry

from apysc._expression import event_handler_scope
from apysc._expression import expression_file_util
from apysc._expression import indent_num
from apysc._expression.expression_file_util import INDENT_NUM_FILE_PATH
from apysc._expression.indent_num import Indent
from apysc._file import file_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_current_indent_num() -> None:
    file_util.remove_file_if_exists(file_path=INDENT_NUM_FILE_PATH)
    current_indent_num: int = indent_num.get_current_indent_num()
    assert current_indent_num == 0

    file_util.save_plain_txt(
        txt='', file_path=INDENT_NUM_FILE_PATH)
    current_indent_num = indent_num.get_current_indent_num()
    assert current_indent_num == 0

    file_util.save_plain_txt(txt=' 2 ', file_path=INDENT_NUM_FILE_PATH)
    current_indent_num = indent_num.get_current_indent_num()
    assert current_indent_num == 2


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_reset() -> None:
    expression_file_util.empty_expression_dir()
    with Indent():
        indent_num.reset()
        current_indent_num: int = indent_num.get_current_indent_num()
        assert current_indent_num == 0

    event_handler_scope._increment_scope_count()
    with Indent():
        indent_num.reset()
        current_indent_num = indent_num.get_current_indent_num()
        assert current_indent_num == 0


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_indent_num_file_path() -> None:
    expression_file_util.empty_expression_dir()
    file_path: str = indent_num._get_indent_num_file_path()
    assert file_path == expression_file_util.INDENT_NUM_FILE_PATH

    event_handler_scope._increment_scope_count()
    file_path = indent_num._get_indent_num_file_path()
    assert file_path == \
        expression_file_util.EVENT_HANDLER_INDENT_NUM_FILE_PATH
    expression_file_util.empty_expression_dir()


class TestIndent:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___enter__(self) -> None:
        indent_num.reset()
        with Indent():
            current_indent_num: int = indent_num.get_current_indent_num()
            assert current_indent_num == 1
            with Indent():
                current_indent_num = indent_num.get_current_indent_num()
                assert current_indent_num == 2

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___exit__(self) -> None:
        indent_num.reset()
        with Indent():
            with Indent():
                pass
            current_indent_num: int = indent_num.get_current_indent_num()
            assert current_indent_num == 1
        current_indent_num = indent_num.get_current_indent_num()
        assert current_indent_num == 0
