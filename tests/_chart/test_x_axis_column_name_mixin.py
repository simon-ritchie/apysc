import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._chart.x_axis_column_name_mixin import XAxisColumnNameMixIn


class TestXAxisSettings:
    @apply_test_settings()
    def test__make_snapshot_and__revert(self) -> None:
        mixin: XAxisColumnNameMixIn = XAxisColumnNameMixIn()
        mixin._x_axis_column_name = ap.String("test_1")
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._x_axis_column_name._value = "test_2"
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._x_axis_column_name == ap.String("test_1")

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
