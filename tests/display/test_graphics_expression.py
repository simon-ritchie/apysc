from random import randint

from retrying import retry

from apyscript.display import graphics_expression
from apyscript.display.graphics import Graphics
from apyscript.display.rectangle import Rectangle
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_append_fill_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    graphics: Graphics = sprite.graphics
    expression: str = '.attr({'
    expression = graphics_expression.append_fill_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == '.attr({'

    graphics.begin_fill(color='#333')
    expression = graphics_expression.append_fill_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == (
        '.attr({'
        '\n  fill: "#333333",'
    )


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_append_x_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    rectangle: Rectangle = Rectangle(
        parent=sprite.graphics,
        x=100, y=200, width=300, height=400)
    expression: str = '.attr({'
    expression = graphics_expression.append_x_expression(
        graphic=rectangle, expression=expression, indent_num=1)
    assert expression == (
        '.attr({'
        '\n  x: 100,')


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_append_y_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    rectangle: Rectangle = Rectangle(
        parent=sprite.graphics,
        x=100, y=200, width=300, height=400)
    expression: str = '.attr({'
    expression = graphics_expression.append_y_expression(
        graphic=rectangle, expression=expression, indent_num=1)
    assert expression == (
        '.attr({'
        '\n  y: 200,')


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_append_fill_opacity_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    graphics: Graphics = sprite.graphics
    expression: str = '.attr({'
    expression = graphics_expression.append_fill_opacity_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == '.attr({'

    graphics.begin_fill(color='#333', alpha=0.5)
    expression = graphics_expression.append_fill_opacity_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == (
        '.attr({'
        '\n  "fill-opacity": 0.5,')


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_append_stroke_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    graphics: Graphics = sprite.graphics
    expression: str = '.attr({'
    expression = graphics_expression.append_stroke_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == '.attr({'

    graphics.line_style(color='#666')
    expression = graphics_expression.append_stroke_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == (
        '.attr({'
        '\n  stroke: "#666666",'
    )
