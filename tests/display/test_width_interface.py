from apyscript.display.width_interface import WidthInterface


class TestWidthInterface:

    def test_width(self) -> None:
        width_interface: WidthInterface = WidthInterface()
        width_interface.width = 100
        assert width_interface.width == 100
