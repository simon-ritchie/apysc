from random import randint

from retrying import retry

from apysc._testing.testing_helper import assert_raises
from apysc._type.py_builtin_iter_disabling_mixin import PyBuiltInIterDisablingMixIn


class TestPyBuiltInIterDisablingMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___iter__(self) -> None:
        mixin: PyBuiltInIterDisablingMixIn = PyBuiltInIterDisablingMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin.__iter__,
            match="does not support Python's built-in iteration"
        )
