import apysc as ap
from apysc._chart.x_axis_column_name_mixin import XAxisColumnNameMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestXAxisSettings:
    @apply_test_settings()
    def test__set_initial_x_axis_column_name(self) -> None:
        mixin: XAxisColumnNameMixIn = XAxisColumnNameMixIn()
        mixin._set_initial_x_axis_column_name(
            x_axis_column_name="test_column_1",
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._x_axis_column_name == ap.String("test_column_1")
        assert mixin._x_axis_column_name._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_x_axis_column_name(
            x_axis_column_name=ap.String(
                value="test_column_2",
                variable_name_suffix="test_suffix_2",
            ),
        )
        assert mixin._x_axis_column_name == ap.String("test_column_2")
        assert mixin._x_axis_column_name._variable_name_suffix == "test_suffix_2"
