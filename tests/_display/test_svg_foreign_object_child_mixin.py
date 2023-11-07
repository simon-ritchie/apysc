from apysc._display.add_foreign_object_child_mixin import AddForeignObjectChildMixIn
from apysc._display.svg_foreign_object_child_mixin import SvgForeignObjectChildMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestValidObject(
    SvgForeignObjectChildMixIn,
    AddForeignObjectChildMixIn,
    VariableNameMixIn,
):
    def __init__(self) -> None:
        """
        The test class for the valid case.
        """
        self.variable_name = "test_valid_object"


class _TestInvalidObject(
    SvgForeignObjectChildMixIn,
    VariableNameMixIn,
):
    def __init__(self) -> None:
        """
        The test class for the invalid case.
        """
        self.variable_name = "test_invalid_object"


class TestSvgForeignObjectChildMixIn:
    @apply_test_settings()
    def test__initialize_svg_foreign_object_child(self) -> None:
        valid_object: _TestValidObject = _TestValidObject()
        valid_object._initialize_svg_foreign_object_child(
            html_str="<p>test</p>",
            variable_name_suffix="test_suffix",
        )
        assert valid_object._svg_foreign_object_child._html_str == "<p>test</p>"
        assert (
            valid_object._svg_foreign_object_child._variable_name_suffix
            == "test_suffix"
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{valid_object.variable_name}"
            f".add({valid_object._svg_foreign_object_child.variable_name});"
        )
        assert expected in expression

        invalid_object: _TestInvalidObject = _TestInvalidObject()
        assert_raises(
            expected_error_class=TypeError,
            callable_=invalid_object._initialize_svg_foreign_object_child,
            html_str="<p>test</p>",
        )
