from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util


class TestPolygonY3MixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y3(self) -> None:
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
        y3: ap.Int = triangle.y3
        assert y3 == ap.Int(150)

        triangle.y3 = ap.Int(160)
        assert triangle.y3 == ap.Int(160)
        assert triangle._points[2].y == ap.Int(160)
        expression: str = expression_data_util.get_current_expression()
        assert ".plot" in expression
