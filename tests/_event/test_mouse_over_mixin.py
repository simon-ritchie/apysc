from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.mouse_over_mixin import MouseOverMixIn
from apysc._expression import expression_data_util
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestMouseOver(MouseOverMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """Test class for MouseOverMixIn."""
        self.variable_name = "test_mouse_over"


class TestMouseOverMixIn:
    def on_mouse_over_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse over handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_mouse_over_2(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse over handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_mouse_over_handlers_if_not_initialized(self) -> None:
        mixin_1: MouseOverMixIn = MouseOverMixIn()
        mixin_1._initialize_mouse_over_handlers_if_not_initialized()
        assert mixin_1._mouse_over_handlers == {}

        mixin_1._initialize_mouse_over_handlers_if_not_initialized()
        assert mixin_1._mouse_over_handlers == {}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_mouseover(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestMouseOver = _TestMouseOver()
        name: str = mixin_1.mouseover(handler=self.on_mouse_over_1)
        assert name in mixin_1._mouse_over_handlers
        expression: str = (
            expression_data_util.get_current_event_handler_scope_expression()
        )
        expected: str = f"function {name}("
        assert expected in expression

        expression = expression_data_util.get_current_expression()
        expected = f"{mixin_1.variable_name}.mouseover({name});"
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mouseover(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestMouseOver = _TestMouseOver()
        name: str = mixin_1.mouseover(handler=self.on_mouse_over_1)
        mixin_1.unbind_mouseover(handler=self.on_mouse_over_1)
        assert mixin_1._mouse_over_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}.off("
            f'"{ap.MouseEventType.MOUSEOVER.value}", {name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mouseover_all(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestMouseOver = _TestMouseOver()
        mixin_1.mouseover(handler=self.on_mouse_over_1)
        mixin_1.mouseover(handler=self.on_mouse_over_2)
        mixin_1.unbind_mouseover_all()
        assert mixin_1._mouse_over_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}.off("
            f'"{ap.MouseEventType.MOUSEOVER.value}");'
        )
        assert expected in expression
