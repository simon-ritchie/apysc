from random import randint

import pytest
from retrying import retry

from apyscript.type.number_value_interface import NumberValueInterface
from tests import testing_helper
from apyscript.expression import expression_file_util


class TestNumberValueInterface:

    def test___init__(self) -> None:
        interface: NumberValueInterface = NumberValueInterface(value=100)
        testing_helper.assert_attrs(
            expected_attrs={
                '_value': 100,
            },
            any_obj=interface)

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
        interface: NumberValueInterface = NumberValueInterface(value=100)
        interface.variable_name = 'test_number_value_interface'
        interface.append_constructor_expression()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            'var test_number_value_interface = 100;'
        )
        assert expected in expression
