from random import randint
from typing import Match, Optional
import re

from retrying import retry

from apysc import Ellipse, Stage, Sprite, LineDotSetting
from tests.display.test_graphics_expression import \
    assert_fill_attr_expression_exists
from apysc.expression import expression_file_util
from apysc.display.stage import get_stage_variable_name
from apysc.expression import var_names


class TestEllipse:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#0af')
        stage_variable_name: str = get_stage_variable_name()
        ellipse: Ellipse = Ellipse(
            parent=sprite.graphics,
            x=50, y=100, width=150, height=200)
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'var {ellipse.variable_name} = {stage_variable_name}'
                r'\n  \.ellipse\(.+?, .+?\)'
                r'\n  .attr\(\{.*?'
                r'\n  \}\);'
            ),
            string=expression, flags=re.MULTILINE | re.DOTALL)
        assert match is not None

        assert_fill_attr_expression_exists(expression=expression)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.line_style(
            color='#fff',
            dot_setting=LineDotSetting(dot_size=5))
        ellipse: Ellipse = Ellipse(
            parent=sprite.graphics, x=50, y=100, width=150, height=200)
        assert ellipse.variable_name.startswith(f'{var_names.ELLIPSE}_')
        assert ellipse.width == 150
        assert ellipse.height == 200
        assert ellipse.x == 50
        assert ellipse.y == 100
        assert isinstance(ellipse.line_dot_setting, LineDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        ellipse: Ellipse = Ellipse(
            parent=sprite.graphics, x=50, y=100, width=150, height=200)
        repr_str: str = repr(ellipse)
        assert repr_str == f"Ellipse('{ellipse.variable_name}')"
