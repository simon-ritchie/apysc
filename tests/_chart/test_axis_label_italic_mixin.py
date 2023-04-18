import apysc as ap
from apysc._chart.axis_label_italic_mixin import AxisLabelItalicMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAxisLabelItalicMixIn:
    @apply_test_settings()
    def test__set_initial_axis_label_italic(self) -> None:
        mixin: AxisLabelItalicMixIn = AxisLabelItalicMixIn()
        mixin._set_initial_axis_label_italic(
            axis_label_italic=True,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._axis_label_italic == ap.Boolean(True)
        assert mixin._axis_label_italic._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_axis_label_italic(
            axis_label_italic=ap.Boolean(False, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._axis_label_italic == ap.Boolean(False)
        assert mixin._axis_label_italic._variable_name_suffix == "test_suffix_2"
