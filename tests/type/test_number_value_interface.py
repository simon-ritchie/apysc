import re
from random import randint
from typing import Any, Match
from typing import Optional

import pytest
from retrying import retry

from apysc import Boolean
from apysc import Int
from apysc import Number
from apysc.expression import expression_file_util
from apysc.type.number_value_interface import NumberValueInterface
from apysc.expression import var_names
from tests import testing_helper


class TestNumberValueInterface:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=100, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        testing_helper.assert_attrs(
            expected_attrs={
                '_initial_value': 100,
                '_value': 100,
                '_type_name': 'test_interface',
            },
            any_obj=interface_1)

        interface_2: NumberValueInterface = NumberValueInterface(
            value=interface_1, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_value(self) -> None:
        expression_file_util.remove_expression_file()
        interface: NumberValueInterface = NumberValueInterface(
            value=100, type_name='test_interface')
        interface.variable_name = 'test_number_value_interface'
        interface.value = 200
        assert interface.value == 200

        with pytest.raises(ValueError):  # type: ignore
            interface.value = 'Hello!'  # type: ignore

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_type_name(self) -> None:
        interface: NumberValueInterface = NumberValueInterface(
            value=100, type_name='test_interface')
        assert interface.type_name == 'test_interface'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__copy(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1._copy()
        assert interface_1.value == interface_2.value
        assert interface_1.variable_name != interface_2.variable_name
        assert interface_2.variable_name.startswith('test_interface')

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___sub__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=20, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 - 15
        assert interface_2.value == 5

        interface_3: NumberValueInterface = interface_1 - interface_2
        assert interface_3.value == 15

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___mul__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=20, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 * 3
        assert interface_2.value == 60

        interface_3: NumberValueInterface = interface_1 * interface_2
        assert interface_3.value == 1200

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___truediv__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = interface_1 / 4
        assert interface_2.value == 2.5
        assert isinstance(interface_2, Number)

        interface_3: NumberValueInterface = interface_2 / interface_1
        assert interface_3.value == 0.25

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___iadd__(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        int_1: Int = Int(5)
        interface_1 += int_1
        assert interface_1.value == 15
        assert interface_1.variable_name == 'test_interface_0'

        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r'test_interface_[0-9]+ = test_interface_0 \+ '
                rf'{int_1.variable_name};'
                r'\ntest_interface_0 = test_interface_[0-9]+;'
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL)
        assert match is not None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___isub__(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_1 -= 3
        assert interface_1.value == 7
        assert interface_1.variable_name == 'test_interface_0'

        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r'test_interface_[0-9]+ = test_interface_0 - 3;'
                r'\ntest_interface_0 = test_interface_[0-9]+;'
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL)
        assert match is not None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___imul__(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_1 *= 3
        assert interface_1.value == 30
        assert interface_1.variable_name == 'test_interface_0'

        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r'test_interface_[0-9]+ = test_interface_0 \* 3;'
                r'\ntest_interface_0 = test_interface_[0-9]+;'
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        print(expression)
        assert match is not None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___itruediv__(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_1 /= 4
        assert interface_1.value == 2.5
        assert interface_1.variable_name == 'test_interface_0'

        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r'var n_[0-9]+ = test_interface_0;'
                r'\nn_[0-9]+ = n_[0-9]+ / 4;'
                r'\ntest_interface_0 = n_[0-9]+;'),
            string=expression,
            flags=re.MULTILINE | re.DOTALL)
        assert match is not None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___str__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        assert str(interface_1) == '10'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___eq__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_0'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2.variable_name = 'test_interface_1'
        interface_3: NumberValueInterface = NumberValueInterface(
            value=11, type_name='test_interface')
        interface_3.variable_name = 'test_interface_3'

        assert interface_1 == 10
        assert interface_1 == interface_2
        assert not interface_1 == 11
        assert not interface_1 == interface_3

        assert isinstance(interface_1 == 10, Boolean)
        assert isinstance(interface_1 == interface_2, Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___ne__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=11, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
        assert interface_1 != 11
        assert interface_1 != interface_2

        assert isinstance(interface_1 != 11, Boolean)
        assert isinstance(interface_1 != interface_2, Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___lt__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=11, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
        interface_3: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_3.variable_name = 'test_interface_3'

        assert interface_1 < 11
        assert interface_1 < interface_2
        assert not interface_1 < 10
        assert not interface_1 < interface_3
        assert isinstance(interface_1 < 11, Boolean)
        assert isinstance(interface_1 < interface_2, Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___le__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
        interface_3: NumberValueInterface = NumberValueInterface(
            value=11, type_name='test_interface')
        interface_3.variable_name = 'test_interface_3'
        interface_4: NumberValueInterface = NumberValueInterface(
            value=9, type_name='test_interface')
        interface_4.variable_name = 'test_interface_4'

        assert interface_1 <= 10
        assert interface_1 <= 11
        assert interface_1 <= interface_2
        assert interface_1 <= interface_3
        assert not interface_1 <= 9
        assert not interface_1 <= interface_4

        assert isinstance(interface_1 <= 10, Boolean)
        assert isinstance(interface_1 <= interface_2, Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___gt__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=9, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
        interface_3: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_3.variable_name = 'test_interface_3'

        assert interface_1 > 9
        assert interface_1 > interface_2
        assert not interface_1 > 10
        assert not interface_1 > interface_3

        assert isinstance(interface_1 > 9, Boolean)
        assert isinstance(interface_1 > interface_2, Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___ge__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
        interface_3: NumberValueInterface = NumberValueInterface(
            value=9, type_name='test_interface')
        interface_3.variable_name = 'test_interface_3'
        interface_4: NumberValueInterface = NumberValueInterface(
            value=11, type_name='test_interface')
        interface_4.variable_name = 'test_interface_4'

        assert interface_1 >= 10
        assert interface_1 >= 9
        assert interface_1 >= interface_2
        assert interface_1 >= interface_3
        assert not interface_1 >= 11
        assert not interface_1 >= interface_4

        assert isinstance(interface_1 >= 10, Boolean)
        assert isinstance(interface_1 >= interface_2, Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___int__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        integer: int = int(interface_1)
        assert interface_1 == 10
        assert isinstance(integer, int)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___float__(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10.5, type_name='test_interface')
        float_val: float = float(interface_1)
        assert float_val == 10.5
        assert isinstance(float_val, float)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__make_snapshot(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10.5, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        snapshot_name: str = 'snapshot_1'
        interface_1._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert interface_1._value_snapshots[snapshot_name] == 10.5

        interface_1.value = 20
        interface_1._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert interface_1._value_snapshots[snapshot_name] == 10.5

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__revert(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10.5, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        snapshot_name: str = 'snapshot_1'
        interface_1._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        interface_1.value = 20
        interface_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface_1.value == 10.5

        interface_1.value = 20
        interface_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface_1.value == 20

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_eq_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
        result: Boolean = interface_1 == interface_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'{interface_1.variable_name} === {interface_2.variable_name};'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        result = interface_1 == 10
        expression = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{result.variable_name} = '
                rf'{interface_1.variable_name} === '
                rf'{var_names.INT}\_.+?\;'),
            string=expression,
            flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_ne_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
        result: Boolean = interface_1 != interface_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'{interface_1.variable_name} !== '
            f'{interface_2.variable_name};'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        result = interface_1 != 20
        expression = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{result.variable_name} = '
                rf'{interface_1.variable_name} !== '
                rf'{var_names.INT}\_.+?;'
            ),
            string=expression,
            flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_lt_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
        result: Boolean = interface_1 < interface_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'{interface_1.variable_name} < {interface_2.variable_name};'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        result = interface_1 < 10
        expression = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{result.variable_name} = '
                rf'{interface_1.variable_name} \< '
                rf'{var_names.INT}\_.+;'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_le_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
        result: Boolean = interface_1 <= interface_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'{interface_1.variable_name} <= {interface_2.variable_name};'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        result = interface_1 <= 10
        expression = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{result.variable_name} = '
                rf'{interface_1.variable_name} <= '
                rf'{var_names.INT}\_.+;'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_gt_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
        result: Boolean = interface_1 > interface_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'{interface_1.variable_name} > {interface_2.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_ge_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_1.variable_name = 'test_interface_1'
        interface_2: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        interface_2.variable_name = 'test_interface_2'
        result: Boolean = interface_1 >= interface_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'{interface_1.variable_name} >= {interface_2.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__convert_other_val_to_int_or_number(self) -> None:
        interface_1: NumberValueInterface = NumberValueInterface(
            value=10, type_name='test_interface')
        converted_val: Any = interface_1._convert_other_val_to_int_or_number(
            other=10)
        assert isinstance(converted_val, Int)
        assert converted_val == 10

        converted_val = interface_1._convert_other_val_to_int_or_number(
            other=10.5)
        assert isinstance(converted_val, Number)
        assert converted_val == 10.5

        converted_val = interface_1._convert_other_val_to_int_or_number(
            other='Hello')
        assert converted_val == 'Hello'
