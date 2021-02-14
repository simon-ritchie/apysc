from apyscript.display.begin_fill_interface import BiginFillInterface


class TestBiginFillInterface:

    def test_begin_fill(self) -> None:
        begin_fill_interface: BiginFillInterface = BiginFillInterface()
        begin_fill_interface.begin_fill(color='#333')
        assert begin_fill_interface.fill_color == '#333333'
        assert begin_fill_interface.fill_alpha == 1.0

        begin_fill_interface.begin_fill(color='#333', alpha=0.5)
        assert begin_fill_interface.fill_alpha == 0.5

    def test_fill_color(self) -> None:
        begin_fill_interface: BiginFillInterface = BiginFillInterface()
        begin_fill_interface.begin_fill(color='#333')
        assert begin_fill_interface.fill_color == '#333333'

    def test_fill_alpha(self) -> None:
        begin_fill_interface: BiginFillInterface = BiginFillInterface()
        begin_fill_interface.begin_fill(color='#333', alpha=0.2)
        assert begin_fill_interface.fill_alpha == 0.2
