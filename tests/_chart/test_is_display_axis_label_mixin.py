import apysc as ap
from apysc._chart.is_display_axis_label_mixin import IsDisplayAxisLabelMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestIsDisplayAxisLabelMixIn:
    @apply_test_settings()
    def test__set_initial_is_display_axis_label(self) -> None:
        mixin: IsDisplayAxisLabelMixIn = IsDisplayAxisLabelMixIn()
        mixin._set_initial_is_display_axis_label(
            is_display_axis_label=True,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._is_display_axis_label == ap.Boolean(True)
        assert mixin._is_display_axis_label._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_is_display_axis_label(
            is_display_axis_label=ap.Boolean(
                False,
                variable_name_suffix="test_suffix_2",
            ),
        )
        assert mixin._is_display_axis_label == ap.Boolean(False)
        assert mixin._is_display_axis_label._variable_name_suffix == "test_suffix_2"
