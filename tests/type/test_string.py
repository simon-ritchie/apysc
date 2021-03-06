from apyscript.expression import expression_file_util
from random import randint
from typing import Any, Dict

from retrying import retry

from apyscript.type import String
from tests import testing_helper


class TestString:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__get_str_value(self) -> None:
        string_1: String = String('Hello!')
        value: str = string_1._get_str_value(value='World!')
        assert value == 'World!'
        value = string_1._get_str_value(value=string_1)
        assert value == 'Hello!'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=String,
            kwargs={'value': 100})

        string_1: String = String(value='Hello!')
        expected_attrs: Dict[str, Any] = {
            '_initial_value': 'Hello!',
            '_value': 'Hello!',
            '_type_name': 'string',
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs,
            any_obj=string_1)
        assert string_1.variable_name.startswith('string_')

        string_2: String = String(value=string_1)
        assert string_2._value == 'Hello!'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        string_1: String = String(value='Hello!')
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {string_1.variable_name} = "Hello!";'
        )
        assert expected in expression

        string_2: String = String(value=string_1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'var {string_2.variable_name} = {string_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_value(self) -> None:
        string_1: String = String(value='Hello!')
        string_1.value = 'World!'
        assert string_1.value == 'World!'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_value_setter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        string_1: String = String(value='Hello!')
        string_1.value = 'World!'
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{string_1.variable_name} = "World!";'
        )
        assert expected in expression

        string_2: String = String(value='')
        string_2.value = string_1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{string_2.variable_name} = {string_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___add__(self) -> None:
        string_1: String = String(value='Hello')
        string_2: String = string_1 + ' World!'
        assert string_2._value == 'Hello World!'

        string_3: String = String(value=' apyscript!')
        string_4: String = string_1 + string_3
        assert string_4._value == 'Hello apyscript!'
