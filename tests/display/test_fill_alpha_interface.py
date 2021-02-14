from random import randint

from retrying import retry

from apyscript.display.fill_alpha_interface import FillAlphaInterface


class TestFillAlphaInterface:

    def test_fill_alpha(self) -> None:
        fill_alpha_interface: FillAlphaInterface = FillAlphaInterface()
        fill_alpha_interface.variable_name = 'test_fill_alpha_interface'
        fill_alpha_interface.fill_alpha = 0.5
        assert fill_alpha_interface.fill_alpha == 0.5
