import apysc as ap
from apysc._chart.set_initial_border_color_mixin import SetInitialBorderColorMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialBorderColorMixIn:
    @apply_test_settings()
    def test__set_initial_border_color(self) -> None:
        mixin: SetInitialBorderColorMixIn = SetInitialBorderColorMixIn()
        mixin._set_initial_border_color(
            border_color=ap.Color("#333"),
        )
        assert mixin._border_color == ap.Color("#333333")
