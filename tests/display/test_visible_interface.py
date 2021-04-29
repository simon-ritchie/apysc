from random import randint

from retrying import retry

from apysc import Boolean
from apysc.display.visible_interface import VisibleInterface
from apysc.expression import expression_file_util


class _TestVisible(VisibleInterface):

    def __init__(self) -> None:
        """
        Test class for VisibleInterface.
        """
        self.variable_name = 'test_visible'


class TestVisibleInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_visible_if_not_initialized(self) -> None:
        interface_1: VisibleInterface = VisibleInterface()
        interface_1._initialize_visible_if_not_initialized()
        assert interface_1._visible == True

        interface_1._visible.value = False
        interface_1._initialize_visible_if_not_initialized()
        assert interface_1._visible == False

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_visible(self) -> None:
        interface_1: _TestVisible = _TestVisible()
        result: Boolean = interface_1.visible
        assert result
        assert interface_1._visible.variable_name != result.variable_name

        bool_1: Boolean = Boolean(False)
        interface_1.visible = bool_1
        assert interface_1.visible == False
        assert interface_1._visible.variable_name == bool_1.variable_name

        interface_1.visible = True  # type: ignore
        assert interface_1.visible == True

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_visible_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface_1: _TestVisible = _TestVisible()
        interface_1.visible = Boolean(True)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.show();'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        interface_1.visible = Boolean(False)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{interface_1.variable_name}.hide();'
        )
        assert expected in expression
