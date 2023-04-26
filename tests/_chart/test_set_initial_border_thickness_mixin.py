import apysc as ap
from apysc._chart.set_initial_border_thickness_mixin import (
    SetInitialBorderThicknessMixIn,
)
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialBorderThicknessMixIn:
    @apply_test_settings()
    def test__set_initial_border_thickness(self) -> None:
        mixin: SetInitialBorderThicknessMixIn = SetInitialBorderThicknessMixIn()
        mixin._set_initial_border_thickness(
            border_thickness=2, variable_name_suffix="test_suffix_1"
        )
        assert mixin._border_thickness == ap.Int(2)
        assert mixin._border_thickness._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_border_thickness(
            border_thickness=ap.Int(3, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._border_thickness == ap.Int(3)
        assert mixin._border_thickness._variable_name_suffix == "test_suffix_2"
