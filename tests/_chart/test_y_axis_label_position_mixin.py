import apysc as ap
from apysc._chart.y_axis_label_position_mixin import YAxisLabelPositionMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestYAxisLabelPositionMixIn:
    @apply_test_settings()
    def test__set_initial_y_axis_label_position(self) -> None:
        mixin: YAxisLabelPositionMixIn = YAxisLabelPositionMixIn()
        mixin._set_initial_y_axis_label_position(
            y_axis_label_position=ap.YAxisLabelPosition.OUTER_TOP,
        )
        assert mixin._y_axis_label_position == ap.YAxisLabelPosition.OUTER_TOP
