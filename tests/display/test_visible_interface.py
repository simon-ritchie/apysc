from apysc.display.visible_interface import VisibleInterface


class TestVisibleInterface:

    def test__initialize_visible_if_not_initialized(self) -> None:
        interface_1: VisibleInterface = VisibleInterface()
        interface_1._initialize_visible_if_not_initialized()
        assert interface_1._visible == True

        interface_1._visible.value = False
        interface_1._initialize_visible_if_not_initialized()
        assert interface_1._visible == False
