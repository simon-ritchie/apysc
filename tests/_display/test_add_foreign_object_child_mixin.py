from apysc._display.add_foreign_object_child_mixin import AddForeignObjectChildMixIn
from apysc._display.svg_foreign_object_child import SvgForeignObjectChild
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestObject(AddForeignObjectChildMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """
        A class for testing.
        """
        self.variable_name = "test_object"


class TestAddForeignObjectChildMixIn:
    @apply_test_settings()
    def test__add_foreign_object_child(self) -> None:
        foreign_object: _TestObject = _TestObject()
        foreign_object_child: SvgForeignObjectChild = SvgForeignObjectChild(
            html_str="<div></div>",
        )
        foreign_object._add_foreign_object_child(child=foreign_object_child)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{foreign_object.variable_name}.add({foreign_object_child.variable_name});"
        )
        assert expected in expression
