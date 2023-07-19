import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestCircle:
    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        circle: ap.Circle = ap.Circle(parent=sprite.graphics, x=50, y=100, radius=30)
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"var {circle.variable_name} = {stage.variable_name}"
                r"\n  \.circle\(.+?\)"
                r"\n  \.attr\(.+?"
                r"\n  \}\);"
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

    @apply_test_settings()
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        circle: ap.Circle = ap.Circle(
            x=50,
            y=100,
            radius=150,
            fill_color="#0af",
            fill_alpha=0.5,
            line_color="fff",
            line_alpha=0.3,
            line_thickness=3,
            line_cap=ap.LineCaps.ROUND,
            line_dot_setting=ap.LineDotSetting(dot_size=10),
            variable_name_suffix="test_circle_1",
        )
        assert_attrs(
            expected_attrs={
                "_x": 50,
                "_y": 100,
                "_radius": 150,
                "_fill_color": "#00aaff",
                "_fill_alpha": 0.5,
                "_line_color": "#ffffff",
                "_line_alpha": 0.3,
                "_line_thickness": 3,
                "_line_cap": ap.LineCaps.ROUND.value,
                "_line_dot_setting": ap.LineDotSetting(dot_size=10),
                "_parent": stage,
                "_variable_name_suffix": "test_circle_1",
            },
            any_obj=circle,
        )

        sprite: ap.Sprite = ap.Sprite()
        circle = ap.Circle(
            x=50,
            y=100,
            radius=150,
            line_dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),
            parent=sprite,
        )
        assert_attrs(
            expected_attrs={
                "_line_dash_setting": ap.LineDashSetting(dash_size=10, space_size=5),
                "_parent": sprite,
            },
            any_obj=circle,
        )

        circle = ap.Circle(
            x=50,
            y=100,
            radius=150,
            line_round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=5),
        )
        assert circle._line_round_dot_setting == ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )

        circle = ap.Circle(
            x=50,
            y=100,
            radius=150,
            line_dash_dot_setting=ap.LineDashDotSetting(
                dot_size=5, dash_size=10, space_size=5
            ),
        )
        assert circle._line_dash_dot_setting == ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=5
        )

    @apply_test_settings()
    def test___repr__(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        circle: ap.Circle = ap.Circle(parent=sprite.graphics, x=50, y=100, radius=30)
        repr_str: str = repr(circle)
        assert repr_str == f'Circle("{circle.variable_name}")'

    @apply_test_settings()
    def test__set_center_coordinates(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        circle: ap.Circle = ap.Circle(parent=sprite.graphics, x=50, y=100, radius=30)
        assert circle.x == 50
        assert circle.y == 100
        expression: str = expression_data_util.get_current_expression()
        assert f"{circle.variable_name}.cx(" in expression
        assert f"{circle.variable_name}.cy(" in expression

    @apply_test_settings()
    def test__create_with_graphics(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color="#0af", alpha=0.5)
        sprite.graphics.line_style(
            color="#fff",
            thickness=3,
            alpha=0.3,
            cap=ap.LineCaps.ROUND,
            joints=ap.LineJoints.BEVEL,
            dot_setting=ap.LineDotSetting(dot_size=10),
        )
        circle: ap.Circle = ap.Circle._create_with_graphics(
            graphics=sprite.graphics,
            x=50,
            y=100,
            radius=75,
            variable_name_suffix="test_circle",
        )
        assert_attrs(
            expected_attrs={
                "_x": 50,
                "_y": 100,
                "_radius": 75,
                "_fill_color": "#00aaff",
                "_fill_alpha": 0.5,
                "_line_color": "#ffffff",
                "_line_thickness": 3,
                "_line_alpha": 0.3,
                "_line_cap": ap.LineCaps.ROUND.value,
                "_line_dot_setting": ap.LineDotSetting(dot_size=10),
                "_parent": sprite.graphics,
                "_variable_name_suffix": "test_circle",
            },
            any_obj=circle,
        )

    @apply_test_settings()
    def test__initialize_with_base_value(self) -> None:
        circle: ap.Circle = ap.Circle._initialize_with_base_value()
        assert circle.x == ap.Number(-1)
        assert circle.y == ap.Number(-1)
        assert circle.radius == ap.Int(1)
        assert circle.visible == ap.Boolean(False)
