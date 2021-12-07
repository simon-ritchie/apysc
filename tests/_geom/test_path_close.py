import re
from typing import Optional, Match
from random import randint

from retrying import retry

from apysc._expression import var_names
import apysc as ap
from tests.testing_helper import assert_attrs


class TestPathClose:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_close: ap.PathClose = ap.PathClose()
        assert_attrs(
            expected_attrs={
                '_path_label': ap.PathLabel.CLOSE,
                '_relative': False,
            },
            any_obj=path_close)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_path_close(self) -> None:
        path_close: ap.PathClose = ap.PathClose()
        svg_str: str = path_close._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=rf'{var_names.STRING}_\d+?$',
            string=svg_str)
        assert match is not None
