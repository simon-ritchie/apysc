from random import randint

from retrying import retry

import apysc as ap


class TestPolygonX1MixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x1(self) -> None:
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
