import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._expression import var_names
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_svg_str(self) -> None:
        continual: ap.PathBezier3DContinual = \
            ap.PathBezier3DContinual(
                control_x=10, control_y=20, dest_x=30, dest_y=40)
        svg_str: str = continual._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf'{var_names.STRING}_\d+? \+ '
                rf'String\({continual._control_x.variable_name}\) \+ " " \+ '
                rf'String\({continual._control_y.variable_name}\) \+ " " \+ '
                rf'String\({continual._dest_x.variable_name}\) \+ " " \+ '
                rf'String\({continual._dest_y.variable_name}\)'
            ),
            string=svg_str)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_update_path_data(self) -> None:
        continual: ap.PathBezier3DContinual = \
            ap.PathBezier3DContinual(
                control_x=10, control_y=20, dest_x=30, dest_y=40,
                relative=False)
        continual.update_path_data(
            control_x=100, control_y=200, dest_x=300, dest_y=400,
            relative=True)
        assert_attrs(
            expected_attrs={
                '_control_x': 100,
                '_control_y': 200,
                '_dest_x': 300,
                '_dest_y': 400,
                '_relative': True,
            },
            any_obj=continual)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___eq__(self) -> None:
        continual: ap.PathBezier3DContinual = \
            ap.PathBezier3DContinual(
                control_x=10, control_y=20, dest_x=30, dest_y=40,
                relative=False)
        result: ap.Boolean = continual == 10
        assert isinstance(result, ap.Boolean)
        assert not result

        other: ap.PathBezier3DContinual = \
            ap.PathBezier3DContinual(
                control_x=20, control_y=20, dest_x=30, dest_y=40,
                relative=False)
        result = continual == other
        assert isinstance(result, ap.Boolean)
        assert not result

        other = ap.PathBezier3DContinual(
            control_x=20, control_y=20, dest_x=30, dest_y=40,
            relative=False)
        result = continual == other
        assert isinstance(result, ap.Boolean)
        assert not result

        other = ap.PathBezier3DContinual(
            control_x=10, control_y=10, dest_x=30, dest_y=40,
            relative=False)
        result = continual == other
        assert not result

        other = ap.PathBezier3DContinual(
            control_x=10, control_y=20, dest_x=20, dest_y=40,
            relative=False)
        result = continual == other
        assert not result

        other = ap.PathBezier3DContinual(
            control_x=10, control_y=20, dest_x=30, dest_y=30,
            relative=False)
        result = continual == other
        assert not result

        other = ap.PathBezier3DContinual(
            control_x=10, control_y=20, dest_x=30, dest_y=40,
            relative=True)
        result = continual == other
        assert not result

        other = ap.PathBezier3DContinual(
            control_x=10, control_y=20, dest_x=30, dest_y=40,
            relative=False)
        result = continual == other
        assert result

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___ne__(self) -> None:
        continual: ap.PathBezier3DContinual = \
            ap.PathBezier3DContinual(
                control_x=10, control_y=20, dest_x=30, dest_y=40,
                relative=False)
        other: ap.PathBezier3DContinual = \
            ap.PathBezier3DContinual(
                control_x=20, control_y=20, dest_x=30, dest_y=40,
                relative=False)
        result: ap.Boolean = continual != other
        assert isinstance(result, ap.Boolean)
        assert result
