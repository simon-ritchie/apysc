from random import randint

from retrying import retry

from apyscript.type import Array
from tests import testing_helper


class TestArray:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__validate_acceptable_value_type(self) -> None:
        array_1: Array = Array([1, 2, 3])
        _: Array = Array((1, 2, 3))
        _: Array = Array(array_1)

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=Array,
            kwargs={'value': 100})
