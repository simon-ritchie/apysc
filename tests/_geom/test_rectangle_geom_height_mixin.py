import apysc as ap
from apysc._geom.rectangle_geom_height_mixin import RectangleGeomHeightMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestRectangleGeomHeightMixIn:
    @apply_test_settings()
    def test_height(self) -> None:
        mixin: RectangleGeomHeightMixIn = RectangleGeomHeightMixIn()
        mixin._height = ap.Int(100)
        assert mixin.height == 100
