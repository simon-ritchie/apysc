import apysc as ap
from apysc._chart.tick_text_font_family_mixin import TickTextFontFamilyMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestTickTextFontFamilyMixIn:
    @apply_test_settings()
    def test__set_initial_tick_text_font_family(self) -> None:
        ap.Stage()
        mixin: TickTextFontFamilyMixIn = TickTextFontFamilyMixIn()
        mixin._set_initial_tick_text_font_family(tick_text_font_family=None)
        value = mixin._tick_text_font_family
        assert value is None

        mixin._set_initial_tick_text_font_family(
            tick_text_font_family=["Impact", "Helvetica"],
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._tick_text_font_family == ap.Array(["Impact", "Helvetica"])
        if mixin._tick_text_font_family is not None:
            assert mixin._tick_text_font_family._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_tick_text_font_family(
            tick_text_font_family=ap.Array(
                [ap.String("Impact"), ap.String("Helvetica")],
                variable_name_suffix="test_suffix_2",
            ),
        )
        assert mixin._tick_text_font_family == ap.Array(
            [ap.String("Impact"), ap.String("Helvetica")]
        )
        if mixin._tick_text_font_family is not None:
            assert mixin._tick_text_font_family._variable_name_suffix == "test_suffix_2"
