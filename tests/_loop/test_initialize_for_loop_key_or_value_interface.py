from apysc._loop.initialize_for_loop_key_or_value_interface import (
    InitializeForLoopKeyOrValueInterface,
)
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises


class TestInitializeForLoopKeyOrValueInterface:
    @apply_test_settings()
    def test__initialize_for_loop_key_or_value(self) -> None:
        assert_raises(
            expected_error_class=NotImplementedError,
            callable_=(
                InitializeForLoopKeyOrValueInterface._initialize_for_loop_key_or_value
            ),
        )
