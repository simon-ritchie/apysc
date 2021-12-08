import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestPathBezier2DContinual:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_bezier_2d_continual: ap.PathBezier2DContinual = \
            ap.PathBezier2DContinual(x=10, y=20, relative=True)
        assert_attrs(
            expected_attrs={
                '_path_label': ap.PathLabel.BEZIER_2D_CONTINUAL,
                '_relative': True,
                '_x': 10,
                '_y': 20,
            },
            any_obj=path_bezier_2d_continual)
        assert isinstance(path_bezier_2d_continual._x, ap.Int)
        assert isinstance(path_bezier_2d_continual._y, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_svg_str(self) -> None:
        path_bezier_2d_continual: ap.PathBezier2DContinual = \
            ap.PathBezier2DContinual(x=10, y=20)
        svg_str: str = path_bezier_2d_continual._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf'{var_names.STRING}_\d+? \+ '
                rf'String\({path_bezier_2d_continual._x.variable_name}\) \+ '
                r'" " \+ '
                rf'String\({path_bezier_2d_continual._y.variable_name}\)'
            ),
            string=svg_str)
        assert match is not None
