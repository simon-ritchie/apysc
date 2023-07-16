from typing import Any
from typing import Dict

import apysc as ap
from apysc._event.mouse_down_mixin import MouseDownMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestMouseDown(MouseDownMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """Test class for mouse down testing."""
        self.variable_name = "test_mouse_down"


class TestMouseDownMixIn:
    def on_mouse_down_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse down handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_mouse_down_2(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse down handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @apply_test_settings()
    def test__initialize_mouse_down_handlers_if_not_initialized(self) -> None:
        mixin_1: MouseDownMixIn = MouseDownMixIn()
        mixin_1._initialize_mouse_down_handlers_if_not_initialized()
        assert mixin_1._mouse_down_handlers == {}

        mixin_1._initialize_mouse_down_handlers_if_not_initialized()
        assert mixin_1._mouse_down_handlers == {}

    @apply_test_settings()
    def test_mousedown(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseDown = _TestMouseDown()
        name: str = mixin_1.mousedown(
            handler=self.on_mouse_down_1, options={"msg": "Hello!"}
        )
        assert name in mixin_1._mouse_down_handlers
        expression: str = (
            expression_data_util.get_current_event_handler_scope_expression()
        )
        expected: str = f"function {name}("
        assert expected in expression

        expression = expression_data_util.get_current_expression()
        expected = f"{mixin_1.variable_name}.mousedown({name});"
        assert expected in expression

    @apply_test_settings()
    def test_unbind_mousedown(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseDown = _TestMouseDown()
        name = mixin_1.mousedown(handler=self.on_mouse_down_1)
        mixin_1.unbind_mousedown(handler=self.on_mouse_down_1)
        assert mixin_1._mouse_down_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}.off("
            f'"{ap.MouseEventType.MOUSEDOWN.value}", {name});'
        )
        assert expected in expression

    @apply_test_settings()
    def test_unbind_mousedown_all(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseDown = _TestMouseDown()
        mixin_1.mousedown(handler=self.on_mouse_down_1)
        mixin_1.mousedown(handler=self.on_mouse_down_2)
        mixin_1.unbind_mousedown_all()
        assert mixin_1._mouse_down_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}.off(" f'"{ap.MouseEventType.MOUSEDOWN.value}");'
        )
        assert expected in expression
