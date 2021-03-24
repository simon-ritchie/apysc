from random import randint

from retrying import retry

from apysc.display.line_thickness_interface import LineThicknessInterface
from apysc.expression import expression_file_util
from apysc.type import Int


class TestLineThicknessInterface:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_line_thickness(self) -> None:
        line_thickness_interface: LineThicknessInterface = \
            LineThicknessInterface()
        line_thickness_interface.variable_name = \
            'test_line_thickness_interface'
        line_thickness_interface.line_thickness = Int(3)
        assert line_thickness_interface.line_thickness == 3

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_line_thickness_update_expression(self) -> None:
        line_thickness_interface: LineThicknessInterface = \
            LineThicknessInterface()
        line_thickness_interface.variable_name = \
            'test_line_thickness_interface'
        expression_file_util.remove_expression_file()
        line_thickness_interface.line_thickness = Int(2)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            'test_line_thickness_interface.attr({"stroke-width": 2});')
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_update_line_thickness_and_skip_appending_exp(self) -> None:
        line_thickness_interface: LineThicknessInterface = \
            LineThicknessInterface()
        line_thickness_interface.variable_name = \
            'test_line_thickness_interface'
        expression_file_util.remove_expression_file()
        line_thickness_interface.update_line_thickness_and_skip_appending_exp(
            value=Int(5))
        assert line_thickness_interface.line_thickness == 5
        expression: str = expression_file_util.get_current_expression()
        assert 'stroke-width' not in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_line_thickness_if_not_initialized(self) -> None:
        line_thickness_interface: LineThicknessInterface = \
            LineThicknessInterface()
        line_thickness_interface.variable_name = \
            'test_line_thickness_interface'
        line_thickness_interface.\
            _initialize_line_thickness_if_not_initialized()
        assert line_thickness_interface.line_thickness == 1

        line_thickness_interface.line_thickness = Int(2)
        line_thickness_interface.\
            _initialize_line_thickness_if_not_initialized()
        assert line_thickness_interface.line_thickness == 2
