import apysc as ap
from apysc._chart.axis_label_font_size_mixin import AxisLabelFontSizeMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAxisLabelFontSizeMixIn:
    @apply_test_settings()
    def test__set_initial_axis_label_font_size(self) -> None:
        mixin: AxisLabelFontSizeMixIn = AxisLabelFontSizeMixIn()
        mixin._set_initial_axis_label_font_size(
            axis_label_font_size=20,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._axis_label_font_size == ap.Int(20)
        assert mixin._axis_label_font_size._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_axis_label_font_size(
            axis_label_font_size=ap.Int(25, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._axis_label_font_size == ap.Int(25)
        assert mixin._axis_label_font_size._variable_name_suffix == "test_suffix_2"
