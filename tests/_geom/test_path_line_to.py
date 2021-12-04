from random import randint
import re
from typing import Match, Optional

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestPathLineTo:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_line_to: ap.PathLineTo = ap.PathLineTo(
            x=50, y=100, relative=True)
        assert_attrs(
            expected_attrs={
                '_x': 50,
                '_y': 100,
                '_path_label': ap.PathLabel.LINE_TO,
                '_relative': True,
            },
            any_obj=path_line_to,
        )
        assert isinstance(path_line_to._x, ap.Int)
        assert isinstance(path_line_to._y, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_svg_str(self) -> None:
        path_line_to: ap.PathLineTo = ap.PathLineTo(x=50, y=100)
        svg_str: str = path_line_to._get_svg_str()
        expected: str = (
            f'L {path_line_to._x.variable_name} '
            f'{path_line_to._y.variable_name}'
        )
        assert svg_str == expected
