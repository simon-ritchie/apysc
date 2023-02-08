import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestPathVertical:
    @apply_test_settings()
    def test___init__(self) -> None:
        path_vertical: ap.PathVertical = ap.PathVertical(
            y=50, relative=True, variable_name_suffix="test_path_vertical"
        )
        assert_attrs(
            expected_attrs={
                "_y": 50,
                "_path_label": ap.PathLabel.VERTICAL,
                "_relative": True,
            },
            any_obj=path_vertical,
        )
        assert isinstance(path_vertical._y, ap.Number)
        assert path_vertical._variable_name_suffix == "test_path_vertical"
        assert path_vertical._y._variable_name_suffix == "test_path_vertical__y"

    @apply_test_settings()
    def test__get_svg_str(self) -> None:
        path_vertical: ap.PathVertical = ap.PathVertical(y=50)
        svg_str: str = path_vertical._get_svg_str()
        match: Optional[Match] = re.match(
            pattern=(
                rf"{var_names.STRING}_\d+? "
                rf"\+ String\({path_vertical._y.variable_name}\)"
            ),
            string=svg_str,
        )
        assert match is not None

    @apply_test_settings()
    def test_update_path_data(self) -> None:
        path_vertical: ap.PathVertical = ap.PathVertical(
            y=50, relative=False, variable_name_suffix="test_path_vertical"
        )
        path_vertical.update_path_data(y=100, relative=True)
        assert_attrs(
            expected_attrs={
                "_y": 100,
                "_relative": True,
            },
            any_obj=path_vertical,
        )
        assert path_vertical._y._variable_name_suffix == "test_path_vertical__y"
        assert (
            path_vertical._relative._variable_name_suffix
            == "test_path_vertical__relative"
        )

    @apply_test_settings()
    def test___eq__(self) -> None:
        path_vertical: ap.PathVertical = ap.PathVertical(y=50, relative=False)
        result: ap.Boolean = path_vertical == 10
        assert isinstance(result, ap.Boolean)
        assert not result

        other: ap.PathVertical = ap.PathVertical(y=100, relative=False)
        result = path_vertical == other
        assert isinstance(result, ap.Boolean)
        assert not result

        other = ap.PathVertical(y=50, relative=True)
        result = path_vertical == other
        assert not result

        other = ap.PathVertical(y=50, relative=False)
        result = path_vertical == other
        assert result

    @apply_test_settings()
    def test___ne__(self) -> None:
        path_vertical: ap.PathVertical = ap.PathVertical(y=50, relative=False)
        other: ap.PathVertical = ap.PathVertical(y=100, relative=False)
        result: ap.Boolean = path_vertical != other
        assert isinstance(result, ap.Boolean)
        assert result
