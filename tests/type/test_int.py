from random import randint

import pytest
from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.type.int import Int
from tests import testing_helper


class TestInt:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        expression_file_util.remove_expression_file()
        int_val_1: Int = Int(value=100.5)
        assert int_val_1.value == 100
        assert int_val_1.variable_name.startswith('int_')

        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {int_val_1.variable_name} = 100;'
        )
        assert expected in expression

        int_val_2: Int = Int(value=int_val_1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'var {int_val_2.variable_name} = {int_val_1.variable_name};'
        )
        assert expected in expression

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=Int,
            kwargs={'value': 'Hello!'})

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_value(self) -> None:
        expression_file_util.remove_expression_file()
        int_val_1: Int = Int(value=100)
        int_val_1.value = 200.5  # type: ignore
        assert int_val_1.value == 200

        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{int_val_1.variable_name} = 200;'
        )
        assert expected in expression

        with pytest.raises(ValueError):  # type: ignore
            int_val_1.value = 'Hello!'  # type: ignore

        int_val_2: Int = Int(value=100)
        int_val_2.value = int_val_1
        assert int_val_2.value == 200  # type: ignore
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{int_val_2.variable_name} = {int_val_1.variable_name};'
        )
