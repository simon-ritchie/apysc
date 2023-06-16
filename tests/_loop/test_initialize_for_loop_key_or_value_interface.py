from apysc._loop.initialize_for_loop_key_or_value_interface import (
    InitializeForLoopValueInterface,
)
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises


class TestInitializeForLoopValueInterface:
    @apply_test_settings()
    def test__initialize_for_loop_value(self) -> None:
        assert_raises(
            expected_error_class=NotImplementedError,
            callable_=InitializeForLoopValueInterface._initialize_for_loop_value,
        )
