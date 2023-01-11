from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util


class TestPolygonX2MixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x2(self) -> None:
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
        x2: ap.Int = triangle.x2
        assert x2 == ap.Int(75)
        triangle.x2 = ap.Int(80)
        assert triangle.x2 == ap.Int(80)
        assert triangle._x2.value == 80
        assert triangle._points[1].x == ap.Int(80)
        expression: str = expression_data_util.get_current_expression()
        assert ".plot" in expression
