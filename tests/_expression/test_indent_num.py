from random import randint

from retrying import retry

from apysc._expression import event_handler_scope
from apysc._expression import expression_data_util
from apysc._expression import indent_num
from apysc._expression.indent_num import Indent


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_current_indent_num() -> None:
    expression_data_util.empty_expression()
    current_indent_num: int = indent_num.get_current_indent_num()
    assert current_indent_num == 0

    indent_num._save_current_indent_num(indent_num=2)
    current_indent_num = indent_num.get_current_indent_num()
    assert current_indent_num == 2


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_reset() -> None:
    expression_data_util.empty_expression()
    with Indent():
        indent_num.reset()
        current_indent_num: int = indent_num.get_current_indent_num()
        assert current_indent_num == 0

    event_handler_scope._increment_scope_count()
    with Indent():
        indent_num.reset()
        current_indent_num = indent_num.get_current_indent_num()
        assert current_indent_num == 0


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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_indent_num_table_name() -> None:
    expression_data_util.empty_expression()
    table_name: str = indent_num._get_indent_num_table_name()
    assert table_name == \
        expression_data_util.TableName.INDENT_NUM_NORMAL.value

    with event_handler_scope.HandlerScope():
        table_name = indent_num._get_indent_num_table_name()
        assert table_name == \
            expression_data_util.TableName.INDENT_NUM_HANDLER.value
