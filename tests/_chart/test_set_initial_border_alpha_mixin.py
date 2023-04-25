import apysc as ap
from apysc._chart.set_initial_border_alpha_mixin import SetInitialBorderAlphaMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialBorderAlphaMixIn:
    @apply_test_settings()
    def test__set_initial_border_alpha(self) -> None:
        mixin: SetInitialBorderAlphaMixIn = SetInitialBorderAlphaMixIn()
        mixin._set_initial_border_alpha(
            border_alpha=0.3, variable_name_suffix="test_suffix_1"
        )
        assert mixin._border_alpha == ap.Number(0.3)
        assert mixin._border_alpha._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_border_alpha(
            border_alpha=ap.Number(0.5, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._border_alpha == ap.Number(0.5)
        assert mixin._border_alpha._variable_name_suffix == "test_suffix_2"
