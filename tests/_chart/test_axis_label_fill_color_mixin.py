import apysc as ap
from apysc._chart.axis_label_fill_color_mixin import AxisLabelFillColorMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAxisLabelFillColorMixIn:
    @apply_test_settings()
    def test__set_initial_axis_label_fill_color(self) -> None:
        mixin: AxisLabelFillColorMixIn = AxisLabelFillColorMixIn()
        mixin._set_initial_axis_label_fill_color(
            axis_label_fill_color="#0af",
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._axis_label_fill_color == ap.String("#00aaff")
        assert mixin._axis_label_fill_color._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_axis_label_fill_color(
            axis_label_fill_color=ap.String(
                "#00aaff", variable_name_suffix="test_suffix_2"
            )
        )
        assert mixin._axis_label_fill_color == ap.String("#00aaff")
        assert mixin._axis_label_fill_color._variable_name_suffix == "test_suffix_2"
