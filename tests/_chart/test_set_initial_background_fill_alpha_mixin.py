import apysc as ap
from apysc._chart.set_initial_background_fill_alpha_mixin import (
    SetInitialBackgroundFillAlphaMixIn,
)
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialBackgroundFillAlphaMixIn:
    @apply_test_settings()
    def test__set_initial_background_fill_alpha(self) -> None:
        mixin: SetInitialBackgroundFillAlphaMixIn = SetInitialBackgroundFillAlphaMixIn()
        mixin._set_initial_background_fill_alpha(
            background_fill_alpha=0.5,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._background_fill_alpha == ap.Number(0.5)
        assert mixin._background_fill_alpha._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_background_fill_alpha(
            background_fill_alpha=ap.Number(0.7, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._background_fill_alpha == ap.Number(0.7)
        assert mixin._background_fill_alpha._variable_name_suffix == "test_suffix_2"
