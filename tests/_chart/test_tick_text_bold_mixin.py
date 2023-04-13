import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._chart.tick_text_bold_mixin import TickTextBoldMixIn


class TestTickTextBoldMixIn:
    @apply_test_settings()
    def test__set_initial_tick_text_bold(self) -> None:
        mixin: TickTextBoldMixIn = TickTextBoldMixIn()
        mixin._set_initial_tick_text_bold(
            tick_text_bold=True,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._tick_text_bold == ap.Boolean(True)
        assert mixin._tick_text_bold._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_tick_text_bold(
            tick_text_bold=ap.Boolean(False, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._tick_text_bold == ap.Boolean(False)
        assert mixin._tick_text_bold._variable_name_suffix == "test_suffix_2"
