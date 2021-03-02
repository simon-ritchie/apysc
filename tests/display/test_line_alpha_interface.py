from random import randint

from retrying import retry

from apyscript.display.line_alpha_interface import LineAlphaInterface
from apyscript.expression import expression_file_util
from apyscript.type import Number


class TestLineAlphaInterface:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_line_alpha(self) -> None:
        line_alpha_interface: LineAlphaInterface = LineAlphaInterface()
        line_alpha_interface.variable_name = 'test_line_alpha_interface'
        line_alpha_interface.line_alpha = Number(0.3)
        assert line_alpha_interface.line_alpha == 0.3

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_line_alpha_update_expression(self) -> None:
        line_alpha_interface: LineAlphaInterface = LineAlphaInterface()
        line_alpha_interface.variable_name = 'test_line_alpha_interface'
        expression_file_util.remove_expression_file()
        line_alpha_interface.line_alpha = Number(0.5)
        expression: str = expression_file_util.get_current_expression()
        expected: str = 'test_line_alpha_interface.stroke({opacity: 0.5});'
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_update_line_alpha_and_skip_appending_exp(self) -> None:
        line_alpha_interface: LineAlphaInterface = LineAlphaInterface()
        line_alpha_interface.variable_name = 'test_line_alpha_interface'
        expression_file_util.remove_expression_file()
        line_alpha_interface.update_line_alpha_and_skip_appending_exp(
            value=Number(0.25))
        assert line_alpha_interface.line_alpha == 0.25
        expression: str = expression_file_util.get_current_expression()
        assert 'stroke-opacity' not in expression
