from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util


class TestPolygonY2MixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y2(self) -> None:
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
        y2: ap.Int = triangle.y2
        assert y2 == ap.Int(150)
        triangle.y2 = ap.Int(160)
        assert triangle.y2 == ap.Int(160)
        assert triangle._y2.value == 160
        assert triangle._points[1].y == ap.Int(160)
        expression: str = expression_data_util.get_current_expression()
        assert ".plot" in expression
