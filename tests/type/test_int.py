import pytest

from apyscript.type.int import Int
from tests import testing_helper


class TestInt:

    def test___init__(self) -> None:
        int_val: Int = Int(value=100.5)
        assert int_val.value == 100
        assert int_val.variable_name.startswith('int_')

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=Int,
            kwargs={'value': 'Hello!'})

    def test_value(self) -> None:
        int_val: Int = Int(value=100)
        int_val.value = 200.5  # type: ignore
        int_val.value == 200

        with pytest.raises(ValueError):  # type: ignore
            int_val.value = 'Hello!'
