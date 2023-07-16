import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestPolygonY2MixIn:
    @apply_test_settings()
    def test_y2(self) -> None:
        ap.Stage()
        triangle: ap.Triangle = ap.Triangle(
            x1=100,
            y1=100,
            x2=75,
            y2=150,
            x3=125,
            y3=150,
        )
        y2: ap.Number = triangle.y2
        assert y2 == ap.Number(150)
        triangle.y2 = ap.Number(160)
        assert triangle.y2 == ap.Number(160)
        assert triangle._y2.value == 160
        assert triangle._points[1].y == ap.Number(160)
        expression: str = expression_data_util.get_current_expression()
        assert ".plot" in expression
