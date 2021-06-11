from random import randint
from typing import Match, Optional
import re

from retrying import retry

from apysc import Ellipse, Stage, Sprite
from tests.display.test_graphics_expression import \
    assert_fill_attr_expression_exists
from apysc.expression import expression_file_util
from apysc.display.stage import get_stage_variable_name


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
                r'\n  \.ellipse\(parseInt\(.+?/ 2\), '
                r'parseInt\(.+? / 2\)\)'
                r'\n  .attr\(\{.*?'
                r'\n  \}\);'
            ),
            string=expression, flags=re.MULTILINE | re.DOTALL)
        assert match is not None

        assert_fill_attr_expression_exists(expression=expression)
