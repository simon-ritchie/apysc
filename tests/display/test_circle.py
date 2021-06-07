from random import randint
from typing import Match, Optional
import re

from retrying import retry

from apysc import Circle, Stage, Sprite
from apysc.expression import expression_file_util
from apysc.display.stage import get_stage_variable_name


class TestCircle:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        stage: Stage = Stage()
        stage_variable_name: str = get_stage_variable_name()
        sprite: Sprite = Sprite(stage=stage)
        circle: Circle = Circle(
            parent=sprite.graphics,
            x=50,
            y=100,
            radius=30)
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'var {circle.variable_name} = {stage_variable_name}'
                r'\n  \.circle\(.+?\)'
                r'\n  \.attr\(.+?'
                r'\n  \}\);'
            ),
            string=expression, flags=re.MULTILINE | re.DOTALL)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#0af')
        sprite.graphics.line_style(color='#fff')
        circle: Circle = Circle(
            parent=sprite.graphics,
            x=50,
            y=100,
            radius=30)
        assert circle.x == 50
        assert circle.y == 100
        assert circle.radius == 30
        assert circle.fill_color == '#00aaff'
        assert circle.line_color == '#ffffff'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        circle: Circle = Circle(
            parent=sprite.graphics,
            x=50,
            y=100,
            radius=30)
        repr_str: str = repr(circle)
        assert repr_str == f"Circle('{circle.variable_name}')"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_center_coordinates(self) -> None:
        expression_file_util.remove_expression_file()
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        circle: Circle = Circle(
            parent=sprite.graphics,
            x=50,
            y=100,
            radius=30)
        assert circle.x == 50
        assert circle.y == 100
        expression: str = expression_file_util.get_current_expression()
        assert f'{circle.variable_name}.cx(' in expression
