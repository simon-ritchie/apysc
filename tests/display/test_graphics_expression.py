import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc.display import graphics_expression
from apysc.display.graphics import Graphics
from apysc.expression import var_names


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  fill: {var_names.STRING}.+?,'
        ),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_append_x_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    rectangle: Rectangle = Rectangle(
        parent=sprite.graphics,
        x=100, y=200, width=300, height=400)
    expression: str = '.attr({'
    expression = graphics_expression.append_x_expression(
        graphic=rectangle, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  x: {var_names.INT}.+?,'
        ),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_append_y_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    rectangle: Rectangle = Rectangle(
        parent=sprite.graphics,
        x=100, y=200, width=300, height=400)
    expression: str = '.attr({'
    expression = graphics_expression.append_y_expression(
        graphic=rectangle, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  y: {var_names.INT}.+?,'),
        string=expression, flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_append_fill_opacity_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    graphics: Graphics = sprite.graphics
    expression: str = '.attr({'
    graphics.begin_fill(color='#333', alpha=0.5)
    expression = graphics_expression.append_fill_opacity_expression(
        graphics=graphics, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  "fill-opacity": {var_names.NUMBER}.+?,'),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
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
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  stroke: {var_names.STRING}.+?,'
        ),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_append_stroke_width_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    graphics: Graphics = sprite.graphics
    expression: str = '.attr({'
    expression = graphics_expression.append_stroke_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == '.attr({'

    graphics.line_style(color='#666', thickness=3)
    expression = graphics_expression.append_stroke_width_expression(
        graphics=graphics, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  "stroke-width": {var_names.INT}.+?,'),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_append_stroke_opacity_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    graphics: Graphics = sprite.graphics
    expression: str = '.attr({'
    expression = graphics_expression.append_stroke_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == '.attr({'

    graphics.line_style(color='#666', alpha=0.25)
    expression = graphics_expression.append_stroke_opacity_expression(
        graphics=graphics, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  "stroke-opacity": {var_names.NUMBER}.+?,'),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None
