import apysc as ap
from apysc._chart.set_initial_vertical_padding_mixin import SetInitialVerticalPaddingMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialVerticalPaddingMixIn:
    @apply_test_settings()
    def test__set_initial_vertical_padding(self) -> None:
        mixin: SetInitialVerticalPaddingMixIn = SetInitialVerticalPaddingMixIn()
        mixin._set_initial_vertical_padding(
            vertical_padding=10, variable_name_suffix="test_suffix_1"
        )
        assert mixin._vertical_padding == ap.Int(10)
        assert mixin._vertical_padding._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_vertical_padding(
            vertical_padding=ap.Int(20, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._vertical_padding == ap.Int(20)
        assert mixin._vertical_padding._variable_name_suffix == "test_suffix_2"
