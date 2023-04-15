import apysc as ap
from apysc._chart.axis_line_thickness_mixin import AxisLineThicknessMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAxisLineThicknessMixIn:
    @apply_test_settings()
    def test__set_initial_line_thickness(self) -> None:
        mixin: AxisLineThicknessMixIn = AxisLineThicknessMixIn()
        mixin._set_initial_line_thickness(
            line_thickness=3,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._line_thickness == ap.Int(3)
        assert mixin._line_thickness._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_line_thickness(
            line_thickness=ap.Int(5, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._line_thickness == ap.Int(5)
        assert mixin._line_thickness._variable_name_suffix == "test_suffix_2"
