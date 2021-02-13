from apyscript.display.fill_color_interface import FillColorInterface


class TestFillColorInterface:

    def test_begin_fill(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.begin_fill(color='#333')
        assert fill_color_interface.fill_color == '#333333'
        assert fill_color_interface.fill_alpha == 1.0

        fill_color_interface.begin_fill(color='#333', alpha=0.5)
        assert fill_color_interface.fill_alpha == 0.5

    def test_fill_color(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.begin_fill(color='#333')
        assert fill_color_interface.fill_color == '#333333'

    def test_fill_alpha(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.begin_fill(color='#333', alpha=0.2)
        assert fill_color_interface.fill_alpha == 0.2
