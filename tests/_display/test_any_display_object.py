import apysc as ap
from apysc._display.any_display_object import AnyDisplayObject
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestAnyDisplayObject:
    @apply_test_settings()
    def test___init__(self) -> None:
        ap.Stage()
        any_display_object: AnyDisplayObject = AnyDisplayObject()
        assert any_display_object.variable_name.startswith(
            f"{var_names.ANY_DISPLAY_OBJECT}_"
        )
        expression: str = expression_data_util.get_current_expression()
        assert f"var {any_display_object.variable_name};" in expression

    @apply_test_settings()
    def test__initialize_for_loop_value(self) -> None:
        ap.Stage()
        any_display_object: AnyDisplayObject = (
            AnyDisplayObject._initialize_for_loop_value()
        )
        expression: str = expression_data_util.get_current_expression()
        assert f"var {any_display_object.variable_name};" in expression
        assert any_display_object.visible == ap.Boolean(False)
