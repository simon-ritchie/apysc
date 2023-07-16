import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestPathDataBase:
    @apply_test_settings()
    def test___init__(self) -> None:
        path_data: ap.PathMoveTo = ap.PathMoveTo(
            x=10, y=20, relative=True, variable_name_suffix="test_path_data"
        )
        assert_attrs(
            expected_attrs={"_path_label": ap.PathLabel.MOVE_TO, "_relative": True},
            any_obj=path_data,
        )
        assert isinstance(path_data._relative, ap.Boolean)
        assert path_data._relative._variable_name_suffix == "test_path_data__relative"

    @apply_test_settings()
    def test__get_svg_char(self) -> None:
        ap.Stage()
        path_data: ap.PathMoveTo = ap.PathMoveTo(
            x=10, y=20, relative=False, variable_name_suffix="test_path_data"
        )
        svg_char: ap.String = path_data._get_svg_char()
        assert svg_char == "M"
        assert isinstance(svg_char, ap.String)
        assert svg_char._variable_name_suffix == "test_path_data"
        expression: str = expression_data_util.get_current_expression()
        assert "if (" in expression
        assert "else {" in expression

        path_data = ap.PathMoveTo(x=10, y=20, relative=True)
        svg_char = path_data._get_svg_char()
        assert svg_char == "m"
        assert isinstance(svg_char, ap.String)
