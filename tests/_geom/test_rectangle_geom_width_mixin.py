import apysc as ap
from apysc._geom.rectangle_geom_width_mixin import RectangleGeomWidthMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestRectangleGeomWidthMixIn:
    @apply_test_settings()
    def test_width(self) -> None:
        mixin: RectangleGeomWidthMixIn = RectangleGeomWidthMixIn()
        mixin._width = ap.Int(200)
        assert mixin.width == ap.Int(200)
