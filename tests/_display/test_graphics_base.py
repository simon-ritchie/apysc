from random import randint

from retrying import retry

import apysc as ap
from apysc._display.rectangle import Rectangle
from apysc._testing import testing_helper


class TestGraphicsBase:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        rectangle: Rectangle = Rectangle(
            parent=sprite.graphics, x=ap.Int(100), y=ap.Int(200),
            width=ap.Int(50), height=ap.Int(50))
        testing_helper.assert_attrs(
            expected_attrs={
                'parent_graphics': sprite.graphics,
                '_x': 100,
                '_y': 200,
                'stage': stage,
            },
            any_obj=rectangle)

        rectangle = Rectangle(
            parent=sprite.graphics, x=300, y=400,
            width=50, height=50)
        testing_helper.assert_attrs(
            expected_attrs={
                'parent_graphics': sprite.graphics,
                '_x': 300,
                '_y': 400,
            },
            any_obj=rectangle)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        rectangle: Rectangle = Rectangle(
            parent=sprite.graphics, x=ap.Int(100), y=ap.Int(200),
            width=50, height=50)
        rectangle.x = ap.Int(300)
        assert rectangle.x == 300

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        rectangle: Rectangle = Rectangle(
            parent=sprite.graphics, x=ap.Int(100), y=ap.Int(200),
            width=50, height=50)
        rectangle.y = ap.Int(400)
        assert rectangle.y == 400
