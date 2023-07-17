import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression.event_handler_scope import HandlerScope
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.copy_mixin import CopyMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn


class TestCopyMixIn:
    @apply_test_settings()
    def test__copy(self) -> None:
        mixin: CopyMixIn = CopyMixIn()
        mixin.variable_name = "test_copy_mixin"
        mixin._type_name = "test_copy_mixin"
        result: CopyMixIn = mixin._copy()
        assert result.variable_name.startswith("test_copy_mixin_")
        assert result.variable_name != mixin.variable_name

    @apply_test_settings()
    def test__append_copy_expression(self) -> None:
        int_1: ap.Int = ap.Int(10)
        int_2: ap.Int = int_1._copy()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{int_2.variable_name} = " f"{int_1.variable_name};"
        assert expected in expression

        ap.Stage()
        arr_1: ap.Array = ap.Array([10, 20, 30])
        arr_2: ap.Array = arr_1._copy()
        expression = expression_data_util.get_current_expression()
        expected = f"{arr_2.variable_name} = " f"cpy({arr_1.variable_name});"
        assert expected in expression

    @apply_test_settings()
    def test__append_value_updating_cpy_exp_to_handler_scope(self) -> None:
        instance: VariableNameMixIn = VariableNameMixIn()
        instance.variable_name = "test_instance"
        int_1: ap.Int = ap.Int(10)
        with HandlerScope(handler_name="test_handler_1", instance=instance):
            int_2: ap.Int = int_1._copy()
        expression: str = (
            expression_data_util.get_current_event_handler_scope_expression()
        )
        pattern: str = rf"^{int_2.variable_name} = {int_1.variable_name};"
        match: Optional[Match] = re.search(
            pattern=pattern, string=expression, flags=re.MULTILINE
        )
        assert match is not None

        ap.Stage()
        arr_1: ap.Array = ap.Array([1, 2, 3])
        with HandlerScope(handler_name="test_handler_1", instance=instance):
            arr_2: ap.Array = arr_1._copy()
        expression = expression_data_util.get_current_event_handler_scope_expression()
        pattern = rf"^{arr_2.variable_name} = cpy\({arr_1.variable_name}\);"
        match = re.search(pattern=pattern, string=expression, flags=re.MULTILINE)
        assert match is not None
