import apysc as ap
from apysc._chart.tick_text_fill_color_mixin import TickTextFillColorMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestTickTextFillColorMixIn:
    @apply_test_settings()
    def test__set_initial_tick_text_fill_color(self) -> None:
        mixin: TickTextFillColorMixIn = TickTextFillColorMixIn()
        mixin._set_initial_tick_text_fill_color(
            tick_text_fill_color=ap.Color("#0af"),
        )
        assert mixin._tick_text_fill_color == ap.Color("#00aaff")
