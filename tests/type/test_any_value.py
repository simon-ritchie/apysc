from random import randint

from retrying import retry

from apysc import AnyValue, Int
from apysc.expression import expression_file_util
from apysc.expression import var_names


class TestAnyValue:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        any_value: AnyValue = AnyValue(100)
        assert any_value._value == 100
        assert any_value.variable_name.startswith(var_names.ANY)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        any_value_1: AnyValue = AnyValue(100)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{any_value_1.variable_name} = 100;'
        )
        assert expected in expression

        int_1: Int = Int(10)
        any_value_2: AnyValue = AnyValue(int_1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{any_value_2.variable_name} = {int_1.variable_name};'
        )
        assert expected in expression
