import apysc as ap
from apysc._chart.y_axis_column_name_mixin import YAxisColumnNameMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestYAxisColumnNameMixIn:
    @apply_test_settings()
    def test__set_initial_y_axis_column_name(self) -> None:
        mixin: YAxisColumnNameMixIn = YAxisColumnNameMixIn()
        mixin._set_initial_y_axis_column_name(
            y_axis_column_name="test_column_1",
        )
        assert mixin._y_axis_column_name == ap.String("test_column_1")

        mixin._set_initial_y_axis_column_name(
            y_axis_column_name=ap.String("test_column_2"),
        )
        assert mixin._y_axis_column_name == ap.String("test_column_2")
