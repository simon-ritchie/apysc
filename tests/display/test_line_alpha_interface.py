from random import randint

from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.display.line_alpha_interface import LineAlphaInterface


class TestLineAlphaInterface:

    def test_line_alpha(self) -> None:
        line_alpha_interface: LineAlphaInterface = LineAlphaInterface()
        line_alpha_interface.variable_name = 'test_line_alpha_interface'
        line_alpha_interface.line_alpha = 0.3
        assert line_alpha_interface.line_alpha == 0.3
