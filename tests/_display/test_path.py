from random import randint
from typing import List

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._geom import path_data_util
from tests.testing_helper import assert_attrs


class TestPath:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        path_data_list: List[ap.PathDataBase] = [
            ap.PathData.MoveTo(x=500, y=100),
        ]
        sprite.graphics.begin_fill(color='#0af')
        path: ap.Path = ap.Path(
            parent=sprite.graphics, path_data_list=path_data_list)
        assert path.variable_name.startswith(f'{var_names.PATH}_')
        assert_attrs(
            expected_attrs={
                '_fill_color': '#00aaff',
                '_path_data_list': path_data_list,
            },
            any_obj=path,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        path_data_list: List[ap.PathDataBase] = [
            ap.PathData.MoveTo(x=500, y=100),
        ]
        path: ap.Path = ap.Path(
            parent=sprite.graphics, path_data_list=path_data_list)
        repr_str: str = repr(path)
        assert repr_str == f"Path('{path.variable_name}')"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        path_move_to: ap.PathMoveTo = ap.PathData.MoveTo(x=500, y=100)
        path_data_list: List[ap.PathDataBase] = [path_move_to]
        path: ap.Path = ap.Path(
            parent=sprite.graphics, path_data_list=path_data_list)
        expression: str = expression_data_util.get_current_expression()
        path_data_expression: str = \
            path_data_util.make_paths_expression_from_list(
                path_data_list=path_data_list)
        expected_expressions: List[str] = [
            f'var {path.variable_name} = {stage.variable_name}',
            f'\n  .path({path_data_expression})',
            '\n  .attr({',
            '\n    fill: "transparent",',
            '\n  });'
        ]
        for expected in expected_expressions:
            assert expected in expression, expected
