from apysc._chart.x_axis_column_name_mixin import XAxisColumnNameMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestXAxisSettings:
    @apply_test_settings()
    def test__set_initial_x_axis_column_name(self) -> None:
        mixin: XAxisColumnNameMixIn = XAxisColumnNameMixIn()
        mixin._set_initial_x_axis_column_name(
            x_axis_column_name="test_column_1",
        )
        assert mixin._x_axis_column_name == "test_column_1"
