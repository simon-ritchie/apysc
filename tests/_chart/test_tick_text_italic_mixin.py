import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._chart.tick_text_italic_mixin import TickTextItalicMixIn


class TestTickTextItalicMixIn:
    @apply_test_settings()
    def test__set_initial_tick_text_italic(self) -> None:
        mixin: TickTextItalicMixIn = TickTextItalicMixIn()
        mixin._set_initial_tick_text_italic(
            tick_text_italic=True,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._tick_text_italic == ap.Boolean(True)
        assert mixin._tick_text_italic._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_tick_text_italic(
            tick_text_italic=ap.Boolean(False, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._tick_text_italic == ap.Boolean(False)
        assert mixin._tick_text_italic._variable_name_suffix == "test_suffix_2"
