from random import randint

from retrying import retry

from apyscript.display.fill_color_interface import FillColorInterface


class TestFillColorInterface:

    def test_fill_color(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        fill_color_interface.fill_color = '#333'
        assert fill_color_interface.fill_color == '#333333'
