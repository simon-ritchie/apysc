from random import randint

import pytest
from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from apysc._expression import var_names
from tests import testing_helper


class TestInt:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        expression_file_util.remove_expression_file()
        int_val_1: ap.Int = ap.Int(value=100.5)
        assert int_val_1.value == 100
        assert int_val_1.variable_name.startswith(f'{var_names.INT}_')

        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {int_val_1.variable_name} = 100;'
        )
        assert expected in expression

        int_val_2: ap.Int = ap.Int(value=int_val_1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'var {int_val_2.variable_name} = {int_val_1.variable_name};'
        )
        assert expected in expression

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=ap.Int,
            kwargs={'value': 'Hello!'})

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        expression_file_util.remove_expression_file()
        int_val_1: ap.Int = ap.Int(value=100)
        int_val_1.value = 200.5  # type: ignore
        assert int_val_1.value == 200

        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{int_val_1.variable_name} = 200;'
        )
        assert expected in expression

        with pytest.raises(ValueError):  # type: ignore
            int_val_1.value = 'Hello!'  # type: ignore

        int_val_2: ap.Int = ap.Int(value=100)
        int_val_2.value = int_val_1
        assert int_val_2.value == 200  # type: ignore
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{int_val_2.variable_name} = {int_val_1.variable_name};'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___add__(self) -> None:
        int_1: ap.Int = ap.Int(value=10)
        int_2: ap.Int = int_1 + 10.5
        assert int_2.value == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_set_value_and_skip_expression_appending(self) -> None:
        expression_file_util.remove_expression_file()
        int_1: ap.Int = ap.Int(value=10)
        int_1._set_value_and_skip_expression_appending(value=20.5)
        assert int_1.value == 20
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{int_1.variable_name} = 20;'
        )
        assert expected not in expression

        int_2: ap.Int = ap.Int(value=30)
        int_2._set_value_and_skip_expression_appending(value=int_1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{int_2.variable_name} = {int_1.variable_name};'
        )
        assert expected not in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_cast_expression(self) -> None:
        expression_file_util.remove_expression_file()
        int_val: ap.Int = ap.Int(value=ap.Number(value=100.5))
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{int_val.variable_name} = '
            f'parseInt({int_val.variable_name}, 10);'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        int_val = ap.Int(value=100)
        expression = expression_file_util.get_current_expression()
        assert 'parseInt' not in expression

        expression_file_util.remove_expression_file()
        int_val = ap.Int(value=100.5)
        expression = expression_file_util.get_current_expression()
        assert 'parseInt' not in expression
        expected = f'{int_val.variable_name} = 100;'
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        int_1: ap.Int = ap.Int(3)
        repr_str: str = repr(int_1)
        assert repr_str == 'Int(3)'
