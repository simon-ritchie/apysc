from random import randint
from typing import Any
from typing import Dict

from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.type import Boolean
from apyscript.type import Int
from tests import testing_helper


class TestBoolean:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        boolean_1: Boolean = Boolean(value=Int(1))
        expected_attrs: Dict[str, Any] = {
            '_initial_value': Int(1),
            '_value': True,
            '_type_name': 'boolean',
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs, any_obj=boolean_1)
        assert boolean_1.variable_name.startswith('boolean_')

        boolean_2: Boolean = Boolean(value=boolean_1)
        expected_attrs = {
            '_initial_value': boolean_1,
            '_value': True,
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs, any_obj=boolean_2)

        boolean_3: Boolean = Boolean(value=False)
        assert not boolean_3._value

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        int_1: Int = Int(1)
        boolean_1: Boolean = Boolean(value=int_1)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{boolean_1.variable_name} = Boolean({int_1.variable_name});'
        )
        assert expected in expression

        boolean_2: Boolean = Boolean(value=True)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{boolean_2.variable_name} = true;'
        )
        assert expected in expression

        boolean_3: Boolean = Boolean(value=False)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{boolean_3.variable_name} = false;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__get_bool_from_arg_value(self) -> None:
        boolean_1: Boolean = Boolean(value=1)
        result: bool = boolean_1._get_bool_from_arg_value(value=1)
        assert result
        result = boolean_1._get_bool_from_arg_value(value=0)
        assert not result
        boolean_2: Boolean = Boolean(value=0)
        result = boolean_1._get_bool_from_arg_value(value=boolean_2)
        assert not result
        result = boolean_1._get_bool_from_arg_value(value=True)
        assert result

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=boolean_1._get_bool_from_arg_value,
            kwargs={'value': 'Hello!'})

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__set_value_and_skip_expression_appending(self) -> None:
        expression_file_util.remove_expression_file()
        boolean_1: Boolean = Boolean(value=1)
        boolean_1._set_value_and_skip_expression_appending(value=False)
        assert not boolean_1._value
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{boolean_1.variable_name} = false;'
        )
        assert expected not in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_value_setter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        boolean_1: Boolean = Boolean(value=1)
        boolean_1.variable_name = 'test_boolean_1'
        int_1: Int = Int(1)
        boolean_1.value = int_1
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{boolean_1.variable_name} = Boolean({int_1.variable_name});'
        )
        assert expected in expression

        boolean_1.value = 1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{boolean_1.variable_name} = true;'
        )
        assert expected in expression

        boolean_1.value = 0
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{boolean_1.variable_name} = false;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_value(self) -> None:
        boolean_1: Boolean = Boolean(value=1)
        int_1: Int = Int(0)
        boolean_1.value = int_1
        assert not boolean_1.value

        boolean_1.value = 1
        assert boolean_1.value

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___bool__(self) -> None:
        boolean_1: Boolean = Boolean(1)
        assert boolean_1
        boolean_1.value = 0
        assert not boolean_1
