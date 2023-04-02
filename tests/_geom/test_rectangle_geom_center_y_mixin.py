import apysc as ap
from apysc._geom.rectangle_geom_center_y_mixin import RectangleGeomCenterYMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestRectangleGeomCenterYMixIn:
    @apply_test_settings()
    def test_center_y(self) -> None:
        mixin: RectangleGeomCenterYMixIn = RectangleGeomCenterYMixIn()
        mixin._center_y = ap.Number(250)
        assert mixin.center_y == ap.Number(250)
