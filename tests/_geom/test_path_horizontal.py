import re
from random import randint
from typing import Optional, Match

from retrying import retry

from apysc._expression import var_names
import apysc as ap
from tests.testing_helper import assert_attrs


class TestPathHorizontal:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_horizontal: ap.PathHorizontal = ap.PathHorizontal(
            x=50, relative=True)
        assert_attrs(
            expected_attrs={
                '_x': 50,
                '_path_label': ap.PathLabel.HORIZONTAL,
                '_relative': True,
            },
            any_obj=path_horizontal)
        assert isinstance(path_horizontal._x, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_svg_str(self) -> None:
        path_horizontal: ap.PathHorizontal = ap.PathHorizontal(x=50)
        svg_str = path_horizontal._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf'{var_names.STRING}_\d+? '
                rf'\+ String\({path_horizontal._x.variable_name}\)'
            ),
            string=svg_str)
        assert match is not None
