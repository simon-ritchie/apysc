from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.py_builtin_iter_disabling_mixin import PyBuiltInIterDisablingMixIn


class TestPyBuiltInIterDisablingMixIn:
    @apply_test_settings()
    def test___iter__(self) -> None:
        mixin: PyBuiltInIterDisablingMixIn = PyBuiltInIterDisablingMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin.__iter__,
            match="does not support Python's built-in iteration",
        )
