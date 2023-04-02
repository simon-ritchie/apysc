import apysc as ap
from apysc._geom.rectangle_geom_center_x_mixin import RectangleGeomCenterXMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestRectangleGeomCenterXMixIn:
    @apply_test_settings()
    def test_center_x(self) -> None:
        mixin: RectangleGeomCenterXMixIn = RectangleGeomCenterXMixIn()
        mixin._center_x = ap.Number(100)
        assert mixin.center_x == ap.Number(100)
