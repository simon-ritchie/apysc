from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises


class TestInitializeWithBaseValueInterface:
    @apply_test_settings()
    def test__initialize_with_base_value(self) -> None:
        assert_raises(
            expected_error_class=NotImplementedError,
            callable_=(
                InitializeWithBaseValueInterface._initialize_with_base_value
            ),
        )
