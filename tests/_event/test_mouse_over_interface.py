from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.mouse_over_interface import MouseOverInterface
from apysc._expression import expression_file_util
from apysc._type.variable_name_interface import VariableNameInterface


class _TestMouseOver(MouseOverInterface, VariableNameInterface):

    def __init__(self) -> None:
        """Test class for MouseOverInterface.
        """
        self.variable_name = 'test_mouse_over'


class TestMouseOverInterface:

    def on_mouse_over_1(
            self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse over handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_mouse_over_2(
            self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
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
        interface_1: MouseOverInterface = MouseOverInterface()
        interface_1._initialize_mouse_over_handlers_if_not_initialized()
        assert interface_1._mouse_over_handlers == {}

        interface_1._initialize_mouse_over_handlers_if_not_initialized()
        assert interface_1._mouse_over_handlers == {}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_mouseover(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseOver = _TestMouseOver()
        name: str = interface_1.mouseover(handler=self.on_mouse_over_1)
        assert name in interface_1._mouse_over_handlers
        expression: str = \
            expression_file_util.get_current_event_handler_scope_expression()
        expected: str = f'function {name}('
        assert expected in expression

        expression = expression_file_util.get_current_expression()
        expected = (
            f'{interface_1.variable_name}.mouseover({name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mouseover(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseOver = _TestMouseOver()
        name: str = interface_1.mouseover(handler=self.on_mouse_over_1)
        interface_1.unbind_mouseover(handler=self.on_mouse_over_1)
        assert interface_1._mouse_over_handlers == {}
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.off('
            f'"{ap.MouseEventType.MOUSEOVER.value}", {name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mouseover_all(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseOver = _TestMouseOver()
        interface_1.mouseover(handler=self.on_mouse_over_1)
        interface_1.mouseover(handler=self.on_mouse_over_2)
        interface_1.unbind_mouseover_all()
        assert interface_1._mouse_over_handlers == {}
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.off('
            f'"{ap.MouseEventType.MOUSEOVER.value}");'
        )
        assert expected in expression
