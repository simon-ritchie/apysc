from random import randint
from typing import Any, Dict

from retrying import retry

from apysc.event.mouse_over_interface import MouseOverInterface
from apysc.type.variable_name_interface import VariableNameInterface
from apysc.expression import expression_file_util
from apysc import MouseEvent


class _TestMouseOver(MouseOverInterface, VariableNameInterface):

    def __init__(self) -> None:
        """Test class for MouseOverInterface.
        """
        self.variable_name = 'test_mouse_over'


class TestMouseOverInterface:

    def on_mouse_over_1(self, e: MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse over handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_mouse_over_handlers_if_not_initialized(self) -> None:
        interface_1: MouseOverInterface = MouseOverInterface()
        interface_1._initialize_mouse_over_handlers_if_not_initialized()
        assert interface_1._mouse_over_handlers == {}

        interface_1._initialize_mouse_over_handlers_if_not_initialized()
        assert interface_1._mouse_over_handlers == {}

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_mouse_over_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseOver = _TestMouseOver()
        name: str = interface_1.mouseover(handler=self.on_mouse_over_1)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.mouseover({name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_mouseover(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseOver = _TestMouseOver()
        name: str = interface_1.mouseover(handler=self.on_mouse_over_1)
        assert name in interface_1._mouse_over_handlers
        expression: str = \
            expression_file_util.get_current_event_handler_scope_expression()
        expected: str = f'function {name}('
        assert expected in expression
