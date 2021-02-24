from random import randint

import pytest
from retrying import retry

from apyscript.type.number_value_interface import NumberValueInterface
from tests import testing_helper
from apyscript.expression import expression_file_util
from apyscript.type.int import Int


class TestNumberValueInterface:

    def test___init__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(value=100)
        testing_helper.assert_attrs(
            expected_attrs={
                '_initial_value': 100,
                '_value': 100,
            },
            any_obj=interface_1)

        interface_2: NumberValueInterface = NumberValueInterface(
            value=interface_1)
        testing_helper.assert_attrs(
            expected_attrs={
                '_initial_value': interface_1,
                '_value': 100,
            },
            any_obj=interface_2)

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=NumberValueInterface,
            kwargs={'value': 'Hello!'})

    def test_value(self) -> None:
        interface: NumberValueInterface = NumberValueInterface(value=100)
        interface.value = 200
        assert interface.value == 200

        with pytest.raises(ValueError):  # type: ignore
            interface.value = 'Hello!'

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_append_constructor_expression(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(value=100)
        interface_1.variable_name = 'test_number_value_interface_1'
        interface_1.append_constructor_expression()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            'var test_number_value_interface_1 = 100;'
        )
        assert expected in expression

        interface_2: NumberValueInterface = NumberValueInterface(
            value=interface_1)
        interface_2.variable_name = 'test_number_value_interface_2'
        interface_2.append_constructor_expression()
        expression = expression_file_util.get_current_expression()
        expected: str = (
            'var test_number_value_interface_2 = '
            'test_number_value_interface_1'
        )
        assert expected in expression
