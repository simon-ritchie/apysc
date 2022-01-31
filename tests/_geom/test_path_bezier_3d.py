import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestPathBezier3D:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_bezier_3d: ap.PathBezier3D = ap.PathBezier3D(
            control_x1=10, control_y1=20, control_x2=30, control_y2=40,
            dest_x=50, dest_y=60, relative=True)
        assert_attrs(
            expected_attrs={
                '_path_label': ap.PathLabel.BEZIER_3D,
                '_relative': True,
                '_control_x1': 10,
                '_control_y1': 20,
                '_control_x2': 30,
                '_control_y2': 40,
                '_dest_x': 50,
                '_dest_y': 60,
            },
            any_obj=path_bezier_3d)
        assert isinstance(path_bezier_3d._control_x1, ap.Int)
        assert isinstance(path_bezier_3d._control_y1, ap.Int)
        assert isinstance(path_bezier_3d._control_x2, ap.Int)
        assert isinstance(path_bezier_3d._control_y2, ap.Int)
        assert isinstance(path_bezier_3d._dest_x, ap.Int)
        assert isinstance(path_bezier_3d._dest_y, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_svg_str(self) -> None:
        path_bezier_3d: ap.PathBezier3D = ap.PathBezier3D(
            control_x1=10, control_y1=20, control_x2=30, control_y2=40,
            dest_x=50, dest_y=60)
        svg_str: str = path_bezier_3d._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf'{var_names.STRING}_\d+? \+ '
                rf'String\({path_bezier_3d._control_x1.variable_name}\)'
                r' \+ " " \+ '
                rf'String\({path_bezier_3d._control_y1.variable_name}\)'
                r' \+ " " \+ '
                rf'String\({path_bezier_3d._control_x2.variable_name}\)'
                r' \+ " " \+ '
                rf'String\({path_bezier_3d._control_y2.variable_name}\)'
                r' \+ " " \+ '
                rf'String\({path_bezier_3d._dest_x.variable_name}\)'
                r' \+ " " \+ '
                rf'String\({path_bezier_3d._dest_y.variable_name}\)'
            ),
            string=svg_str)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_update_path_data(self) -> None:
        path_bezier_3d: ap.PathBezier3D = ap.PathBezier3D(
            control_x1=10, control_y1=20, control_x2=30, control_y2=40,
            dest_x=50, dest_y=60, relative=False)
        path_bezier_3d.update_path_data(
            control_x1=100, control_y1=200, control_x2=300,
            control_y2=400, dest_x=500, dest_y=600, relative=True)
        assert_attrs(
            expected_attrs={
                '_control_x1': 100,
                '_control_y1': 200,
                '_control_x2': 300,
                '_control_y2': 400,
                '_dest_x': 500,
                '_dest_y': 600,
                '_relative': True,
            },
            any_obj=path_bezier_3d)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___eq__(self) -> None:
        path_bezier_3d: ap.PathBezier3D = ap.PathBezier3D(
            control_x1=10, control_y1=20, control_x2=30, control_y2=40,
            dest_x=50, dest_y=60, relative=False)
        result: ap.Boolean = path_bezier_3d == 10
        assert isinstance(result, ap.Boolean)
        assert not result

        other: ap.PathBezier3D = ap.PathBezier3D(
            control_x1=20, control_y1=20, control_x2=30, control_y2=40,
            dest_x=50, dest_y=60, relative=False)
        result = path_bezier_3d == other
        assert isinstance(result, ap.Boolean)
        assert not result

        other = ap.PathBezier3D(
            control_x1=10, control_y1=10, control_x2=30, control_y2=40,
            dest_x=50, dest_y=60, relative=False)
        result = path_bezier_3d == other
        assert not result

        other = ap.PathBezier3D(
            control_x1=10, control_y1=20, control_x2=20, control_y2=40,
            dest_x=50, dest_y=60, relative=False)
        result = path_bezier_3d == other
        assert not result

        other = ap.PathBezier3D(
            control_x1=10, control_y1=20, control_x2=30, control_y2=30,
            dest_x=50, dest_y=60, relative=False)
        result = path_bezier_3d == other
        assert not result

        other = ap.PathBezier3D(
            control_x1=10, control_y1=20, control_x2=30, control_y2=40,
            dest_x=40, dest_y=60, relative=False)
        result = path_bezier_3d == other
        assert not result

        other = ap.PathBezier3D(
            control_x1=10, control_y1=20, control_x2=30, control_y2=40,
            dest_x=50, dest_y=50, relative=False)
        result = path_bezier_3d == other
        assert not result

        other = ap.PathBezier3D(
            control_x1=10, control_y1=20, control_x2=30, control_y2=40,
            dest_x=50, dest_y=60, relative=True)
        result = path_bezier_3d == other
        assert not result

        other = ap.PathBezier3D(
            control_x1=10, control_y1=20, control_x2=30, control_y2=40,
            dest_x=50, dest_y=60, relative=False)
        result = path_bezier_3d == other
        assert result

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___ne__(self) -> None:
        path_bezier_3d: ap.PathBezier3D = ap.PathBezier3D(
            control_x1=10, control_y1=20, control_x2=30, control_y2=40,
            dest_x=50, dest_y=60, relative=False)
        other: ap.PathBezier3D = ap.PathBezier3D(
            control_x1=20, control_y1=20, control_x2=30, control_y2=40,
            dest_x=50, dest_y=60, relative=False)
        result: ap.Boolean = path_bezier_3d != other
        assert isinstance(result, ap.Boolean)
        assert result
