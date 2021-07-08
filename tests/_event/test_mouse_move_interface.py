from random import randint
from typing import Any
from typing import Dict

from retrying import retry

from apysc import MouseEvent
from apysc import MouseEventType
from apysc._event.mouse_move_interface import MouseMoveInterface
from apysc._expression import expression_file_util
from apysc._type.variable_name_interface import VariableNameInterface


class _TestMouseMove(MouseMoveInterface, VariableNameInterface):

    def __init__(self) -> None:
        """Class for MouseMoveInterface testing.
        """
        self.variable_name = 'test_mouse_move'


class TestMouseMoveInterface:

    def on_mouse_move_1(self, e: MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse move handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_mouse_move_2(self, e: MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse move handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_mouse_move_handlers_if_not_initialized(self) -> None:
        interface_1: MouseMoveInterface = MouseMoveInterface()
        interface_1._initialize_mouse_move_handlers_if_not_initialized()
        assert interface_1._mouse_move_handlers == {}

        interface_1._initialize_mouse_move_handlers_if_not_initialized()
        assert interface_1._mouse_move_handlers == {}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_mousemove(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseMove = _TestMouseMove()
        name: str = interface_1.mousemove(
            handler=self.on_mouse_move_1, options={'msg': 'Hello!'})
        assert name in interface_1._mouse_move_handlers
        assert interface_1._mouse_move_handlers[name]['options'] == \
            {'msg': 'Hello!'}

        expression: str = \
            expression_file_util.get_current_event_handler_scope_expression()
        expected: str = f'function {name}('
        assert expected in expression

        expression = expression_file_util.get_current_expression()
        expected = (
            f'{interface_1.variable_name}.mousemove({name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mousemove(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseMove = _TestMouseMove()
        name: str = interface_1.mousemove(handler=self.on_mouse_move_1)
        interface_1.unbind_mousemove(handler=self.on_mouse_move_1)
        assert interface_1._mouse_move_handlers == {}
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.off('
            f'"{MouseEventType.MOUSEMOVE.value}", {name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mousemove_all(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseMove = _TestMouseMove()
        interface_1.mousemove(handler=self.on_mouse_move_1)
        interface_1.mousemove(handler=self.on_mouse_move_2)
        interface_1.unbind_mousemove_all()
        assert interface_1._mouse_move_handlers == {}
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.off('
            f'"{MouseEventType.MOUSEMOVE.value}");'
        )
        assert expected in expression
