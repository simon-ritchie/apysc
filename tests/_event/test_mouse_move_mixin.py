from typing import Any
from typing import Dict

import apysc as ap
from apysc._event.mouse_move_mixin import MouseMoveMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestMouseMove(MouseMoveMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """Class for MouseMoveMixIn testing."""
        self.variable_name = "test_mouse_move"


class TestMouseMoveMixIn:
    def on_mouse_move_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse move handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_mouse_move_2(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse move handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @apply_test_settings()
    def test__initialize_mouse_move_handlers_if_not_initialized(self) -> None:
        mixin_1: MouseMoveMixIn = MouseMoveMixIn()
        mixin_1._initialize_mouse_move_handlers_if_not_initialized()
        assert mixin_1._mouse_move_handlers == {}

        mixin_1._initialize_mouse_move_handlers_if_not_initialized()
        assert mixin_1._mouse_move_handlers == {}

    @apply_test_settings()
    def test_mousemove(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseMove = _TestMouseMove()
        name: str = mixin_1.mousemove(
            handler=self.on_mouse_move_1, options={"msg": "Hello!"}
        )
        assert name in mixin_1._mouse_move_handlers
        assert mixin_1._mouse_move_handlers[name].options == {"msg": "Hello!"}

        expression: str = (
            expression_data_util.get_current_event_handler_scope_expression()
        )
        expected: str = f"function {name}("
        assert expected in expression

        expression = expression_data_util.get_current_expression()
        expected = f"{mixin_1.variable_name}.mousemove({name});"
        assert expected in expression

    @apply_test_settings()
    def test_unbind_mousemove(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseMove = _TestMouseMove()
        name: str = mixin_1.mousemove(handler=self.on_mouse_move_1)
        mixin_1.unbind_mousemove(handler=self.on_mouse_move_1)
        assert mixin_1._mouse_move_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}.off("
            f'"{ap.MouseEventType.MOUSEMOVE.value}", {name});'
        )
        assert expected in expression

    @apply_test_settings()
    def test_unbind_mousemove_all(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseMove = _TestMouseMove()
        mixin_1.mousemove(handler=self.on_mouse_move_1)
        mixin_1.mousemove(handler=self.on_mouse_move_2)
        mixin_1.unbind_mousemove_all()
        assert mixin_1._mouse_move_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}.off(" f'"{ap.MouseEventType.MOUSEMOVE.value}");'
        )
        assert expected in expression
