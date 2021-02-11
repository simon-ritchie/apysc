from apyscript.display.fill_color_interface import FillColorInterface


class TestFillColorInterface:

    def test_begin_fill(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.begin_fill(color='#333')
        assert fill_color_interface._fill_color == '#333333'
