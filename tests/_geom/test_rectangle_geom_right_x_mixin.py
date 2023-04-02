import apysc as ap
from apysc._geom.rectangle_geom_right_x_mixin import RectangleGeomRightXMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestRectangleGeomRightXMixIn:
    @apply_test_settings()
    def test_right_x(self) -> None:
        mixin: RectangleGeomRightXMixIn = RectangleGeomRightXMixIn()
        mixin._right_x = ap.Number(150)
        assert mixin.right_x == ap.Number(150)
