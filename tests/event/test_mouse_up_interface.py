from apysc.event.mouse_up_interface import MouseUpInterface


class TestMouseUpInterface:

    def test__initialize_mouse_up_handlers_if_not_initialized(self) -> None:
        interface_1: MouseUpInterface = MouseUpInterface()
        interface_1._initialize_mouse_up_handlers_if_not_initialized()
        assert interface_1._mouse_up_handlers == {}

        interface_1._initialize_mouse_up_handlers_if_not_initialized()
        assert interface_1._mouse_up_handlers == {}
