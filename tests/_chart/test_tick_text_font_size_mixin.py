import apysc as ap
from apysc._chart.tick_text_font_size_mixin import TickTextFontSizeMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestTickTextFontSizeMixIn:
    @apply_test_settings()
    def test__set_initial_tick_text_font_size(self) -> None:
        mixin: TickTextFontSizeMixIn = TickTextFontSizeMixIn()
        mixin._set_initial_tick_text_font_size(
            tick_text_font_size=20,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._tick_text_font_size == ap.Int(20)
        assert mixin._tick_text_font_size._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_tick_text_font_size(
            tick_text_font_size=ap.Int(30, variable_name_suffix="test_suffix_2")
        )
        assert mixin._tick_text_font_size == ap.Int(30)
        assert mixin._tick_text_font_size._variable_name_suffix == "test_suffix_2"
