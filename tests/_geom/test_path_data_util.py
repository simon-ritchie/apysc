from random import randint

from retrying import retry

import apysc as ap
from apysc._geom import path_data_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_make_paths_expression_from_list() -> None:
    path_move_to: ap.PathMoveTo = ap.PathMoveTo(x=50, y=50)
    path_line_to: ap.PathLineTo = ap.PathLineTo(x=100, y=100)
    expression: str = path_data_util.make_paths_expression_from_list(
        path_data_list=[path_move_to, path_line_to])
    expected: str = (
        f'{path_move_to._get_svg_str()} + " " '
        f'+ {path_line_to._get_svg_str()}'
    )
    assert expression == expected
