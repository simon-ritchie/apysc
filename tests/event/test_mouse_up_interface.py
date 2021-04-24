from random import randint
from typing import Any, Dict

from retrying import retry

from apysc.event.mouse_up_interface import MouseUpInterface
from apysc.expression import expression_file_util
from apysc import MouseEvent, EventType
from apysc.type.variable_name_interface import VariableNameInterface


class _TestMouseUp(MouseUpInterface, VariableNameInterface):

    def __init__(self) -> None:
        """Test class for mouse up interface.
        """
        self.variable_name = 'test_mouse_up'


class TestMouseUpInterface:

    def on_mouse_up_1(self, e: MouseEvent, kwargs: Dict[str, Any]) -> None:
        """
        Test handler for mouse up event.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        kwargs : dict
            Keyword arguments to pass to.
        """

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_mouse_up_handlers_if_not_initialized(self) -> None:
        interface_1: MouseUpInterface = MouseUpInterface()
        interface_1._initialize_mouse_up_handlers_if_not_initialized()
        assert interface_1._mouse_up_handlers == {}

        interface_1._initialize_mouse_up_handlers_if_not_initialized()
        assert interface_1._mouse_up_handlers == {}

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_mouse_up_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseUp = _TestMouseUp()
        name: str = interface_1.mouseup(handler=self.on_mouse_up_1)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.mouseup({name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_mouseup(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseUp = _TestMouseUp()
        name: str = interface_1.mouseup(
            handler=self.on_mouse_up_1, kwargs={'msg': 'Hello!'})
        assert name in interface_1._mouse_up_handlers
        expression: str = \
            expression_file_util.get_current_event_handler_scope_expression()
        expected: str = f'function {name}('
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_unbind_mouseup(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseUp = _TestMouseUp()
        name: str = interface_1.mouseup(handler=self.on_mouse_up_1)
        interface_1.unbind_mouseup(handler=self.on_mouse_up_1)
        assert interface_1._mouse_up_handlers == {}
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.off("{EventType.MOUSEUP.value}", '
            f'{name});'
        )
        assert expected in expression
