import apysc as ap
from apysc._geom.rectangle_geom_bottom_y_mixin import RectangleGeomBottomYMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestRectangleGeomBottomYMixIn:
    @apply_test_settings()
    def test_bottom_y(self) -> None:
        mixin: RectangleGeomBottomYMixIn = RectangleGeomBottomYMixIn()
        mixin._bottom_y = ap.Number(300)
        assert mixin.bottom_y == ap.Number(300)
