import pytest

import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings
from apysc._type import type_util


class TestNumber:

    expression_data_util.empty_expression()

    @apply_test_settings()
    def test___init__(self) -> None:
        expression_data_util.empty_expression()
        number_1: ap.Number = ap.Number(value=100, variable_name_suffix="test_number")
        assert number_1.value == 100.0
        assert type_util.is_same_class_instance(class_=float, instance=number_1.value)
        assert number_1._variable_name_suffix == "test_number"

        number_1 = ap.Number(value=100.5)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"var {number_1.variable_name} = 100.5;"
        assert expected in expression

        number_2 = ap.Number(value=number_1)
        expression = expression_data_util.get_current_expression()
        expected = f"var {number_2.variable_name} = {number_1.variable_name};"
        assert expected in expression

        testing_helper.assert_raises(
            expected_error_class=ValueError, callable_=ap.Number, value="Hello!"
        )

    @apply_test_settings()
    def test_value(self) -> None:
        expression_data_util.empty_expression()
        number_1: ap.Number = ap.Number(value=100.5)
        number_1.value = 200.5
        assert number_1.value == 200.5

        number_1.value = 200
        assert type_util.is_same_class_instance(class_=float, instance=number_1.value)

        number_1.value = 300.5
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{number_1.variable_name} = 300.5;"
        assert expected in expression

        with pytest.raises(ValueError):  # type: ignore
            number_1.value = "Hello!"  # type: ignore

        number_2: ap.Number = ap.Number(value=400.5)
        number_2.value = number_1
        expression = expression_data_util.get_current_expression()
        expected = f"{number_2.variable_name} = {number_1.variable_name};"
        assert expected in expression

    def test___add__(self) -> None:
        number_1: ap.Number = ap.Number(value=10.5)
        number_2: ap.Number = number_1 + 20.6
        assert number_2.value == 31.1

    @apply_test_settings()
    def test_set_value_and_skip_expression_appending(self) -> None:
        expression_data_util.empty_expression()
        number_1: ap.Number = ap.Number(value=10.5)
        number_1._set_value_and_skip_expression_appending(value=20.5)
        assert number_1.value == 20.5
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{number_1.variable_name} = 20.5;"
        assert expected not in expression

        number_2: ap.Number = ap.Number(value=30.5)
        number_2._set_value_and_skip_expression_appending(value=number_1)
        assert number_2.value == 20.5
        expression = expression_data_util.get_current_expression()
        expected = f"{number_2.variable_name} = {number_1.variable_name};"
        assert expected not in expression

    @apply_test_settings()
    def test___repr__(self) -> None:
        number_1: ap.Number = ap.Number(value=10.5)
        repr_str: str = repr(number_1)
        assert repr_str == "Number(10.5)"

        del number_1._value
        assert repr(number_1) == "Number(0)"


class TestFloat:
    def test_top_level_import(self) -> None:
        assert ap.Float == ap.Number
        float_val_1: ap.Float = ap.Float(value=10.5)
        float_val_2: ap.Float = ap.Float(value=10.5)
        assert float_val_1 == float_val_2
