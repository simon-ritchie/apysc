import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestPathBezier2D:
    @apply_test_settings()
    def test___init__(self) -> None:
        path_bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
            control_x=10,
            control_y=20,
            dest_x=30,
            dest_y=40,
            relative=True,
            variable_name_suffix="test_path_bezier_2d",
        )
        assert_attrs(
            expected_attrs={
                "_path_label": ap.PathLabel.BEZIER_2D,
                "_relative": True,
                "_control_x": 10,
                "_control_y": 20,
                "_dest_x": 30,
                "_dest_y": 40,
            },
            any_obj=path_bezier_2d,
        )
        assert isinstance(path_bezier_2d._control_x, ap.Number)
        assert isinstance(path_bezier_2d._control_y, ap.Number)
        assert isinstance(path_bezier_2d._dest_x, ap.Number)
        assert isinstance(path_bezier_2d._dest_y, ap.Number)
        assert path_bezier_2d._variable_name_suffix == "test_path_bezier_2d"
        assert (
            path_bezier_2d._control_x._variable_name_suffix
            == "test_path_bezier_2d__control_x"
        )
        assert (
            path_bezier_2d._control_y._variable_name_suffix
            == "test_path_bezier_2d__control_y"
        )
        assert (
            path_bezier_2d._dest_x._variable_name_suffix
            == "test_path_bezier_2d__dest_x"
        )
        assert (
            path_bezier_2d._dest_y._variable_name_suffix
            == "test_path_bezier_2d__dest_y"
        )

    @apply_test_settings()
    def test__get_svg_str(self) -> None:
        path_bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
            control_x=10, control_y=20, dest_x=30, dest_y=40
        )
        svg_str: str = path_bezier_2d._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf"{var_names.STRING}_\d+? \+ "
                rf"String\({path_bezier_2d._control_x.variable_name}\)"
                r' \+ " " \+ '
                rf"String\({path_bezier_2d._control_y.variable_name}\)"
                r' \+ " " \+ '
                rf"String\({path_bezier_2d._dest_x.variable_name}\)"
                r' \+ " " \+ '
                rf"String\({path_bezier_2d._dest_y.variable_name}\)"
            ),
            string=svg_str,
        )
        assert match is not None

    @apply_test_settings()
    def test_update_path_data(self) -> None:
        path_bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
            control_x=10,
            control_y=20,
            dest_x=30,
            dest_y=40,
            relative=False,
            variable_name_suffix="test_path_bezier_2d",
        )
        path_bezier_2d.update_path_data(
            control_x=100, control_y=200, dest_x=300, dest_y=400, relative=True
        )
        assert_attrs(
            expected_attrs={
                "_control_x": 100,
                "_control_y": 200,
                "_dest_x": 300,
                "_dest_y": 400,
                "_relative": True,
            },
            any_obj=path_bezier_2d,
        )
        assert (
            path_bezier_2d._control_x._variable_name_suffix
            == "test_path_bezier_2d__control_x"
        )
        assert (
            path_bezier_2d._control_y._variable_name_suffix
            == "test_path_bezier_2d__control_y"
        )
        assert (
            path_bezier_2d._dest_x._variable_name_suffix
            == "test_path_bezier_2d__dest_x"
        )
        assert (
            path_bezier_2d._dest_y._variable_name_suffix
            == "test_path_bezier_2d__dest_y"
        )

    @apply_test_settings()
    def test___eq__(self) -> None:
        path_bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
            control_x=10, control_y=20, dest_x=30, dest_y=40, relative=False
        )
        result: ap.Boolean = path_bezier_2d == 10
        assert isinstance(result, ap.Boolean)
        assert not result

        other: ap.PathBezier2D = ap.PathBezier2D(
            control_x=20, control_y=20, dest_x=30, dest_y=40, relative=False
        )
        result = path_bezier_2d == other
        assert isinstance(result, ap.Boolean)
        assert not result

        other = ap.PathBezier2D(
            control_x=10, control_y=10, dest_x=30, dest_y=40, relative=False
        )
        result = path_bezier_2d == other
        assert not result

        other = ap.PathBezier2D(
            control_x=10, control_y=10, dest_x=30, dest_y=40, relative=False
        )
        result = path_bezier_2d == other
        assert not result

        other = ap.PathBezier2D(
            control_x=10, control_y=20, dest_x=10, dest_y=40, relative=False
        )
        result = path_bezier_2d == other
        assert not result

        other = ap.PathBezier2D(
            control_x=10, control_y=20, dest_x=30, dest_y=10, relative=False
        )
        result = path_bezier_2d == other
        assert not result

        other = ap.PathBezier2D(
            control_x=10, control_y=20, dest_x=30, dest_y=40, relative=True
        )
        result = path_bezier_2d == other
        assert not result

        other = ap.PathBezier2D(
            control_x=10, control_y=20, dest_x=30, dest_y=40, relative=False
        )
        result = path_bezier_2d == other
        assert result

    @apply_test_settings()
    def test___ne__(self) -> None:
        path_bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
            control_x=10, control_y=20, dest_x=30, dest_y=40, relative=False
        )
        other: ap.PathBezier2D = ap.PathBezier2D(
            control_x=20, control_y=20, dest_x=30, dest_y=40, relative=False
        )
        result: ap.Boolean = path_bezier_2d != other
        assert isinstance(result, ap.Boolean)
        assert result
