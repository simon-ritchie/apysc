from random import randint
from typing import Any, Dict

from retrying import retry

from apysc.event.mouse_down_interface import MouseDownInterface
from apysc.expression import expression_file_util
from apysc import MouseEvent
from apysc.type.variable_name_interface import VariableNameInterface


class _TestMouseDown(MouseDownInterface, VariableNameInterface):

    def __init__(self) -> None:
        """Test class for mouse down testing.
        """
        self.variable_name = 'test_mouse_down'


class TestMouseDownInterface:

    def on_mouse_down_1(self, e: MouseEvent, kwargs: Dict[str, Any]) -> None:
        """
        Mouse down handler method for testing.

        Parameters
        ----------
        e : Event
            Created event instance.
        kwargs : dict
            Keyword arguments to pass to.
        """

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_mouse_down_handlers_if_not_initialized(
            self) -> None:
        interface_1: MouseDownInterface = MouseDownInterface()
        interface_1._initialize_mouse_down_handlers_if_not_initialized()
        assert interface_1._mouse_down_handlers == {}

        interface_1._initialize_mouse_down_handlers_if_not_initialized()
        assert interface_1._mouse_down_handlers == {}

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_mouse_down_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestMouseDown = _TestMouseDown()
        name: str = interface_1.mousedown(handler=self.on_mouse_down_1)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.mousedown({name});'
        )
        assert expected in expression
