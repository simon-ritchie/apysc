import apysc as ap
from apysc._chart.set_initial_background_fill_color_mixin import (
    SetInitialBackgroundFillColorMixIn,
)
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialBackgroundColorMixIn:
    @apply_test_settings()
    def test__set_initial_background_color(self) -> None:
        mixin: SetInitialBackgroundFillColorMixIn = SetInitialBackgroundFillColorMixIn()
        mixin._set_initial_background_fill_color(
            background_fill_color="#333",
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._background_fill_color == ap.String("#333333")
        assert mixin._background_fill_color._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_background_fill_color(
            background_fill_color=ap.String(
                "#555",
                variable_name_suffix="test_suffix_2",
            ),
        )
        assert mixin._background_fill_color == ap.String("#555555")
        assert mixin._background_fill_color._variable_name_suffix == "test_suffix_2"
