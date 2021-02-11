from apyscript.display.height_interface import HeightInterface


class TestHeightInterface:

    def test_height(self) -> None:
        height_interface: HeightInterface = HeightInterface()
        height_interface.height = 200
        assert height_interface.height == 200
