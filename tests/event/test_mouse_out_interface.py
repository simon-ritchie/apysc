from apysc.event.mouse_out_interface import MouseOutInterface


class TestMouseOutInterface:

    def test__initialize_mouse_out_handlers_if_not_initialized(self) -> None:
        interface_1: MouseOutInterface = MouseOutInterface()
        interface_1._initialize_mouse_out_handlers_if_not_initialized()
        assert interface_1._mouse_out_handlers == {}

        interface_1._initialize_mouse_out_handlers_if_not_initialized()
        assert interface_1._mouse_out_handlers == {}
