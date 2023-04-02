import apysc as ap
from apysc._geom.rectangle_geom_left_x_mixin import RectangleGeomLeftXMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestRectangleGeomLeftXMixIn:
    @apply_test_settings()
    def test_left_x(self) -> None:
        mixin: RectangleGeomLeftXMixIn = RectangleGeomLeftXMixIn()
        mixin._left_x = ap.Number(50)
        assert mixin.left_x == ap.Number(50)
