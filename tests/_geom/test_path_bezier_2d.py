from random import randint
import re
from typing import Match, Optional

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestPathBezier2D:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
            control_x=10, control_y=20, dest_x=30, dest_y=40,
            relative=True)
        assert_attrs(
            expected_attrs={
                '_path_label': ap.PathLabel.BEZIER_2D,
                '_relative': True,
                '_control_x': 10,
                '_control_y': 20,
                '_dest_x': 30,
                '_dest_y': 40,
            },
            any_obj=path_bezier_2d,
        )
        assert isinstance(path_bezier_2d._control_x, ap.Int)
        assert isinstance(path_bezier_2d._control_y, ap.Int)
        assert isinstance(path_bezier_2d._dest_x, ap.Int)
        assert isinstance(path_bezier_2d._dest_y, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_svg_str(self) -> None:
        path_bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
            control_x=10, control_y=20, dest_x=30, dest_y=40)
        svg_str: str = path_bezier_2d._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf'Q {var_names.INT}_\d+? {var_names.INT}_\d+? '
                rf'{var_names.INT}_\d+? {var_names.INT}_\d+?$'),
            string=svg_str)
        assert match is not None
