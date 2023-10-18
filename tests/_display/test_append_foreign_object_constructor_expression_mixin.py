import apysc as ap
from apysc._display.append_foreign_object_constructor_expression_mixin import (
    AppendForeignObjectConstructorExpressionMixIn
)
from apysc._expression import expression_data_util
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._testing.testing_helper import apply_test_settings


class _TestObject(
    AppendForeignObjectConstructorExpressionMixIn,
    VariableNameMixIn,
):
    _width: ap.Int

    def __init__(self) -> None:
        """
        A class for testing.
        """
        self._variable_name = "test_object"
        self._width = ap.Int(100)


class TestAppendForeignObjectConstructorExpressionMixIn:
    @apply_test_settings()
    def test__append_foreign_object_constructor_expression(self) -> None:
        stage: ap.Stage = ap.get_stage()
        test_object: _TestObject = _TestObject()
        test_object._append_foreign_object_constructor_expression()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {test_object.variable_name} = {stage.variable_name}"
            f".foreignObject({test_object._width.variable_name}, 0);"
        )
        assert expected in expression
