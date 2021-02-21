from random import randint

from retrying import retry

from apyscript.display.x_interface import XInterface
from apyscript.expression import expression_file_util
from apyscript.html import html_util


class TestXInterface:

    def test_x(self) -> None:
        x_interface = XInterface()
        x_interface.variable_name = 'test_x_interface'
        x_interface.x = 100
        assert x_interface.x == 100

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_x_update_expression(self) -> None:
        x_interface = XInterface()
        x_interface.variable_name = 'test_x_interface'
        expression_file_util.remove_expression_file()
        x_interface.x = 200
        expression: str = expression_file_util.get_current_expression()
        expected: str = 'test_x_interface.x(200);'
        expected = html_util.wrap_expression_by_script_tag(
            expression=expected)
        assert expected in expression
