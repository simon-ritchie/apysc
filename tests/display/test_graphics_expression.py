from random import randint

from retrying import retry

from apyscript.display import graphics_expression
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from apyscript.display.graphics import Graphics
from apyscript.display.rectangle import Rectangle


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_append_fill_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    graphics: Graphics = Graphics(parent=sprite)
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
