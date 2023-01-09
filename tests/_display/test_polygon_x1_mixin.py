from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util


class TestPolygonX1MixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x1(self) -> None:
        expression_data_util.empty_expression()
        ap.Stage()
        triangle: ap.Triangle = ap.Triangle(
            x1=100,
            y1=100,
            x2=75,
            y2=150,
            x3=125,
            y3=150,
        )
        x1: ap.Int = triangle.x1
        assert isinstance(x1, ap.Int)
        assert x1 == ap.Int(100)

        triangle.x1 = ap.Int(110)
        assert triangle.x1 == ap.Int(110)
        assert triangle._points[0].x == ap.Int(110)
        expression: str = expression_data_util.get_current_expression()
        assert ".plot" in expression
