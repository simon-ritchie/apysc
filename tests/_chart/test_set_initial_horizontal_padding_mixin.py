import apysc as ap
from apysc._chart.set_initial_horizontal_padding_mixin import SetInitialHorizontalPaddingMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialHorizontalPaddingMixIn:
    @apply_test_settings()
    def test__set_initial_horizontal_padding(self) -> None:
        mixin: SetInitialHorizontalPaddingMixIn = SetInitialHorizontalPaddingMixIn()
        mixin._set_initial_horizontal_padding(
            horizontal_padding=10, variable_name_suffix="test_suffix_1"
        )
        assert mixin._horizontal_padding == ap.Int(10)
        assert mixin._horizontal_padding._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_horizontal_padding(
            horizontal_padding=ap.Int(20, variable_name_suffix="test_suffix_2")
        )
        assert mixin._horizontal_padding == ap.Int(20)
        assert mixin._horizontal_padding._variable_name_suffix == "test_suffix_2"
