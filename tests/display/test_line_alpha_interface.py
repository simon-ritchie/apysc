from random import randint

from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.display.line_alpha_interface import LineAlphaInterface


class TestLineAlphaInterface:

    def test_line_alpha(self) -> None:
        line_alpha_interface: LineAlphaInterface = LineAlphaInterface()
        line_alpha_interface.variable_name = 'test_line_alpha_interface'
        line_alpha_interface.line_alpha = 0.3
        assert line_alpha_interface.line_alpha == 0.3

    def test__append_line_alpha_update_expression(self) -> None:
        line_alpha_interface: LineAlphaInterface = LineAlphaInterface()
        line_alpha_interface.variable_name = 'test_line_alpha_interface'
        expression_file_util.remove_current_scope_expression_file()
        line_alpha_interface.line_alpha = 0.5
        expression: str = expression_file_util.get_current_scope_expression()
        expected: str = 'test_line_alpha_interface.stroke({opacity: 0.5});'
        expected = html_util.wrap_expression_by_script_tag(
            expression=expected)
        assert expected in expression

    def test_update_line_alpha_and_skip_appending_exp(self) -> None:
        line_alpha_interface: LineAlphaInterface = LineAlphaInterface()
        line_alpha_interface.variable_name = 'test_line_alpha_interface'
        expression_file_util.remove_current_scope_expression_file()
        line_alpha_interface.update_line_alpha_and_skip_appending_exp(
            value=0.25)
        assert line_alpha_interface.line_alpha == 0.25
        expression: str = expression_file_util.get_current_scope_expression()
        assert expression == ''
