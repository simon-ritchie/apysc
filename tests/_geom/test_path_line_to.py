import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestPathLineTo:
    @apply_test_settings()
    def test___init__(self) -> None:
        path_line_to: ap.PathLineTo = ap.PathLineTo(
            x=50, y=100, relative=True, variable_name_suffix="test_path_line_to"
        )
        assert_attrs(
            expected_attrs={
                "_x": 50,
                "_y": 100,
                "_path_label": ap.PathLabel.LINE_TO,
                "_relative": True,
            },
            any_obj=path_line_to,
        )
        assert isinstance(path_line_to._x, ap.Number)
        assert isinstance(path_line_to._y, ap.Number)
        assert path_line_to._variable_name_suffix == "test_path_line_to"
        assert path_line_to._x._variable_name_suffix == "test_path_line_to__x"
        assert path_line_to._y._variable_name_suffix == "test_path_line_to__y"

    @apply_test_settings()
    def test__get_svg_str(self) -> None:
        path_line_to: ap.PathLineTo = ap.PathLineTo(x=50, y=100)
        svg_str: str = path_line_to._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf"{var_names.STRING}_\d+? \+ "
                rf"String\({path_line_to._x.variable_name}\) \+ "
                rf'" " \+ String\({path_line_to._y.variable_name}\)'
            ),
            string=svg_str,
        )
        assert match is not None

    @apply_test_settings()
    def test_update_path_data(self) -> None:
        path_line_to: ap.PathLineTo = ap.PathLineTo(
            x=50, y=100, relative=False, variable_name_suffix="test_path_line_to"
        )
        path_line_to.update_path_data(x=150, y=200, relative=True)
        assert_attrs(
            expected_attrs={
                "_x": 150,
                "_y": 200,
                "_relative": True,
            },
            any_obj=path_line_to,
        )
        assert path_line_to._x._variable_name_suffix == "test_path_line_to__x"
        assert path_line_to._y._variable_name_suffix == "test_path_line_to__y"
        assert (
            path_line_to._relative._variable_name_suffix
            == "test_path_line_to__relative"
        )

    @apply_test_settings()
    def test___eq__(self) -> None:
        path_line_to: ap.PathLineTo = ap.PathLineTo(x=50, y=100, relative=False)
        result: ap.Boolean = path_line_to == 10
        assert isinstance(result, ap.Boolean)
        assert not result

        other: ap.PathLineTo = ap.PathLineTo(x=100, y=100, relative=False)
        result = path_line_to == other
        assert isinstance(result, ap.Boolean)
        assert not result

        other = ap.PathLineTo(x=50, y=50, relative=False)
        result = path_line_to == other
        assert not result

        other = ap.PathLineTo(x=50, y=100, relative=True)
        result = path_line_to == other
        assert not result

        other = ap.PathLineTo(x=50, y=100, relative=False)
        result = path_line_to == other
        assert result

    @apply_test_settings()
    def test___ne__(self) -> None:
        path_line_to: ap.PathLineTo = ap.PathLineTo(x=50, y=100, relative=False)
        other: ap.PathLineTo = ap.PathLineTo(x=100, y=100, relative=False)
        result: ap.Boolean = path_line_to != other
        assert isinstance(result, ap.Boolean)
        assert result
