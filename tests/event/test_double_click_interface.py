from random import randint

from retrying import retry

from apysc.event.double_click_interface import DoubleClickInterface
from apysc.expression import expression_file_util
from apysc.type.variable_name_interface import VariableNameInterface


class _TestDoubleClick(DoubleClickInterface, VariableNameInterface):

    def __init__(self) -> None:
        """
        Class for double click interface's testing.
        """
        self.variable_name = 'test_double_click'


class TestDoubleClickInterface:

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
            f'{interface_1.variable_name}.dblclick(test_double_click);'
        )
        assert expected in expression
