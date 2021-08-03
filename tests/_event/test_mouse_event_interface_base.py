from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.click_interface import ClickInterface
from apysc._event.handler import HandlerData
from apysc._event.handler import get_handler_name
from apysc._event.mouse_event_interface_base import MouseEventInterfaceBase
from apysc._expression import expression_file_util
from apysc._type.variable_name_interface import VariableNameInterface
from tests import testing_helper


class _TestClickInterface(ClickInterface, VariableNameInterface):

    def __init__(self) -> None:
        """Interface for testing.
        """
        self.variable_name = 'test_click_interface'


class TestMouseEventInterfaceBase:

    def on_click_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler method.

        Parameters
        ----------
        e : MouseEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_click_2(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler method.

        Parameters
        ----------
        e : MouseEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_mouse_event_handler_data(self) -> None:
        handlers_dict: Dict[str, HandlerData] = {}
        interface_1: _TestClickInterface = _TestClickInterface()
        interface_1._set_mouse_event_handler_data(
            handler=self.on_click_1,
            handlers_dict=handlers_dict,
            options=None)
        name: str = get_handler_name(
            handler=self.on_click_1, instance=interface_1)
        assert handlers_dict == {
            name: {
                'handler': self.on_click_1,
                'options': {},
            }
        }

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__unbind_mouse_event(self) -> None:
        expression_file_util.empty_expression_dir()
        interface_1: _TestClickInterface = _TestClickInterface()
        interface_1.click(handler=self.on_click_1)
        interface_1._unbind_mouse_event(
            handler=self.on_click_1,
            mouse_event_type=ap.MouseEventType.CLICK,
            handlers_dict=interface_1._click_handlers)
        assert interface_1._click_handlers == {}
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}'
            f'.off("{ap.MouseEventType.CLICK.value}",')
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__unbind_all_mouse_events(self) -> None:
        expression_file_util.empty_expression_dir()
        interface_1: _TestClickInterface = _TestClickInterface()
        interface_1.click(handler=self.on_click_1)
        interface_1.click(handler=self.on_click_2)
        interface_1._unbind_all_mouse_events(
            mouse_event_type=ap.MouseEventType.CLICK,
            handlers_dict=interface_1._click_handlers)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}'
            f'.off("{ap.MouseEventType.CLICK.value}");'
        )
        assert expected in expression
        assert interface_1._click_handlers == {}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_mouse_event_binding_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        interface_1: _TestClickInterface = _TestClickInterface()
        name: str = interface_1.click(handler=self.on_click_1)
        interface_1._append_mouse_event_binding_expression(
            name=name, mouse_event_type=ap.MouseEventType.CLICK)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.'
            f'{ap.MouseEventType.CLICK.value}({name});'
        )
        assert expected in expression
