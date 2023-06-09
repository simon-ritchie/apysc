import re
from typing import List
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestPath:
    @apply_test_settings()
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        path_data_list: List[ap.PathDataBase] = [
            ap.PathData.MoveTo(x=500, y=100),
        ]
        path: ap.Path = ap.Path(
            path_data_list=path_data_list,
            fill_color="#0af",
            fill_alpha=0.5,
            line_color="fff",
            line_alpha=0.3,
            line_thickness=3,
            line_cap=ap.LineCaps.ROUND,
            line_joints=ap.LineJoints.BEVEL,
            line_dot_setting=ap.LineDotSetting(dot_size=10),
            variable_name_suffix="test_path",
        )
        assert_attrs(
            expected_attrs={
                "_path_data_list": path_data_list,
                "_fill_color": "#00aaff",
                "_fill_alpha": 0.5,
                "_line_color": "#ffffff",
                "_line_alpha": 0.3,
                "_line_thickness": 3,
                "_line_cap": ap.LineCaps.ROUND.value,
                "_line_joints": ap.LineJoints.BEVEL.value,
                "_line_dot_setting": ap.LineDotSetting(dot_size=10),
                "_parent": stage,
                "_variable_name_suffix": "test_path",
            },
            any_obj=path,
        )

        sprite: ap.Sprite = ap.Sprite()
        path = ap.Path(
            path_data_list=path_data_list,
            line_dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),
            parent=sprite,
        )
        assert_attrs(
            expected_attrs={
                "_line_dash_setting": ap.LineDashSetting(dash_size=10, space_size=5),
                "_parent": sprite,
            },
            any_obj=path,
        )

        path = ap.Path(
            path_data_list=path_data_list,
            line_round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=5),
        )
        assert path._line_round_dot_setting == ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )

        path = ap.Path(
            path_data_list=path_data_list,
            line_dash_dot_setting=ap.LineDashDotSetting(
                dot_size=5, dash_size=10, space_size=3
            ),
        )
        assert path._line_dash_dot_setting == ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=3
        )

    @apply_test_settings()
    def test___repr__(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        path_data_list: List[ap.PathDataBase] = [
            ap.PathData.MoveTo(x=500, y=100),
        ]
        path: ap.Path = sprite.graphics.draw_path(path_data_list=path_data_list)
        repr_str: str = repr(path)
        assert repr_str == f'Path("{path.variable_name}")'

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        path_move_to: ap.PathMoveTo = ap.PathData.MoveTo(x=500, y=100)
        path_data_list: List[ap.PathDataBase] = [path_move_to]
        path: ap.Path = sprite.graphics.draw_path(path_data_list=path_data_list)
        expression: str = expression_data_util.get_current_expression()
        expected_epx_patterns: List[str] = [
            rf"var {path.variable_name} = {stage.variable_name}",
            r"\n  .path\(.+?\)",
            r"\n  .attr\(\{",
            r'\n    fill: "transparent",',
            r"\n  \}\);",
        ]
        for expected in expected_epx_patterns:
            match: Optional[Match] = re.search(
                pattern=expected, string=expression, flags=re.MULTILINE | re.DOTALL
            )
            assert match is not None, f"{expected}, \n\n{expression}\n\n"

    @apply_test_settings()
    def test__create_with_graphics(self) -> None:
        ap.Stage()
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
        path_data_list: List[ap.PathDataBase] = [
            ap.PathData.MoveTo(x=500, y=100),
        ]
        path: ap.Path = ap.Path._create_with_graphics(
            graphics=sprite.graphics,
            path_data_list=path_data_list,
            variable_name_suffix="test_path",
        )
        assert_attrs(
            expected_attrs={
                "_path_data_list": path_data_list,
                "_fill_color": "#00aaff",
                "_fill_alpha": 0.5,
                "_line_color": "#ffffff",
                "_line_alpha": 0.3,
                "_line_cap": ap.LineCaps.ROUND.value,
                "_line_joints": ap.LineJoints.BEVEL.value,
                "_line_dot_setting": ap.LineDotSetting(dot_size=10),
                "_parent": sprite.graphics,
                "_variable_name_suffix": "test_path",
            },
            any_obj=path,
        )

    @apply_test_settings()
    def test__initialize_for_loop_value(self) -> None:
        ap.Stage()
        path: ap.Path = ap.Path._initialize_for_loop_value()
        assert path._path_data_list == [
            ap.PathMoveTo(x=-2, y=-2),
            ap.PathLineTo(x=-1, y=-1),
        ]
