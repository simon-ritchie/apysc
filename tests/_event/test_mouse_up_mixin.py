# pyright: reportUnusedExpression=false

from typing import Any
from typing import Dict

import apysc as ap
from apysc._event.mouse_up_mixin import MouseUpMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestMouseUp(MouseUpMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """Test class for mouse up mixin."""
        self.variable_name = "test_mouse_up"


class TestMouseUpMixIn:
    def on_mouse_up_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler for mouse up event.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_mouse_up_2(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler for mouse up event.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @apply_test_settings()
    def test__initialize_mouse_up_handlers_if_not_initialized(self) -> None:
        mixin_1: MouseUpMixIn = MouseUpMixIn()
        mixin_1._initialize_mouse_up_handlers_if_not_initialized()
        assert mixin_1._mouse_up_handlers == {}

        mixin_1._initialize_mouse_up_handlers_if_not_initialized()
        assert mixin_1._mouse_up_handlers == {}

    @apply_test_settings()
    def test_mouseup(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseUp = _TestMouseUp()
        name: str = mixin_1.mouseup(
            handler=self.on_mouse_up_1, options={"msg": "Hello!"}
        )
        assert name in mixin_1._mouse_up_handlers
        expression: str = (
            expression_data_util.get_current_event_handler_scope_expression()
        )
        expected: str = f"function {name}("
        assert expected in expression

        expression = expression_data_util.get_current_expression()
        expected = f"{mixin_1.variable_name}.mouseup({name});"
        assert expected in expression

    @apply_test_settings()
    def test_unbind_mouseup(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseUp = _TestMouseUp()
        name: str = mixin_1.mouseup(handler=self.on_mouse_up_1)
        mixin_1.unbind_mouseup(handler=self.on_mouse_up_1)
        assert mixin_1._mouse_up_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}.off("
            f'"{ap.MouseEventType.MOUSEUP.value}", {name});'
        )
        assert expected in expression

    @apply_test_settings()
    def test_unbind_mouseup_all(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseUp = _TestMouseUp()
        mixin_1.mouseup(handler=self.on_mouse_up_1)
        mixin_1.mouseup(handler=self.on_mouse_up_2)
        mixin_1.unbind_mouseup_all()
        mixin_1._mouse_up_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}.off(" f'"{ap.MouseEventType.MOUSEUP.value}");'
        )
        assert expected in expression
