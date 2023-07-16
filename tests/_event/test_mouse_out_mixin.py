from typing import Any
from typing import Dict

import apysc as ap
from apysc._event.mouse_out_mixin import MouseOutMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestMouseOut(MouseOutMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """Test class for MouseOutMixIn."""
        self.variable_name = "test_mouse_out"


class TestMouseOutMixIn:
    def on_mouse_out_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse out handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_mouse_out_2(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse out handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @apply_test_settings()
    def test__initialize_mouse_out_handlers_if_not_initialized(self) -> None:
        mixin_1: MouseOutMixIn = MouseOutMixIn()
        mixin_1._initialize_mouse_out_handlers_if_not_initialized()
        assert mixin_1._mouse_out_handlers == {}

        mixin_1._initialize_mouse_out_handlers_if_not_initialized()
        assert mixin_1._mouse_out_handlers == {}

    @apply_test_settings()
    def test_mouseout(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseOut = _TestMouseOut()
        name: str = mixin_1.mouseout(
            handler=self.on_mouse_out_1, options={"msg": "Hello!"}
        )
        assert name in mixin_1._mouse_out_handlers
        assert mixin_1._mouse_out_handlers[name].options == {"msg": "Hello!"}
        expression: str = (
            expression_data_util.get_current_event_handler_scope_expression()
        )
        expected: str = f"function {name}("
        assert expected in expression

        expression = expression_data_util.get_current_expression()
        expected = f"{mixin_1.variable_name}.mouseout({name});"
        assert expected in expression

    @apply_test_settings()
    def test_unbind_mouseout(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseOut = _TestMouseOut()
        name: str = mixin_1.mouseout(handler=self.on_mouse_out_1)
        mixin_1.unbind_mouseout(handler=self.on_mouse_out_1)
        assert mixin_1._mouse_out_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}.off"
            f'("{ap.MouseEventType.MOUSEOUT.value}", {name});'
        )
        assert expected in expression

    @apply_test_settings()
    def test_unbind_mouseout_all(self) -> None:
        ap.Stage()
        mixin_1: _TestMouseOut = _TestMouseOut()
        mixin_1.mouseout(handler=self.on_mouse_out_1)
        mixin_1.mouseout(handler=self.on_mouse_out_2)
        mixin_1.unbind_mouseout_all()
        assert mixin_1._mouse_out_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}.off(" f'"{ap.MouseEventType.MOUSEOUT.value}");'
        )
        assert expected in expression
