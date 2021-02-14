from random import randint

from retrying import retry

from apyscript.display.line_color_interface import LineColorInterface
from apyscript.expression import expression_file_util


class TestLineColorInterface:

    def test_line_color(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        line_color_interface.line_color = '#555'
        assert line_color_interface.line_color == '#555555'

    def test__append_line_color_update_expression(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        expression_file_util.remove_current_scope_expression_file()
        line_color_interface.line_color = '#333'
        expression: str = expression_file_util.get_current_scope_expression()
        expected: str = 'test_line_color_interface.stroke("#333333");'
        assert expected in expression

    def test_update_line_color_and_skip_appending_exp(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        expression_file_util.remove_current_scope_expression_file()
        line_color_interface.update_line_color_and_skip_appending_exp(
            value='#777')
        assert line_color_interface.line_color == '#777777'
        expression: str = expression_file_util.get_current_scope_expression()
        assert expression == ''
