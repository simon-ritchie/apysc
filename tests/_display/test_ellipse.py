import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.stage import get_stage_variable_name
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_attrs
from tests._display.test_graphics_expression import \
    assert_fill_attr_expression_exists


class TestEllipse:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#0af')
        stage_variable_name: str = get_stage_variable_name()
        ellipse: ap.Ellipse = ap.Ellipse(
            parent=sprite.graphics,
            x=50, y=100, width=150, height=200)
        expression: str = expression_data_util.get_current_expression()
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
        stage: ap.Stage = ap.Stage()
        ellipse: ap.Ellipse = ap.Ellipse(
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
            line_dot_setting=ap.LineDotSetting(dot_size=10),
            variable_name_suffix='test_ellipse')
        assert_attrs(
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
                '_parent': stage,
                '_variable_name_suffix': 'test_ellipse',
            },
            any_obj=ellipse,
        )

        sprite = ap.Sprite()
        ellipse = ap.Ellipse(
            x=50, y=100, width=150, height=200,
            line_dash_setting=ap.LineDashSetting(
                dash_size=10, space_size=5),
            parent=sprite)
        assert_attrs(
            expected_attrs={
                '_line_dash_setting': ap.LineDashSetting(
                    dash_size=10, space_size=5),
                '_parent': sprite,
            },
            any_obj=ellipse)

        ellipse = ap.Ellipse(
            x=50, y=100, width=150, height=200,
            line_round_dot_setting=ap.LineRoundDotSetting(
                round_size=10, space_size=5))
        assert ellipse._line_round_dot_setting == ap.LineRoundDotSetting(
            round_size=10, space_size=5)

        ellipse = ap.Ellipse(
            x=50, y=100, width=150, height=200,
            line_dash_dot_setting=ap.LineDashDotSetting(
                dot_size=5, dash_size=10, space_size=3))
        assert ellipse._line_dash_dot_setting == ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=3)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        ellipse: ap.Ellipse = ap.Ellipse(
            parent=sprite.graphics, x=50, y=100, width=150, height=200)
        repr_str: str = repr(ellipse)
        assert repr_str == f"Ellipse('{ellipse.variable_name}')"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__create_with_graphics(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#0af', alpha=0.5)
        sprite.graphics.line_style(
            color='#fff',
            thickness=3,
            alpha=0.3,
            cap=ap.LineCaps.ROUND,
            joints=ap.LineJoints.BEVEL,
            dash_setting=ap.LineDashSetting(dash_size=10, space_size=5))
        ellipse: ap.Ellipse = ap.Ellipse._create_with_graphics(
            graphics=sprite.graphics,
            x=100, y=150, width=30, height=50,
            variable_name_suffix='test_ellipse')
        assert_attrs(
            expected_attrs={
                '_parent': sprite.graphics,
                '_x': 100,
                '_y': 150,
                '_width': 30,
                '_height': 50,
                '_fill_color': '#00aaff',
                '_fill_alpha': 0.5,
                '_line_color': '#ffffff',
                '_line_thickness': 3,
                '_line_alpha': 0.3,
                '_line_cap': ap.LineCaps.ROUND.value,
                '_line_joints': ap.LineJoints.BEVEL.value,
                '_line_dash_setting':
                ap.LineDashSetting(dash_size=10, space_size=5),
                '_variable_name_suffix': 'test_ellipse',
            },
            any_obj=ellipse)
