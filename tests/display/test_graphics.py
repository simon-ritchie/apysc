from retrying import retry

from apyscript.display.graphics import Graphics, Rectangle, _GraphicBase
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from tests import testing_helper


class TestGraphics:

    @retry(stop_max_attempt_number=5, wait_fixed=300)
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphics: Graphics = Graphics(parent=sprite)
        testing_helper.assert_attrs(
            expected_attrs={
                'parent': sprite,
            },
            any_obj=graphics)

    @retry(stop_max_attempt_number=5, wait_fixed=300)
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

    @retry(stop_max_attempt_number=5, wait_fixed=300)
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

    @retry(stop_max_attempt_number=5, wait_fixed=300)
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

    @retry(stop_max_attempt_number=5, wait_fixed=300)
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphic_base: _GraphicBase = _GraphicBase(
            parent=sprite.graphics, x=100, y=200,
            variable_name='test_graphic')
        testing_helper.assert_attrs(
            expected_attrs={
                'parent': sprite.graphics,
                '_x': 100,
                '_y': 200,
            },
            any_obj=graphic_base)

    @retry(stop_max_attempt_number=5, wait_fixed=300)
    def test_x(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphic_base: _GraphicBase = _GraphicBase(
            parent=sprite.graphics, x=100, y=200,
            variable_name='test_graphic')
        graphic_base.x = 300
        assert graphic_base.x == 300

    @retry(stop_max_attempt_number=5, wait_fixed=300)
    def test_y(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphic_base: _GraphicBase = _GraphicBase(
            parent=sprite.graphics, x=100, y=200,
            variable_name='test_graphic')
        graphic_base.y = 400
        assert graphic_base.y == 400

    @retry(stop_max_attempt_number=5, wait_fixed=300)
    def test_variable_name(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphic_base: _GraphicBase = _GraphicBase(
            parent=sprite.graphics, x=100, y=200,
            variable_name='test_graphic_1')
        assert graphic_base.variable_name == 'test_graphic_1'
        graphic_base.variable_name = 'test_graphic_2'
        assert graphic_base.variable_name == 'test_graphic_2'
