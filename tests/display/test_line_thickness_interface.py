from apyscript.display.line_thickness_interface import LineThicknessInterface
from apyscript.expression import expression_file_util
from apyscript.html import html_util


class TestLineThicknessInterface:

    def test_line_thickness(self) -> None:
        line_thickness_interface: LineThicknessInterface = \
            LineThicknessInterface()
        line_thickness_interface.variable_name = \
            'test_line_thickness_interface'
        line_thickness_interface.line_thickness = 3
        assert line_thickness_interface.line_thickness == 3

    def test__append_line_thickness_update_expression(self) -> None:
        line_thickness_interface: LineThicknessInterface = \
            LineThicknessInterface()
        line_thickness_interface.variable_name = \
            'test_line_thickness_interface'
        expression_file_util.remove_expression_file()
        line_thickness_interface.line_thickness = 2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            'test_line_thickness_interface.attr({"stroke-width": 2});')
        expected = html_util.wrap_expression_by_script_tag(
            expression=expected)
        assert expected in expression

    def test_update_line_thickness_and_skip_appending_exp(self) -> None:
        line_thickness_interface: LineThicknessInterface = \
            LineThicknessInterface()
        line_thickness_interface.variable_name = \
            'test_line_thickness_interface'
        expression_file_util.remove_expression_file()
        line_thickness_interface.update_line_thickness_and_skip_appending_exp(
            value=5)
        assert line_thickness_interface.line_thickness == 5
        expression: str = expression_file_util.get_current_expression()
        assert expression == ''
