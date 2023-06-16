from typing import Dict
import pytest

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings


class TestInt:
    @apply_test_settings()
    def test___init__(self) -> None:
        expression_data_util.empty_expression()
        int_val_1: ap.Int = ap.Int(value=100.5)
        assert int_val_1.value == 100
        assert int_val_1.variable_name.startswith(f"{var_names.INT}_")

        expression: str = expression_data_util.get_current_expression()
        expected: str = f"var {int_val_1.variable_name} = 100;"
        assert expected in expression

        int_val_2: ap.Int = ap.Int(value=int_val_1)
        expression = expression_data_util.get_current_expression()
        expected = f"var {int_val_2.variable_name} = {int_val_1.variable_name};"
        assert expected in expression

        testing_helper.assert_raises(
            expected_error_class=ValueError, callable_=ap.Int, value="Hello!"
        )

        int_val_3: ap.Int = ap.Int(value=10, variable_name_suffix="test_int_3")
        assert int_val_3._variable_name_suffix == "test_int_3"

    @apply_test_settings()
    def test_value(self) -> None:
        expression_data_util.empty_expression()
        int_val_1: ap.Int = ap.Int(value=100)
        int_val_1.value = 200.5  # type: ignore
        assert int_val_1.value == 200

        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{int_val_1.variable_name} = 200;"
        assert expected in expression

        with pytest.raises(ValueError):  # type: ignore
            int_val_1.value = "Hello!"  # type: ignore

        int_val_2: ap.Int = ap.Int(value=100)
        int_val_2.value = int_val_1
        assert int_val_2.value == 200  # type: ignore
        expression = expression_data_util.get_current_expression()
        expected = f"{int_val_2.variable_name} = {int_val_1.variable_name};"

    @apply_test_settings()
    def test___add__(self) -> None:
        int_1: ap.Int = ap.Int(value=10)
        int_2: ap.Int = int_1 + 10.5
        assert int_2.value == 20

    @apply_test_settings()
    def test_set_value_and_skip_expression_appending(self) -> None:
        expression_data_util.empty_expression()
        int_1: ap.Int = ap.Int(value=10)
        int_1._set_value_and_skip_expression_appending(value=20.5)
        assert int_1.value == 20
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{int_1.variable_name} = 20;"
        assert expected not in expression

        int_2: ap.Int = ap.Int(value=30)
        int_2._set_value_and_skip_expression_appending(value=int_1)
        expression = expression_data_util.get_current_expression()
        expected = f"{int_2.variable_name} = {int_1.variable_name};"
        assert expected not in expression

    @apply_test_settings()
    def test__append_cast_expression(self) -> None:
        expression_data_util.empty_expression()
        int_val: ap.Int = ap.Int(value=ap.Number(value=100.5))
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{int_val.variable_name} = " f"Math.trunc({int_val.variable_name}, 10);"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        int_val = ap.Int(value=100)
        expression = expression_data_util.get_current_expression()
        assert "Math.trunc" not in expression

        expression_data_util.empty_expression()
        int_val = ap.Int(value=100.5)
        expression = expression_data_util.get_current_expression()
        assert "Math.trunc" not in expression
        expected = f"{int_val.variable_name} = 100;"
        assert expected in expression

    @apply_test_settings()
    def test___repr__(self) -> None:
        int_1: ap.Int = ap.Int(3)
        repr_str: str = repr(int_1)
        assert repr_str == "Int(3)"

        del int_1._value
        assert repr(int_1) == "Int(0)"

    @apply_test_settings()
    def test__initialize_for_loop_key_or_value(self) -> None:
        int_value: ap.Int = ap.Int._initialize_for_loop_key_or_value()
        assert int_value == ap.Int(0)

    @apply_test_settings()
    def test___hash__(self) -> None:
        int_value: ap.Int = ap.Int(5)
        assert int_value.__hash__() == 5
        dict_val: Dict[ap.Int, int] = {ap.Int(10): 5}
        assert dict_val[ap.Int(10)] == 5
