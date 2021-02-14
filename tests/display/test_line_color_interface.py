from random import randint

from retrying import retry

from apyscript.display.line_color_interface import LineColorInterface


class TestLineColorInterface:

    def test_line_color(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        line_color_interface.line_color = '#555'
        assert line_color_interface.line_color == '#555555'
