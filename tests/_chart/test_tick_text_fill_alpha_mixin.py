import apysc as ap
from apysc._chart.tick_text_fill_alpha_mixin import TickTextFillAlphaMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestTickTextFillAlphaMixIn:
    @apply_test_settings()
    def test__set_initial_tick_text_fill_alpha(self) -> None:
        mixin: TickTextFillAlphaMixIn = TickTextFillAlphaMixIn()
        mixin._set_initial_tick_text_fill_alpha(
            tick_text_fill_alpha=0.3,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._tick_text_fill_alpha == ap.Number(0.3)
        assert mixin._tick_text_fill_alpha._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_tick_text_fill_alpha(
            tick_text_fill_alpha=ap.Number(0.5, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._tick_text_fill_alpha == ap.Number(0.5)
        assert mixin._tick_text_fill_alpha._variable_name_suffix == "test_suffix_2"
