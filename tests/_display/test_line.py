import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs
from tests._display.test_graphics_expression import assert_stroke_attr_expression_exists


class TestLine:
    @apply_test_settings()
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        line: ap.Line = ap.Line(
            start_point=ap.Point2D(x=10, y=20),
            end_point=ap.Point2D(x=30, y=40),
            line_color="fff",
            line_alpha=0.3,
            line_thickness=3,
            line_cap=ap.LineCaps.ROUND,
            line_dot_setting=ap.LineDotSetting(dot_size=10),
            variable_name_suffix="test_line",
        )
        assert_attrs(
            expected_attrs={
                "_start_point": ap.Point2D(x=10, y=20),
                "_end_point": ap.Point2D(x=30, y=40),
                "_line_color": "#ffffff",
                "_line_alpha": 0.3,
                "_line_thickness": 3,
                "_line_cap": ap.LineCaps.ROUND.value,
                "_line_dot_setting": ap.LineDotSetting(dot_size=10),
                "_parent": stage,
                "_variable_name_suffix": "test_line",
            },
            any_obj=line,
        )

        sprite: ap.Sprite = ap.Sprite()
        line = ap.Line(
            start_point=ap.Point2D(x=10, y=20),
            end_point=ap.Point2D(x=30, y=40),
            line_dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),
            parent=sprite,
        )
        assert_attrs(
            expected_attrs={
                "_line_dash_setting": ap.LineDashSetting(dash_size=10, space_size=5),
                "_parent": sprite,
            },
            any_obj=line,
        )

        line = ap.Line(
            start_point=ap.Point2D(x=10, y=20),
            end_point=ap.Point2D(x=30, y=40),
            line_round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=5),
        )
        assert line._line_round_dot_setting == ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )

        line = ap.Line(
            start_point=ap.Point2D(x=10, y=20),
            end_point=ap.Point2D(x=30, y=40),
            line_dash_dot_setting=ap.LineDashDotSetting(
                dot_size=5, dash_size=10, space_size=3
            ),
        )
        assert line._line_dash_dot_setting == ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=3
        )

    @apply_test_settings()
    def test__make_points_expression(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        line: ap.Line = ap.Line(
            parent=sprite.graphics,
            start_point=ap.Point2D(x=10, y=20),
            end_point=ap.Point2D(x=30, y=40),
        )
        expression: str = line._make_points_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{var_names.NUMBER}_.+, {var_names.NUMBER}_.+, "
                rf"{var_names.NUMBER}_.+, {var_names.NUMBER}_.+$"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.line_style(color="#333", thickness=3)
        line: ap.Line = sprite.graphics.draw_line(
            x_start=10, y_start=20, x_end=30, y_end=40
        )
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"var {line.variable_name} = {stage.variable_name}"
                r"\n  .line\(.+?\)"
                r"\n  .attr\(\{.*?"
                r"\n  \}\);"
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None
        assert_stroke_attr_expression_exists(expression=expression)

    @apply_test_settings()
    def test___repr__(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        line: ap.Line = ap.Line(
            parent=sprite.graphics,
            start_point=ap.Point2D(x=10, y=20),
            end_point=ap.Point2D(x=30, y=40),
        )
        repr_str: str = repr(line)
        expected: str = f'Line("{line.variable_name}")'
        assert repr_str == expected

    @apply_test_settings()
    def test__create_with_graphics(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.line_style(
            color="#fff",
            thickness=3,
            alpha=0.3,
            cap=ap.LineCaps.ROUND,
            dot_setting=ap.LineDotSetting(dot_size=10),
        )
        line: ap.Line = ap.Line._create_with_graphics(
            graphics=sprite.graphics,
            start_point=ap.Point2D(x=10, y=20),
            end_point=ap.Point2D(x=30, y=40),
            variable_name_suffix="test_line",
        )
        assert_attrs(
            expected_attrs={
                "_start_point": ap.Point2D(x=10, y=20),
                "_end_point": ap.Point2D(x=30, y=40),
                "_line_color": "#ffffff",
                "_line_thickness": 3,
                "_line_alpha": 0.3,
                "_line_cap": ap.LineCaps.ROUND.value,
                "_line_dot_setting": ap.LineDotSetting(dot_size=10),
                "_parent": sprite.graphics,
                "_variable_name_suffix": "test_line",
            },
            any_obj=line,
        )

    @apply_test_settings()
    def test__set_initial_x_and_y_with_minimum_point(self) -> None:
        ap.Stage()
        line: ap.Line = ap.Line(
            start_point=ap.Point2D(x=10, y=20), end_point=ap.Point2D(x=30, y=40)
        )
        assert line.x == 10
        assert line.y == 20

        line = ap.Line(
            start_point=ap.Point2D(x=30, y=40), end_point=ap.Point2D(x=10, y=20)
        )
        assert line.x == 10
        assert line.y == 20
