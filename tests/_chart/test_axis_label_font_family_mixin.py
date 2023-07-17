import apysc as ap
from apysc._chart.axis_label_font_family_mixin import AxisLabelFontFamilyMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAxisLabelFontFamilyMixIn:
    @apply_test_settings()
    def test__set_initial_axis_label_font_family(self) -> None:
        mixin: AxisLabelFontFamilyMixIn = AxisLabelFontFamilyMixIn()
        mixin._set_initial_axis_label_font_family(
            axis_label_font_family=["Impact", "Helvetica"],
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._axis_label_font_family == ap.Array(
            [ap.String("Impact"), ap.String("Helvetica")]
        )
        if mixin._axis_label_font_family is not None:
            assert (
                mixin._axis_label_font_family._variable_name_suffix == "test_suffix_1"
            )

        mixin._set_initial_axis_label_font_family(
            axis_label_font_family=ap.Array(
                [ap.String("Helvetica"), ap.String("Impact")],
                variable_name_suffix="test_suffix_2",
            ),
        )
        assert mixin._axis_label_font_family == ap.Array(
            [ap.String("Helvetica"), ap.String("Impact")]
        )
        if mixin._axis_label_font_family is not None:
            assert (
                mixin._axis_label_font_family._variable_name_suffix == "test_suffix_2"
            )
