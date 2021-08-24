from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.mouse_up_interface import MouseUpInterface
from apysc._expression import expression_data_util
from apysc._type.variable_name_interface import VariableNameInterface


class _TestMouseUp(MouseUpInterface, VariableNameInterface):

    def __init__(self) -> None:
        """Test class for mouse up interface.
        """
        self.variable_name = 'test_mouse_up'


class TestMouseUpInterface:

    def on_mouse_up_1(
            self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler for mouse up event.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_mouse_up_2(
            self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler for mouse up event.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_mouse_up_handlers_if_not_initialized(self) -> None:
        interface_1: MouseUpInterface = MouseUpInterface()
        interface_1._initialize_mouse_up_handlers_if_not_initialized()
        assert interface_1._mouse_up_handlers == {}

        interface_1._initialize_mouse_up_handlers_if_not_initialized()
        assert interface_1._mouse_up_handlers == {}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_mouseup(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestMouseUp = _TestMouseUp()
        name: str = interface_1.mouseup(
            handler=self.on_mouse_up_1, options={'msg': 'Hello!'})
        assert name in interface_1._mouse_up_handlers
        expression: str = \
            expression_data_util.get_current_event_handler_scope_expression()
        expected: str = f'function {name}('
        assert expected in expression

        expression = expression_data_util.get_current_expression()
        expected = (
            f'{interface_1.variable_name}.mouseup({name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mouseup(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestMouseUp = _TestMouseUp()
        name: str = interface_1.mouseup(handler=self.on_mouse_up_1)
        interface_1.unbind_mouseup(handler=self.on_mouse_up_1)
        assert interface_1._mouse_up_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.off('
            f'"{ap.MouseEventType.MOUSEUP.value}", {name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mouseup_all(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestMouseUp = _TestMouseUp()
        interface_1.mouseup(handler=self.on_mouse_up_1)
        interface_1.mouseup(handler=self.on_mouse_up_2)
        interface_1.unbind_mouseup_all()
        interface_1._mouse_up_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.off('
            f'"{ap.MouseEventType.MOUSEUP.value}");'
        )
        assert expected in expression
