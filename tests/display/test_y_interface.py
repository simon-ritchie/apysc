from random import randint

from retrying import retry

from apyscript.display.y_interface import YInterface
from apyscript.expression import expression_file_util
from apyscript.html import html_util


class TestYInterface:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_y(self) -> None:
        y_interface: YInterface = YInterface()
        y_interface.variable_name = 'test_y_interface'
        y_interface.y = 200
        assert y_interface.y == 200

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_y_update_expression(self) -> None:
        y_interface: YInterface = YInterface()
        expression_file_util.remove_expression_file()
        y_interface.variable_name = 'test_y_interface'
        y_interface.y = 300
        expression: str = expression_file_util.get_current_expression()
        expected: str = 'test_y_interface.y(300);'
        assert expected in expression
