from random import randint

from retrying import retry

import apysc as ap
from tests.testing_helper import assert_attrs


class TestPathBezier2DContinual:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_bezier_2d_continual: ap.PathBezier2DContinual = \
            ap.PathBezier2DContinual(x=10, y=20, relative=True)
        assert_attrs(
            expected_attrs={
                '_path_label': ap.PathLabel.Bezier2DContinual,
                '_relative': True,
                '_x': 10,
                '_y': 20,
            },
            any_obj=path_bezier_2d_continual)
        assert isinstance(path_bezier_2d_continual._x, ap.Int)
        assert isinstance(path_bezier_2d_continual._y, ap.Int)
