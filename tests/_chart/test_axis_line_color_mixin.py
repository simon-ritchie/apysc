import apysc as ap
from apysc._chart.axis_line_color_mixin import AxisLineColorMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAxisLineColorMixIn:
    @apply_test_settings()
    def test__set_initial_line_color(self) -> None:
        mixin: AxisLineColorMixIn = AxisLineColorMixIn()
        mixin._set_initial_line_color(
            line_color=ap.Color("#0af"),
        )
        assert mixin._line_color == ap.Color("#00aaff")
