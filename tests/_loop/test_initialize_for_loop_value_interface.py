import apysc as ap
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._loop.initialize_for_loop_value_interface import (
    InitializeForLoopValueInterface,
)


class TestInitializeForLoopValueInterface:
    @apply_test_settings()
    def test__initialize_for_loop_value(self) -> None:
        assert_raises(
            expected_error_class=NotImplementedError,
            callable_=InitializeForLoopValueInterface._initialize_for_loop_value,
        )
