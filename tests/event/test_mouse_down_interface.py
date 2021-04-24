from apysc.event.mouse_down_interface import MouseDownInterface


class TestMouseDownInterface:

    def test__initialize_mouse_down_handlers_if_not_initialized(
            self) -> None:
        interface_1: MouseDownInterface = MouseDownInterface()
        interface_1._initialize_mouse_down_handlers_if_not_initialized()
        assert interface_1._mouse_down_handlers == {}

        interface_1._initialize_mouse_down_handlers_if_not_initialized()
        assert interface_1._mouse_down_handlers == {}
