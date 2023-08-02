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
            background_fill_color=ap.Color("#333"),
        )
        assert mixin._background_fill_color == ap.Color("#333333")
