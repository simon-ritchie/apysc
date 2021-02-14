from random import randint

from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.display.line_thickness_interface import LineThicknessInterface


class TestLineThicknessInterface:

    def test_line_thickness(self) -> None:
        line_thickness_interface: LineThicknessInterface = \
            LineThicknessInterface()
        line_thickness_interface.variable_name = \
            'test_line_thickness_interface'
        line_thickness_interface.line_thickness = 3
        assert line_thickness_interface.line_thickness == 3
