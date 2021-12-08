import re
from random import randint
from typing import Optional, Match

from retrying import retry

import apysc as ap
from apysc._geom import path_data_util
from apysc._expression import var_names


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_make_paths_expression_from_list() -> None:
    path_move_to: ap.PathMoveTo = ap.PathMoveTo(x=50, y=50)
    path_line_to: ap.PathLineTo = ap.PathLineTo(x=100, y=100)
    expression: str = path_data_util.make_paths_expression_from_list(
        path_data_list=[path_move_to, path_line_to])
    match: Optional[Match] = re.search(
        pattern=(
            rf'{var_names.STRING}_\d+? \+ .+?" " '
            rf'.+?\+ {var_names.STRING}_\d+? .+?'
        ),
        string=expression,
        flags=re.MULTILINE | re.DOTALL,
    )
    assert match is not None, expression
