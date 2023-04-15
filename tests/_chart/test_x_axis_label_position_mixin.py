import apysc as ap
from apysc._chart.x_axis_label_position_mixin import XAxisLabelPositionMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestXAxisLabelPositionMixIn:
    @apply_test_settings()
    def test__set_initial_x_axis_label_position(self) -> None:
        mixin: XAxisLabelPositionMixIn = XAxisLabelPositionMixIn()
        mixin._set_initial_x_axis_label_position(
            x_axis_label_position=ap.XAxisLabelPosition.OUTER_LEFT
        )
        assert mixin._x_axis_label_position == ap.XAxisLabelPosition.OUTER_LEFT
