import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestPathHorizontal:
    @apply_test_settings()
    def test___init__(self) -> None:
        path_horizontal: ap.PathHorizontal = ap.PathHorizontal(
            x=50, relative=True, variable_name_suffix="test_path_horizontal"
        )
        assert_attrs(
            expected_attrs={
                "_x": 50,
                "_path_label": ap.PathLabel.HORIZONTAL,
                "_relative": True,
            },
            any_obj=path_horizontal,
        )
        assert isinstance(path_horizontal._x, ap.Number)
        assert path_horizontal._variable_name_suffix == "test_path_horizontal"
        assert path_horizontal._x._variable_name_suffix == "test_path_horizontal__x"

    @apply_test_settings()
    def test__get_svg_str(self) -> None:
        path_horizontal: ap.PathHorizontal = ap.PathHorizontal(x=50)
        svg_str = path_horizontal._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf"{var_names.STRING}_\d+? "
                rf"\+ String\({path_horizontal._x.variable_name}\)"
            ),
            string=svg_str,
        )
        assert match is not None

    @apply_test_settings()
    def test_update_path_data(self) -> None:
        path_horizontal: ap.PathHorizontal = ap.PathHorizontal(
            x=50, relative=False, variable_name_suffix="test_path_horizontal"
        )
        path_horizontal.update_path_data(x=100, relative=True)
        assert_attrs(
            expected_attrs={
                "_x": 100,
                "_relative": True,
            },
            any_obj=path_horizontal,
        )
        assert path_horizontal._x._variable_name_suffix == "test_path_horizontal__x"
        assert (
            path_horizontal._relative._variable_name_suffix
            == "test_path_horizontal__relative"
        )

    @apply_test_settings()
    def test___eq__(self) -> None:
        path_horizontal: ap.PathHorizontal = ap.PathHorizontal(x=50, relative=False)
        result: ap.Boolean = path_horizontal == 10
        assert isinstance(result, ap.Boolean)
        assert not result

        other: ap.PathHorizontal = ap.PathHorizontal(x=100, relative=False)
        result = path_horizontal == other
        assert isinstance(result, ap.Boolean)
        assert not result

        other = ap.PathHorizontal(x=50, relative=True)
        result = path_horizontal == other
        assert not result

        other = ap.PathHorizontal(x=50, relative=False)
        result = path_horizontal == other
        assert result

    @apply_test_settings()
    def test___ne__(self) -> None:
        path_horizontal: ap.PathHorizontal = ap.PathHorizontal(x=50, relative=False)
        other: ap.PathHorizontal = ap.PathHorizontal(x=100, relative=False)
        result: ap.Boolean = path_horizontal != other
        assert isinstance(result, ap.Boolean)
        assert result
