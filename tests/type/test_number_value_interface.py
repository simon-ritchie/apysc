import pytest

from apyscript.type.number_value_interface import NumberValueInterface
from tests import testing_helper


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
