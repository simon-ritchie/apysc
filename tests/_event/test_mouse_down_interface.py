from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.mouse_down_interface import MouseDownInterface
from apysc._expression import expression_data_util
from apysc._type.variable_name_interface import VariableNameInterface


class _TestMouseDown(MouseDownInterface, VariableNameInterface):

    def __init__(self) -> None:
        """Test class for mouse down testing.
        """
        self.variable_name = 'test_mouse_down'


class TestMouseDownInterface:

    def on_mouse_down_1(
            self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse down handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_mouse_down_2(
            self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse down handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_mouse_down_handlers_if_not_initialized(
            self) -> None:
        interface_1: MouseDownInterface = MouseDownInterface()
        interface_1._initialize_mouse_down_handlers_if_not_initialized()
        assert interface_1._mouse_down_handlers == {}

        interface_1._initialize_mouse_down_handlers_if_not_initialized()
        assert interface_1._mouse_down_handlers == {}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_mousedown(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestMouseDown = _TestMouseDown()
        name: str = interface_1.mousedown(
            handler=self.on_mouse_down_1,
            options={'msg': 'Hello!'})
        assert name in interface_1._mouse_down_handlers
        expression: str = \
            expression_data_util.get_current_event_handler_scope_expression()
        expected: str = f'function {name}('
        assert expected in expression

        expression = expression_data_util.get_current_expression()
        expected = (
            f'{interface_1.variable_name}.mousedown({name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mousedown(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestMouseDown = _TestMouseDown()
        name = interface_1.mousedown(handler=self.on_mouse_down_1)
        interface_1.unbind_mousedown(handler=self.on_mouse_down_1)
        assert interface_1._mouse_down_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.off('
            f'"{ap.MouseEventType.MOUSEDOWN.value}", {name});')
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mousedown_all(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestMouseDown = _TestMouseDown()
        interface_1.mousedown(handler=self.on_mouse_down_1)
        interface_1.mousedown(handler=self.on_mouse_down_2)
        interface_1.unbind_mousedown_all()
        assert interface_1._mouse_down_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.off('
            f'"{ap.MouseEventType.MOUSEDOWN.value}");'
        )
        assert expected in expression
