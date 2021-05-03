from random import randint

from retrying import retry

from apysc import AnyValue
from apysc import Int
from apysc.expression import expression_file_util
from apysc.expression import var_names
from apysc.type.variable_name_interface import VariableNameInterface


class TestAnyValue:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        any_value: AnyValue = AnyValue(100)
        assert any_value._value == 100
        assert any_value.variable_name.startswith(var_names.ANY)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        any_value_1: AnyValue = AnyValue(100)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{any_value_1.variable_name} = 100;'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        int_1: Int = Int(10)
        any_value_2: AnyValue = AnyValue(int_1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{any_value_2.variable_name} = {int_1.variable_name};'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        any_value_3 = AnyValue(None)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'var {any_value_3.variable_name} = NaN;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_value_setter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(100)
        any_value.value = 200
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{any_value.variable_name} = 200;'
        )
        assert expected in expression

        int_1: Int = Int(300)
        any_value.value = int_1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{any_value.variable_name} = {int_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        any_value: AnyValue = AnyValue(100)
        any_value.value = 200
        assert any_value.value == 200

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___add__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(100)
        int_1: Int = Int(200)
        result: VariableNameInterface = any_value + int_1
        assert isinstance(result, AnyValue)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {result.variable_name} = {any_value.variable_name} + '
            f'{int_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___sub__(self) -> None:
        expression_file_util.remove_expression_file()
        any_value: AnyValue = AnyValue(100)
        int_1: Int = Int(200)
        result: VariableNameInterface = any_value - int_1
        assert isinstance(result, AnyValue)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {result.variable_name} = {any_value.variable_name} - '
            f'{int_1.variable_name};'
        )
        assert expected in expression
