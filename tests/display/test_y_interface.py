from apyscript.display.y_interface import YInterface


class TestYInterface:

    def test_y(self) -> None:
        y_interface: YInterface = YInterface()
        y_interface.y = 200
        assert y_interface.y == 200
