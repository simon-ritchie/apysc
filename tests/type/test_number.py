from random import randint

import pytest
from retrying import retry

from apysc import Number
from apysc._expression import expression_file_util
from apysc.type import type_util
from tests import testing_helper


class TestNumber:

    expression_file_util.remove_expression_file()

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        expression_file_util.remove_expression_file()
        number_1: Number = Number(value=100)
        assert number_1.value == 100.0
        assert type_util.is_same_class_instance(
            class_=float, instance=number_1.value)

        number_1 = Number(value=100.5)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {number_1.variable_name} = 100.5;'
        )
        assert expected in expression

        number_2 = Number(value=number_1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'var {number_2.variable_name} = {number_1.variable_name};'
        )
        assert expected in expression

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=Number,
            kwargs={'value': 'Hello!'})

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        expression_file_util.remove_expression_file()
        number_1: Number = Number(value=100.5)
        number_1.value = 200.5
        assert number_1.value == 200.5

        number_1.value = 200
        assert type_util.is_same_class_instance(
            class_=float, instance=number_1.value)

        number_1.value = 300.5
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{number_1.variable_name} = 300.5;'
        )
        assert expected in expression

        with pytest.raises(ValueError):  # type: ignore
            number_1.value = 'Hello!'  # type: ignore

        number_2: Number = Number(value=400.5)
        number_2.value = number_1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{number_2.variable_name} = {number_1.variable_name};'
        )
        assert expected in expression

    def test___add__(self) -> None:
        number_1: Number = Number(value=10.5)
        number_2: Number = number_1 + 20.6
        assert number_2.value == 31.1

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_set_value_and_skip_expression_appending(self) -> None:
        expression_file_util.remove_expression_file()
        number_1: Number = Number(value=10.5)
        number_1.set_value_and_skip_expression_appending(value=20.5)
        assert number_1.value == 20.5
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{number_1.variable_name} = 20.5;'
        )
        assert expected not in expression

        number_2: Number = Number(value=30.5)
        number_2.set_value_and_skip_expression_appending(value=number_1)
        assert number_2.value == 20.5
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{number_2.variable_name} = {number_1.variable_name};'
        )
        assert expected not in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        number_1: Number = Number(value=10.5)
        repr_str: str = repr(number_1)
        assert repr_str == 'Number(10.5)'
