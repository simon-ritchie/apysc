from random import randint

from retrying import retry

import apysc as ap
from tests.testing_helper import assert_attrs


class TestPathBezier3DContinual:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_bezier_3d_continual: ap.PathBezier3DContinual = \
            ap.PathBezier3DContinual(
                control_x=10, control_y=20, dest_x=30, dest_y=40,
                relative=True)
        assert_attrs(
            expected_attrs={
                '_path_label': ap.PathLabel.BEZIER_3D_CONTINUAL,
                '_relative': True,
                '_control_x': 10,
                '_control_y': 20,
                '_dest_x': 30,
                '_dest_y': 40,
            },
            any_obj=path_bezier_3d_continual)
        assert isinstance(path_bezier_3d_continual._control_x, ap.Int)
        assert isinstance(path_bezier_3d_continual._control_y, ap.Int)
        assert isinstance(path_bezier_3d_continual._dest_x, ap.Int)
        assert isinstance(path_bezier_3d_continual._dest_y, ap.Int)
