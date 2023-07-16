import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestPolygonX3MixIn:
    @apply_test_settings()
    def test_x3(self) -> None:
        ap.Stage()
        triangle: ap.Triangle = ap.Triangle(
            x1=100,
            y1=100,
            x2=75,
            y2=150,
            x3=125,
            y3=150,
        )
        x3: ap.Number = triangle.x3
        assert x3 == ap.Number(125)

        triangle.x3 = ap.Number(130)
        assert triangle.x3 == ap.Number(130)
        assert triangle._points[2].x == ap.Number(130)
        expression: str = expression_data_util.get_current_expression()
        assert ".plot" in expression
