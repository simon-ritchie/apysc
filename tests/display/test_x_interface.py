from apyscript.display.x_interface import XInterface


class TestXInterface:

    def test_x(self) -> None:
        x_interface = XInterface()
        x_interface.x = 100
        assert x_interface.x == 100
