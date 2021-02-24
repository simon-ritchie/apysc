from random import randint

import pytest
from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.type.number_value_interface import NumberValueInterface
from tests import testing_helper


class TestNumberValueInterface:

    def test___init__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=100, type_name='test_interface')
        testing_helper.assert_attrs(
            expected_attrs={
                '_initial_value': 100,
                '_value': 100,
                '_type_name': 'test_interface',
            },
            any_obj=interface_1)

        interface_2: NumberValueInterface = NumberValueInterface(
            value=interface_1, type_name='test_interface')
        testing_helper.assert_attrs(
            expected_attrs={
                '_initial_value': interface_1,
                '_value': 100,
            },
            any_obj=interface_2)

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=NumberValueInterface,
            kwargs={'value': 'Hello!', 'type_name': 'test_interface'})

    def test_value(self) -> None:
        expression_file_util.remove_expression_file()
        interface: NumberValueInterface = NumberValueInterface(
            value=100, type_name='test_interface')
        interface.variable_name = 'test_number_value_interface'
        interface.value = 200
        assert interface.value == 200

        with pytest.raises(ValueError):  # type: ignore
            interface.value = 'Hello!'  # type: ignore

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=100, type_name='test_interface')
        interface_1.variable_name = 'test_number_value_interface_1'
        interface_1.append_constructor_expression()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            'var test_number_value_interface_1 = 100;'
        )
        assert expected in expression

        interface_2: NumberValueInterface = NumberValueInterface(
            value=interface_1, type_name='test_interface')
        interface_2.variable_name = 'test_number_value_interface_2'
        interface_2.append_constructor_expression()
        expression = expression_file_util.get_current_expression()
        expected = (
            'var test_number_value_interface_2 = '
            'test_number_value_interface_1'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_append_value_setter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=100, type_name='test_interface')
        interface_1.variable_name = 'test_number_value_interface_1'
        interface_1.value = 200
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name} = 200;'
        )
        assert expected in expression

        interface_2: NumberValueInterface = NumberValueInterface(
            value=100, type_name='test_interface')
        interface_2.variable_name = 'test_number_value_interface_2'
        interface_2.value = interface_1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{interface_2.variable_name} = {interface_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_type_name(self) -> None:
        interface: NumberValueInterface = NumberValueInterface(
            value=100, type_name='test_interface')
        assert interface.type_name == 'test_interface'

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___add__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = interface_1 + 20
        assert interface_2.value == 30
        assert interface_1.variable_name != interface_2.variable_name

        interface_3: NumberValueInterface = interface_1 + interface_2
        assert interface_3.value == 40
        assert interface_3.variable_name != interface_2.variable_name
