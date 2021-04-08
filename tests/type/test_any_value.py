from random import randint

from retrying import retry

from apysc import AnyValue
from apysc.expression import expression_file_util
from apysc.expression import var_names


class TestAnyValue:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        any_value: AnyValue = AnyValue(100)
        assert any_value._value == 100
        assert any_value.variable_name.startswith(var_names.ANY)
