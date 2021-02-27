from random import randint
from typing import Union

import pytest
from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.type.int import Int
from apyscript.type.number import Number
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

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__copy(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1._copy()
        assert interface_1.value == interface_2.value
        assert interface_1.variable_name != interface_2.variable_name
        assert interface_2.variable_name.startswith('test_interface')

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_addition_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 + 10
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {interface_2.variable_name} = '
            f'{interface_1.variable_name} + 10;'
        )
        assert expected in expression

        interface_3: NumberValueInterface = interface_1 + interface_2
        expression = expression_file_util.get_current_expression()
        expected = (
            f'var {interface_3.variable_name} = '
            f'{interface_1.variable_name} + {interface_2.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_set_value_and_skip_expression_appending(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_1.set_value_and_skip_expression_appending(value=20)
        assert interface_1.value == 20
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name} = 20;'
        )
        assert expected not in expression

        interface_2: NumberValueInterface = NumberValueInterface(
            value=30, type_name='test_interface')
        interface_2.variable_name = 'test_interface_1'
        interface_2.set_value_and_skip_expression_appending(
            value=interface_1)
        assert interface_2.value == 20
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{interface_2.variable_name} = {interface_1.variable_name};'
        )
        assert expected not in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___sub__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=20, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 - 15
        assert interface_2.value == 5

        interface_3: NumberValueInterface = interface_1 - interface_2
        assert interface_3.value == 15

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_subtraction_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=20, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 - 15
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_2.variable_name} = {interface_1.variable_name} - 15;'
        )
        assert expected in expression

        interface_3: NumberValueInterface = interface_1 - interface_2
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{interface_3.variable_name} = {interface_1.variable_name} '
            f'- {interface_2.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__get_arithmetic_expression_right_value(self) -> None:
        interface: NumberValueInterface = NumberValueInterface(
            value=20, type_name='test_interface')
        other: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        other.variable_name = 'test_interface_0'
        right_value: Union[int, float, str] = interface.\
            _get_arithmetic_expression_right_value(other=other)
        assert right_value == 'test_interface_0'

        right_value = interface._get_arithmetic_expression_right_value(
            other=10)
        assert right_value == 10

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___mul__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=20, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 * 3
        assert interface_2.value == 60

        interface_3: NumberValueInterface = interface_1 * interface_2
        assert interface_3.value == 1200

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_multiplication_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=20, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 * 3
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_2.variable_name} = {interface_1.variable_name} * 3;'
        )
        assert expected in expression

        interface_3: NumberValueInterface = interface_1 * interface_2
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{interface_3.variable_name} = {interface_1.variable_name}'
            f' * {interface_2.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___truediv__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 / 4
        assert interface_2.value == 2.5
        assert isinstance(interface_2, Number)

        interface_3: NumberValueInterface = interface_2 / interface_1
        assert interface_3.value == 0.25

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_true_division_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 / 4
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_2.variable_name} = {interface_1.variable_name};'
            f'\n{interface_2.variable_name} = {interface_2.variable_name}'
            ' / 4;'
        )
        assert expected in expression

        interface_3: NumberValueInterface = interface_2 / interface_1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{interface_3.variable_name} = {interface_2.variable_name};'
            f'\n{interface_3.variable_name} = {interface_3.variable_name}'
            f' / {interface_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___floordiv__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 // 4
        assert interface_2.value == 2
        assert isinstance(interface_2, Int)

        interface_3: NumberValueInterface = NumberValueInterface(
            value=6, type_name='test_interface')
        interface_3.variable_name = 'test_interface_2'
        interface_4: NumberValueInterface = interface_1 // interface_3
        assert interface_4.value == 1

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_floor_division_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 // 4
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_2.variable_name} = '
            f'parseInt({interface_2.variable_name} / 4);'
        )
        assert expected in expression

        interface_3: NumberValueInterface = interface_1 // interface_2
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{interface_3.variable_name} = {interface_1.variable_name};'
        )
        assert expected in expression
        expected = (
            f'{interface_3.variable_name} = parseInt('
            f'{interface_3.variable_name} / {interface_2.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___iadd__(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_1 += 5
        assert interface_1.value == 15

        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name} = test_interface_0 + 5;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___isub__(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_1 -= 3
        assert interface_1.value == 7

        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name} = test_interface_0 - 3;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___imul__(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_1 *= 3
        assert interface_1.value == 30

        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name} = test_interface_0 * 3;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___itruediv__(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_1 /= 4
        assert interface_1.value == 2.5

        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name} = {interface_1.variable_name} / 4;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___str__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        assert str(interface_1) == '10'

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___eq__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_3: NumberValueInterface = NumberValueInterface(
            value=11, type_name='test_interface')

        assert interface_1 == 10
        assert interface_1 == interface_2
        assert interface_1 != 11
        assert interface_1 != interface_3

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___lt__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2: NumberValueInterface = NumberValueInterface(
            value=11, type_name='test_interface')
        interface_3: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')

        assert interface_1 < 11
        assert interface_1 < interface_2
        assert not interface_1 < 10
        assert not interface_1 < interface_3

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___le__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_3: NumberValueInterface = NumberValueInterface(
            value=11, type_name='test_interface')
        interface_4: NumberValueInterface = NumberValueInterface(
            value=9, type_name='test_interface')

        assert interface_1 <= 10
        assert interface_1 <= 11
        assert interface_1 <= interface_2
        assert interface_1 <= interface_3
        assert not interface_1 <= 9
        assert not interface_1 <= interface_4


    def test___gt__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2: NumberValueInterface = NumberValueInterface(
            value=9, type_name='test_interface')
        interface_3: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')

        assert interface_1 > 9
        assert interface_1 > interface_2
        assert not interface_1 > 10
        assert not interface_1 > interface_3

    def test___ge__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_3: NumberValueInterface = NumberValueInterface(
            value=9, type_name='test_interface')
        interface_4: NumberValueInterface = NumberValueInterface(
            value=11, type_name='test_interface')

        assert interface_1 >= 10
        assert interface_1 >= 9
        assert interface_1 >= interface_2
        assert interface_1 >= interface_3
        assert not interface_1 >= 11
        assert not interface_1 >= interface_4
