from random import randint

from retrying import retry

from apyscript.display.graphics import Graphics
from apyscript.display.graphics import Rectangle
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from tests import testing_helper


class TestGraphics:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphics: Graphics = Graphics(parent=sprite)
        testing_helper.assert_attrs(
            expected_attrs={
                'parent': sprite,
            },
            any_obj=graphics)
        assert isinstance(graphics.variable_name, str)
        assert graphics.variable_name != ''

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_begin_fill(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphics: Graphics = Graphics(parent=sprite)
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=graphics.begin_fill,
            kwargs={'color': 'red'})

        graphics.begin_fill(color='#0af')
        testing_helper.assert_attrs(
            expected_attrs={
                '_fill_color': '#00aaff',
            },
            any_obj=graphics)

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_draw_rect(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphics: Graphics = Graphics(parent=sprite)
        rectangle: Rectangle = graphics.draw_rect(
            x=100, y=200, width=300, height=400)
        assert len(graphics._graphics) == 1
        testing_helper.assert_attrs(
            expected_attrs={
                '_x': 100,
                '_y': 200,
                'width': 300,
                'height': 400,
            },
            any_obj=graphics._graphics[0])
        assert isinstance(graphics._graphics[0], Rectangle)
        assert rectangle == graphics._graphics[0]

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_clear(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#333')
        sprite.graphics.draw_rect(x=50, y=50, width=100, height=100)
        assert len(sprite.graphics._graphics) == 1
        sprite.graphics.clear()
        assert len(sprite.graphics._graphics) == 0
