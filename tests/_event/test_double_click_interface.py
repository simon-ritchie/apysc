from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.double_click_interface import DoubleClickInterface
from apysc._expression import expression_data_util
from apysc._type.variable_name_interface import VariableNameInterface


class _TestDoubleClick(DoubleClickInterface, VariableNameInterface):

    def __init__(self) -> None:
        """
        Class for double click interface's testing.
        """
        self.variable_name = 'test_double_click'


class TestDoubleClickInterface:

    def on_double_click_1(
            self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler for double click event.

        Parameters
        ----------
        e : MouseEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_double_click_2(
            self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler for double click event.

        Parameters
        ----------
        e : MouseEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_dblclick_handlers_if_not_initialized(self) -> None:
        interface_1: DoubleClickInterface = DoubleClickInterface()
        interface_1._initialize_dblclick_handlers_if_not_initialized()
        assert interface_1._dblclick_handlers == {}

        interface_1._initialize_dblclick_handlers_if_not_initialized()

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_dblclick(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestDoubleClick = _TestDoubleClick()
        name: str = interface_1.dblclick(handler=self.on_double_click_1)
        assert interface_1._dblclick_handlers == {
            name: {
                'handler': self.on_double_click_1,
                'options': {},
            },
        }

        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{interface_1.variable_name}.dblclick({name});'
        assert expected in expression
        expression = \
            expression_data_util.get_current_event_handler_scope_expression()
        expected = f'function {name}'
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_dblclick(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestDoubleClick = _TestDoubleClick()
        interface_1.dblclick(handler=self.on_double_click_1)
        interface_1.unbind_dblclick(handler=self.on_double_click_1)
        assert interface_1._dblclick_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        assert 'off(' in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_dblclick_all(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestDoubleClick = _TestDoubleClick()
        interface_1.dblclick(handler=self.on_double_click_1)
        interface_1.unbind_dblclick_all()
        assert interface_1._dblclick_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.off('
            f'"{ap.MouseEventType.DBLCLICK.value}");'
        )
        assert expected in expression
