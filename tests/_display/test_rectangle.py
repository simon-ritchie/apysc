import re
from random import randint
from typing import List
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.stage import get_stage_variable_name
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing import testing_helper
from tests._display.test_graphics_expression import \
    assert_fill_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_fill_opacity_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_stroke_opacity_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_stroke_width_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_x_attr_expression_exists
from tests._display.test_graphics_expression import \
    assert_y_attr_expression_exists


class TestRectangle:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        ap.Stage()
        rectangle: ap.Rectangle = ap.Rectangle(
            x=50,
            y=100,
            width=150,
            height=200,
            fill_color='#0af',
            fill_alpha=0.5,
            line_color='fff',
            line_alpha=0.3,
            line_thickness=3,
            line_cap=ap.LineCaps.ROUND,
            line_joints=ap.LineJoints.BEVEL,
            line_dot_setting=ap.LineDotSetting(dot_size=10))
        testing_helper.assert_attrs(
            expected_attrs={
                '_x': 50,
                '_y': 100,
                '_width': 150,
                '_height': 200,
                '_fill_color': '#00aaff',
                '_fill_alpha': 0.5,
                '_line_color': '#ffffff',
                '_line_alpha': 0.3,
                '_line_thickness': 3,
                '_line_cap': ap.LineCaps.ROUND.value,
                '_line_joints': ap.LineJoints.BEVEL.value,
                '_line_dot_setting': ap.LineDotSetting(dot_size=10),
            },
            any_obj=rectangle,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        rectangle_: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50)
        repr_str: str = repr(rectangle_)
        assert repr_str == f"Rectangle('{rectangle_.variable_name}')"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_append_constructor_expression(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#333', alpha=0.5)
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=100, y=200, width=300, height=400)
        graphics_name: str = sprite.graphics.variable_name
        rect_name: str = rectangle.variable_name
        stage_variable_name: str = get_stage_variable_name()
        expression: str = expression_data_util.get_current_expression()
        expected_patterns: List[str] = [
            rf'var {rect_name} = {stage_variable_name}',
            rf'\n  \.rect\({var_names.INT}.+?, {var_names.INT}.+?\)',
            r'\n  \.attr\(\{',
            r'\n  \}\);',
            rf'\n{graphics_name}\.add\({rect_name}\)',
        ]
        for expected_pattern in expected_patterns:
            match: Optional[Match] = re.search(
                pattern=expected_pattern, string=expression,
                flags=re.MULTILINE)
            assert match is not None, f'{expected_pattern}, \n\n{expression}'
        assert_fill_attr_expression_exists(expression=expression)
        assert_fill_opacity_attr_expression_exists(expression=expression)
        assert_x_attr_expression_exists(expression=expression)
        assert_y_attr_expression_exists(expression=expression)
        assert_stroke_width_attr_expression_exists(expression=expression)
        assert_stroke_opacity_attr_expression_exists(expression=expression)
        expression_data_util.empty_expression()
