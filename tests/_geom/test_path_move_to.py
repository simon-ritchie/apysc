import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestPathMoveTo:
    @apply_test_settings()
    def test___init__(self) -> None:
        path_move_to: ap.PathMoveTo = ap.PathMoveTo(
            x=50, y=100, relative=True, variable_name_suffix="test_path_move_to"
        )
        assert_attrs(
            expected_attrs={
                "_x": 50,
                "_y": 100,
                "_path_label": ap.PathLabel.MOVE_TO,
                "_relative": True,
            },
            any_obj=path_move_to,
        )
        assert isinstance(path_move_to._x, ap.Int)
        assert isinstance(path_move_to._y, ap.Int)
        assert path_move_to._variable_name_suffix == "test_path_move_to"
        assert path_move_to._x._variable_name_suffix == "test_path_move_to__x"
        assert path_move_to._y._variable_name_suffix == "test_path_move_to__y"

    @apply_test_settings()
    def test__get_svg_str(self) -> None:
        path_move_to: ap.PathMoveTo = ap.PathMoveTo(x=50, y=100)
        svg_str: str = path_move_to._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf"{var_names.STRING}_\d+? \+ "
                rf'String\({path_move_to._x.variable_name}\) \+ " " \+ '
                rf"String\({path_move_to._y.variable_name}\)"
            ),
            string=svg_str,
        )
        assert match is not None, svg_str

    @apply_test_settings()
    def test_update_path_data(self) -> None:
        path_move_to: ap.PathMoveTo = ap.PathMoveTo(
            x=50, y=100, relative=False, variable_name_suffix="test_path_move_to"
        )
        path_move_to.update_path_data(x=150, y=200, relative=True)
        assert_attrs(
            expected_attrs={
                "_x": 150,
                "_y": 200,
                "_relative": True,
            },
            any_obj=path_move_to,
        )
        assert path_move_to._x._variable_name_suffix == "test_path_move_to__x"
        assert path_move_to._y._variable_name_suffix == "test_path_move_to__y"
        assert (
            path_move_to._relative._variable_name_suffix
            == "test_path_move_to__relative"
        )

    @apply_test_settings()
    def test___eq__(self) -> None:
        path_move_to: ap.PathMoveTo = ap.PathMoveTo(x=50, y=100, relative=False)
        result: ap.Boolean = path_move_to == 10
        assert isinstance(result, ap.Boolean)
        assert not result

        other: ap.PathMoveTo = ap.PathMoveTo(x=100, y=100, relative=False)
        result = path_move_to == other
        assert isinstance(result, ap.Boolean)
        assert not result

        other = ap.PathMoveTo(x=50, y=50, relative=False)
        result = path_move_to == other
        assert not result

        other = ap.PathMoveTo(x=50, y=100, relative=True)
        result = path_move_to == other
        assert not result

        other = ap.PathMoveTo(x=50, y=100, relative=False)
        result = path_move_to == other
        assert result

    @apply_test_settings()
    def test___ne__(self) -> None:
        path_move_to: ap.PathMoveTo = ap.PathMoveTo(x=50, y=100, relative=False)
        other: ap.PathMoveTo = ap.PathMoveTo(x=100, y=100, relative=False)
        result: ap.Boolean = path_move_to != other
        assert isinstance(result, ap.Boolean)
        assert result
