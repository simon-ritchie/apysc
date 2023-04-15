import apysc as ap
from apysc._chart.axis_line_alpha_mixin import AxisLineAlphaMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAxisLineAlphaMixIn:
    @apply_test_settings()
    def test__set_initial_line_alpha(self) -> None:
        mixin: AxisLineAlphaMixIn = AxisLineAlphaMixIn()
        mixin._set_initial_line_alpha(
            line_alpha=0.5,
            variable_name_suffix="test_suffix_1",
        )
        assert mixin._line_alpha == ap.Number(0.5)
        assert mixin._line_alpha._variable_name_suffix == "test_suffix_1"

        mixin._set_initial_line_alpha(
            line_alpha=ap.Number(0.7, variable_name_suffix="test_suffix_2"),
        )
        assert mixin._line_alpha == ap.Number(0.7)
        assert mixin._line_alpha._variable_name_suffix == "test_suffix_2"
