import apysc as ap
from apysc._chart.set_initial_overall_container_coordinates_mixin import (
    SetInitialOverallContainerCoordinatesMixIn,
)
from apysc._testing.testing_helper import apply_test_settings


class TestSetInitialOverallContainerCoordinatesMixIn:
    @apply_test_settings()
    def test__set_initial_overall_container_coordinates(self) -> None:
        mixin: SetInitialOverallContainerCoordinatesMixIn = (
            SetInitialOverallContainerCoordinatesMixIn()
        )
        overall_container: ap.Sprite = ap.Sprite()
        mixin._set_initial_overall_container_coordinates(
            overall_container=overall_container,
            x=ap.Number(50),
            y=ap.Number(100),
        )
        assert overall_container.x == ap.Number(50)
        assert overall_container.y == ap.Number(100)
