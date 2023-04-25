import apysc as ap
from apysc._chart.set_initial_border_color_mixin import SetInitialBorderColorMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialBorderColorMixIn:
    @apply_test_settings()
    def test__set_initial_border_color(self) -> None:
        mixin: SetInitialBorderColorMixIn = SetInitialBorderColorMixIn()
        mixin._set_initial_border_color(
            border_color="#333",
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._border_color == ap.String("#333333")
        assert mixin._border_color._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_border_color(
            border_color=ap.String("#555", variable_name_suffix="test_suffix_2"),
        )
        assert mixin._border_color == ap.String("#555555")
        assert mixin._border_color._variable_name_suffix == "test_suffix_2"
