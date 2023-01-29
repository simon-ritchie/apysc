import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import var_names
from apysc._geom import path_data_util
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_make_paths_expression_from_list() -> None:
    path_move_to: ap.PathMoveTo = ap.PathMoveTo(x=50, y=50)
    path_line_to: ap.PathLineTo = ap.PathLineTo(x=100, y=100)
    expression: str = path_data_util.make_paths_expression_from_list(
        path_data_list=[path_move_to, path_line_to]
    )
    match: Optional[Match] = re.search(
        pattern=(
            rf'{var_names.STRING}_\d+? \+ .+?" " ' rf".+?\+ {var_names.STRING}_\d+? .+?"
        ),
        string=expression,
        flags=re.MULTILINE | re.DOTALL,
    )
    assert match is not None, expression
