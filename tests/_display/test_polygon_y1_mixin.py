import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestPolygonY1MixIn:
    @apply_test_settings()
    def test_y1(self) -> None:
        triangle: ap.Triangle = ap.Triangle(
            x1=100,
            y1=50,
            x2=50,
            y2=100,
            x3=150,
            y3=100,
        )
        y1: ap.Number = triangle.y1
        assert y1 == ap.Number(50)
        assert triangle._y1._value == 50

        triangle.y1 = ap.Number(75)
        assert triangle.y1 == ap.Number(75)
        assert triangle._points[0].y == ap.Number(75)
