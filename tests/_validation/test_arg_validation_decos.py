from random import randint

from retrying import retry

from apysc._testing.testing_helper import assert_raises
from apysc._validation import arg_validation_decos


@arg_validation_decos.not_empty_string(  # type: ignore[misc]
    arg_position_index=0, arg_name='a')
def _test_func_1(a: str) -> None:
    ...


class _TestClass1:

    @arg_validation_decos.not_empty_string(  # type: ignore[misc]
        arg_position_index=2, arg_name='a')
    def _test_method_1(self, *, a: str) -> None:
        ...

    @arg_validation_decos.not_empty_string(  # type: ignore[misc]
        arg_position_index=1, arg_name='a')
    def _test_method_2(self, a: str) -> None:
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

    test_instance: _TestClass1 = _TestClass1()
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=test_instance._test_method_1,
        kwargs={'a': ''})
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=test_instance._test_method_2,
        kwargs={'a': ''})

    test_instance._test_method_1(a='Hello')
    test_instance._test_method_2(a='Hello')
    test_instance._test_method_2('Hello')
