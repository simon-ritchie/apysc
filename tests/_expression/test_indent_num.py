from apysc._expression import event_handler_scope
from apysc._expression import expression_data_util
from apysc._expression import indent_num
from apysc._expression.indent_num import Indent
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn
import apysc as ap


@apply_test_settings()
def test_get_current_indent_num() -> None:
    ap.Stage()
    current_indent_num: int = indent_num.get_current_indent_num()
    assert current_indent_num == 0

    indent_num._save_current_indent_num(indent_num=2)
    current_indent_num = indent_num.get_current_indent_num()
    assert current_indent_num == 2


@apply_test_settings()
def test_reset() -> None:
    ap.Stage()
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
    @apply_test_settings()
    def test___enter__(self) -> None:
        indent_num.reset()
        with Indent():
            current_indent_num: int = indent_num.get_current_indent_num()
            assert current_indent_num == 1
            with Indent():
                current_indent_num = indent_num.get_current_indent_num()
                assert current_indent_num == 2

    @apply_test_settings()
    def test___exit__(self) -> None:
        indent_num.reset()
        with Indent():
            with Indent():
                pass
            current_indent_num: int = indent_num.get_current_indent_num()
            assert current_indent_num == 1
        current_indent_num = indent_num.get_current_indent_num()
        assert current_indent_num == 0


@apply_test_settings()
def test__get_indent_num_table_name() -> None:
    ap.Stage()
    table_name: str = indent_num._get_indent_num_table_name()
    assert table_name == expression_data_util.TableName.INDENT_NUM_NORMAL.value

    instance: VariableNameMixIn = VariableNameMixIn()
    instance.variable_name = "test_instance"
    with event_handler_scope.HandlerScope(
        handler_name="test_handler_1", instance=instance
    ):
        table_name = indent_num._get_indent_num_table_name()
        assert table_name == expression_data_util.TableName.INDENT_NUM_HANDLER.value
