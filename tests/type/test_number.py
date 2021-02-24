import pytest

from apyscript.type.number import Number
from apyscript.type import type_util
from apyscript.expression import expression_file_util
from tests import testing_helper


class TestNumber:

    def test___init__(self) -> None:
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

    def test_value(self) -> None:
        number: Number = Number(value=100.5)
        number.value = 200.5
        assert number.value == 200.5

        number.value = 200
        assert type_util.is_same_class_instance(
            class_=float, instance=number.value)

        with pytest.raises(ValueError):  # type: ignore
            number.value = 'Hello!'
