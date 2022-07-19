import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import assert_attrs


class TestPathBezier2DContinual:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_bezier_2d_continual: ap.PathBezier2DContinual = ap.PathBezier2DContinual(
            x=10,
            y=20,
            relative=True,
            variable_name_suffix="test_path_bezier_2d_continual",
        )
        assert_attrs(
            expected_attrs={
                "_path_label": ap.PathLabel.BEZIER_2D_CONTINUAL,
                "_relative": True,
                "_x": 10,
                "_y": 20,
                "_variable_name_suffix": "test_path_bezier_2d_continual",
            },
            any_obj=path_bezier_2d_continual,
        )
        assert isinstance(path_bezier_2d_continual._x, ap.Int)
        assert isinstance(path_bezier_2d_continual._y, ap.Int)
        assert (
            path_bezier_2d_continual._x._variable_name_suffix
            == "test_path_bezier_2d_continual__x"
        )
        assert (
            path_bezier_2d_continual._y._variable_name_suffix
            == "test_path_bezier_2d_continual__y"
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_svg_str(self) -> None:
        path_bezier_2d_continual: ap.PathBezier2DContinual = ap.PathBezier2DContinual(
            x=10, y=20
        )
        svg_str: str = path_bezier_2d_continual._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf"{var_names.STRING}_\d+? \+ "
                rf"String\({path_bezier_2d_continual._x.variable_name}\) \+ "
                r'" " \+ '
                rf"String\({path_bezier_2d_continual._y.variable_name}\)"
            ),
            string=svg_str,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_update_path_data(self) -> None:
        path_bezier_2d_continual: ap.PathBezier2DContinual = ap.PathBezier2DContinual(
            x=10,
            y=20,
            relative=False,
            variable_name_suffix="test_path_bezier_2d_continual",
        )
        path_bezier_2d_continual.update_path_data(x=100, y=200, relative=True)
        assert_attrs(
            expected_attrs={
                "_x": 100,
                "_y": 200,
                "_relative": True,
            },
            any_obj=path_bezier_2d_continual,
        )
        path_bezier_2d_continual._x._variable_name_suffix = (
            "test_path_bezier_2d_continual__x"
        )
        path_bezier_2d_continual._y._variable_name_suffix = (
            "test_path_bezier_2d_continual__y"
        )
        path_bezier_2d_continual._relative._variable_name_suffix = (
            "test_path_bezier_2d_continual__relative"
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___eq__(self) -> None:
        path_bezier_2d_continual: ap.PathBezier2DContinual = ap.PathBezier2DContinual(
            x=10, y=20, relative=False
        )
        result: ap.Boolean = path_bezier_2d_continual == 10
        assert isinstance(result, ap.Boolean)
        assert not result

        other: ap.PathBezier2DContinual = ap.PathBezier2DContinual(
            x=20, y=20, relative=False
        )
        result = path_bezier_2d_continual == other
        assert isinstance(result, ap.Boolean)
        assert not result

        other = ap.PathBezier2DContinual(x=10, y=10, relative=False)
        result = path_bezier_2d_continual == other
        assert not result

        other = ap.PathBezier2DContinual(x=10, y=20, relative=True)
        result = path_bezier_2d_continual == other
        assert not result

        other = ap.PathBezier2DContinual(x=10, y=20, relative=False)
        result = path_bezier_2d_continual == other
        assert isinstance(result, ap.Boolean)
        assert result

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___ne__(self) -> None:
        path_bezier_2d_continual: ap.PathBezier2DContinual = ap.PathBezier2DContinual(
            x=10, y=20, relative=False
        )
        other: ap.PathBezier2DContinual = ap.PathBezier2DContinual(
            x=10, y=10, relative=False
        )
        result: ap.Boolean = path_bezier_2d_continual != other
        assert isinstance(result, ap.Boolean)
        assert result

        other = ap.PathBezier2DContinual(x=10, y=20, relative=False)
        result = path_bezier_2d_continual != other
        assert not result
