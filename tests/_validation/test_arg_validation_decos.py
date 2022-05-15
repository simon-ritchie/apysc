from random import randint

from retrying import retry

from apysc._validation import arg_validation_decos
from apysc._testing.testing_helper import assert_raises

@arg_validation_decos.not_empty_string(arg_name='a')
def _test_func_1(a: str) -> None:
    ...


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_not_empty_string() -> None:
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func_1,
        kwargs={'a': ''})
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func_1,
        kwargs={'a': 10})

    _test_func_1('Hello')
    _test_func_1(a='Hello')
