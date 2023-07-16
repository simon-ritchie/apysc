import apysc as ap
from apysc._display.any_display_object import AnyDisplayObject
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestDisplayObject:
    @apply_test_settings()
    def test___init__(self) -> None:
        display_object: AnyDisplayObject = AnyDisplayObject()
        assert var_names.ANY_DISPLAY_OBJECT in display_object.variable_name

    @apply_test_settings()
    def test_variable_name(self) -> None:
        ap.Stage()
        display_object: AnyDisplayObject = AnyDisplayObject()
        display_object.variable_name = "test_display_object_1"
        assert display_object.variable_name == "test_display_object_1"

    @apply_test_settings()
    def test__set_overflow_visible_setting(self) -> None:
        ap.Stage()
        display_object: AnyDisplayObject = AnyDisplayObject()
        display_object._set_overflow_visible_setting()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{display_object.variable_name}.css("overflow", "visible");'
        assert expected in expression
