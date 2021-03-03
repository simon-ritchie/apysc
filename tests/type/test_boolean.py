from random import randint
from typing import Any, Dict

from retrying import retry

from apyscript.type import Int
from apyscript.type import Boolean
from apyscript.expression import expression_file_util
from tests import testing_helper


class TestBoolean:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
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
        expected_attrs: Dict[str, Any] = {
            '_initial_value': boolean_1,
            '_value': True,
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs, any_obj=boolean_2)

        boolean_3: Boolean = Boolean(value=False)
        assert not boolean_3._value

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
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
