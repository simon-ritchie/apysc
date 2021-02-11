from random import randint

from retrying import retry

from apyscript.display import graphics
from apyscript.display.graphics import Graphics, Rectangle, _GraphicBase
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from apyscript.display.stage import get_stage_variable_name
from apyscript.expression import expression_scope, expression_file_util
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

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
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

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_x(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphic_base: _GraphicBase = _GraphicBase(
            parent=sprite.graphics, x=100, y=200,
            variable_name='test_graphic')
        graphic_base.x = 300
        assert graphic_base.x == 300

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_y(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphic_base: _GraphicBase = _GraphicBase(
            parent=sprite.graphics, x=100, y=200,
            variable_name='test_graphic')
        graphic_base.y = 400
        assert graphic_base.y == 400

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_variable_name(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        graphic_base: _GraphicBase = _GraphicBase(
            parent=sprite.graphics, x=100, y=200,
            variable_name='test_graphic_1')
        assert graphic_base.variable_name == 'test_graphic_1'
        graphic_base.variable_name = 'test_graphic_2'
        assert graphic_base.variable_name == 'test_graphic_2'


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test__make_rect_attrs_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    rectangle: Rectangle = Rectangle(
        parent=sprite.graphics,
        x=100, y=200,
        width=150, height=50)
    rect_attrs_expression: str = graphics._make_rect_attrs_expression(
        rectangle=rectangle)
    expected: str = (
        '\n  .attr({'
        '\n  })'
    )
    assert rect_attrs_expression == expected

    sprite.graphics.begin_fill(color='#333')
    rect_attrs_expression = graphics._make_rect_attrs_expression(
        rectangle=rectangle)
    expected = (
        '\n  .attr({'
        '\n    fill: "#333333",'
        '\n  })'
    )
    assert rect_attrs_expression == expected


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test__append_draw_rect_expression() -> None:
    stage: Stage = Stage()
    expression_scope.update_current_scope(scope_name='test_graphics')
    expression_file_util.remove_current_scope_expression_file()
    sprite: Sprite = Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#333')
    sprite.graphics.draw_rect(x=100, y=200, width=300, height=400)
    sprite_name: str = sprite.variable_name
    rect_name: str = sprite.graphics._graphics[0].variable_name
    stage_variable_name: str = get_stage_variable_name()
    expression: str = expression_file_util.get_current_scope_expression()
    expected: str = (
        '<script type="text/javascript">'
        f'\nvar {rect_name} = {stage_variable_name}'
        '\n  .rect(300, 400)'
        '\n  .attr({'
        '\n    fill: "#333333",'
        '\n  });'
        f'\n{sprite_name}.add({rect_name});'
        '\n</script>'
    )
    assert expected in expression
    expression_file_util.remove_current_scope_expression_file()
