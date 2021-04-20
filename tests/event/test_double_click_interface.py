from random import randint
from typing import Any, Dict

from retrying import retry

from apysc.event.double_click_interface import DoubleClickInterface
from apysc.expression import expression_file_util
from apysc.type.variable_name_interface import VariableNameInterface
from apysc import MouseEvent


class _TestDoubleClick(DoubleClickInterface, VariableNameInterface):

    def __init__(self) -> None:
        """
        Class for double click interface's testing.
        """
        self.variable_name = 'test_double_click'


class TestDoubleClickInterface:

    def on_double_click(
            self, e: MouseEvent, kwargs: Dict[str, Any]) -> None:
        """
        Test handler for double click event.

        Parameters
        ----------
        e : MouseEvent
            Event instance.
        kwargs : dict
            Keyword arguments.
        """

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_dbclick_handlers_if_not_initialized(self) -> None:
        interface_1: DoubleClickInterface = DoubleClickInterface()
        interface_1._initialize_dbclick_handlers_if_not_initialized()
        assert interface_1._dbclick_handlers == {}

        interface_1._initialize_dbclick_handlers_if_not_initialized()

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_dbclick_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestDoubleClick = _TestDoubleClick()
        interface_1._append_dbclick_expression(name='test_double_click')
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.dbclick(test_double_click);'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_dblclick(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestDoubleClick = _TestDoubleClick()
        name: str = interface_1.dbclick(handler=self.on_double_click)
        assert interface_1._dbclick_handlers == {
            name: {
                'handler': self.on_double_click,
                'kwargs': {},
            },
        }

        expression: str = expression_file_util.get_current_expression()
        expected: str = f'{interface_1.variable_name}.dbclick'
        assert expected in expression
        expression = \
            expression_file_util.get_current_event_handler_scope_expression()
        expected = f'function {name}'
        assert expected in expression
