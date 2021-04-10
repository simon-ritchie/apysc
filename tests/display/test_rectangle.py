from random import randint
from typing import List, Match, Optional
import re

from retrying import retry

from apysc import Number
from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc.display import rectangle
from apysc.display.stage import get_stage_variable_name
from apysc.expression import expression_file_util, var_names
from tests import testing_helper


class TestRectangle:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        rectangle: Rectangle = Rectangle(
            parent=sprite.graphics,
            x=100, y=200, width=300, height=400, fill_color='#333',
            fill_alpha=0.75, line_color='#aaa', line_thickness=3,
            line_alpha=0.3)
        testing_helper.assert_attrs(
            expected_attrs={
                'parent_graphics': sprite.graphics,
                '_x': 100,
                '_y': 200,
                'width': 300,
                'height': 400,
                '_fill_color': '#333333',
                '_fill_alpha': 0.75,
                '_line_color': '#aaaaaa',
                '_line_thickness': 3,
                '_line_alpha': 0.3,
            },
            any_obj=rectangle)

        rectanble = Rectangle(
            parent=sprite.graphics, x=100, y=200, width=300, height=400,
            fill_alpha=Number(value=0.5))
        assert rectanble._fill_alpha == 0.5


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test__make_rect_attrs_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    rectangle_: Rectangle = Rectangle(
        parent=sprite.graphics,
        x=100, y=200,
        width=150, height=50)
    rect_attrs_expression: str = rectangle._make_rect_attrs_expression(
        rectangle=rectangle_)
    match: Optional[Match] = re.search(
        pattern=(
            r'\n  \.attr\(\{'
            rf'\n    "fill-opacity": {var_names.NUMBER}.+?,'
            rf'\n    "stroke-width": {var_names.INT}.+?,'
            rf'\n    "stroke-opacity": {var_names.NUMBER}.+?,'
            rf'\n    x: {var_names.INT}.+?,'
            rf'\n    y: {var_names.INT}.+?,'
            r'\n  \}\)'
        ),
        string=rect_attrs_expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_append_draw_rect_expression() -> None:
    stage: Stage = Stage()
    sprite: Sprite = Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#333', alpha=0.5)
    sprite.graphics.draw_rect(x=100, y=200, width=300, height=400)
    graphics_name: str = sprite.graphics.variable_name
    rect_name: str = sprite.graphics.get_child_at(index=0).variable_name
    stage_variable_name: str = get_stage_variable_name()
    expression: str = expression_file_util.get_current_expression()
    match: Optional[Match] = re.search(
        pattern=(
            rf'\nvar {rect_name} = {stage_variable_name}'
            rf'\n  \.rect\({var_names.INT}.+?, {var_names.INT}.+?\)'
            r'\n  \.attr\(\{'
            rf'\n    fill: {var_names.STRING}.+?,'
            rf'\n    "fill-opacity": {var_names.NUMBER}.+?,'
            rf'\n    "stroke-width": {var_names.INT}.+?,'
            rf'\n    "stroke-opacity": {var_names.NUMBER}.+?,'
            rf'\n    x: {var_names.INT}.+?,'
            rf'\n    y: {var_names.INT}.+?,'
            r'\n  \}\);'
            r'.*'
            rf'\n{graphics_name}\.add\({rect_name}\)'
        ),
        string=expression,
        flags=re.MULTILINE| re.DOTALL,
    )
    assert match is not None
    expression_file_util.remove_expression_file()
