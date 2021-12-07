import re
from typing import Optional, Match
from random import randint

from retrying import retry

from apysc._expression import var_names
import apysc as ap
from tests.testing_helper import assert_attrs


class TestPathVertical:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_vertical: ap.PathVertical = ap.PathVertical(
            y=50, relative=True)
        assert_attrs(
            expected_attrs={
                '_y': 50,
                '_path_label': ap.PathLabel.VERTICAL,
                '_relative': True,
            },
            any_obj=path_vertical,
        )
        assert isinstance(path_vertical._y, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_svg_str(self) -> None:
        path_vertical: ap.PathVertical = ap.PathVertical(y=50)
        svg_str: str = path_vertical._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf'{var_names.STRING}_\d+? '
                rf'\+ String\({path_vertical._y.variable_name}\)'
            ),
            string=svg_str)
        assert match is not None
