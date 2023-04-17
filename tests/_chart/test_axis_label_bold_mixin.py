import apysc as ap
from apysc._chart.axis_label_bold_mixin import AxisLabelBoldMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAxisLabelBoldMixIn:
    @apply_test_settings()
    def test__set_initial_axis_label_bold(self) -> None:
        mixin: AxisLabelBoldMixIn = AxisLabelBoldMixIn()
        mixin._set_initial_axis_label_bold(
            axis_label_bold=True,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._axis_label_bold == ap.Boolean(True)
        assert mixin._axis_label_bold._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_axis_label_bold(
            axis_label_bold=ap.Boolean(False, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._axis_label_bold == ap.Boolean(False)
        assert mixin._axis_label_bold._variable_name_suffix == "test_suffix_2"
