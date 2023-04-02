import apysc as ap
from apysc._geom.rectangle_geom_top_y_mixin import RectangleGeomTopYMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestRectangleGeomTopYMixIn:
    @apply_test_settings()
    def test_top_y(self) -> None:
        mixin: RectangleGeomTopYMixIn = RectangleGeomTopYMixIn()
        mixin._top_y = ap.Number(200)
        assert mixin.top_y == ap.Number(200)
