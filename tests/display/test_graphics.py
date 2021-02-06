from retrying import retry

from apyscript.display.graphics import Graphics, Rectangle, _GraphicBase
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from tests import testing_helper


class TestGraphics:

    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphics: Graphics = Graphics(parent=sprite)
        testing_helper.assert_attrs(
            expected_attrs={
                'parent': sprite,
            },
            any_obj=graphics)

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

    def test_draw_rect(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphics: Graphics = Graphics(parent=sprite)
        graphics.draw_rect(x=100, y=200, width=300, height=400)
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


class TestRectangle:

    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        rectangle: Rectangle = Rectangle(
            parent=sprite.graphics,
            x=100, y=200, width=300, height=400)
        testing_helper.assert_attrs(
            expected_attrs={
                'parent': sprite.graphics,
                '_x': 100,
                '_y': 200,
                'width': 300,
                'height': 400,
            },
            any_obj=rectangle)


class Test_GraphicBase:

    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphic_base: _GraphicBase = _GraphicBase(
            parent=sprite.graphics, x=100, y=200)
        testing_helper.assert_attrs(
            expected_attrs={
                'parent': sprite.graphics,
                '_x': 100,
                '_y': 200,
            },
            any_obj=graphic_base)

    def test_x(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphic_base: _GraphicBase = _GraphicBase(
            parent=sprite.graphics, x=100, y=200)
        graphic_base.x = 300
        assert graphic_base.x == 300
