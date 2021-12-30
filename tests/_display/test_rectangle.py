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
from tests import testing_helper
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
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#333', alpha=0.75)
        sprite.graphics.line_style(color='#aaa', thickness=3, alpha=0.3)
        rectangle: ap.Rectangle = ap.Rectangle(
            parent=sprite.graphics,
            x=100, y=200, width=300, height=400)
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

        sprite.graphics.begin_fill(color='#333', alpha=ap.Number(0.5))
        rectanble = ap.Rectangle(
            parent=sprite.graphics, x=100, y=200, width=300, height=400)
        assert rectanble._fill_alpha == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        rectangle_: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50)
        repr_str: str = repr(rectangle_)
        assert repr_str == f"Rectangle('{rectangle_.variable_name}')"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_rect_attrs_expression(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        _: ap.Rectangle = ap.Rectangle(
            parent=sprite.graphics,
            x=100, y=200,
            width=150, height=50)
        expression: str = expression_data_util.get_current_expression()
        assert '.attr({' in expression
        assert_fill_opacity_attr_expression_exists(expression=expression)
        assert_stroke_width_attr_expression_exists(expression=expression)
        assert_stroke_opacity_attr_expression_exists(expression=expression)
        assert_x_attr_expression_exists(expression=expression)
        assert_y_attr_expression_exists(expression=expression)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_append_constructor_expression(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#333', alpha=0.5)
        sprite.graphics.draw_rect(x=100, y=200, width=300, height=400)
        graphics_name: str = sprite.graphics.variable_name
        rect_name: str = sprite.graphics.get_child_at(index=0).variable_name
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
            assert match is not None
        assert_fill_attr_expression_exists(expression=expression)
        assert_fill_opacity_attr_expression_exists(expression=expression)
        assert_x_attr_expression_exists(expression=expression)
        assert_y_attr_expression_exists(expression=expression)
        assert_stroke_width_attr_expression_exists(expression=expression)
        assert_stroke_opacity_attr_expression_exists(expression=expression)
        expression_data_util.empty_expression()
