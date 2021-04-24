from random import randint

from retrying import retry

from apysc.event.mouse_over_interface import MouseOverInterface


class TestMouseOverInterface:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_mouse_over_handlers_if_not_initialized(self) -> None:
        interface_1: MouseOverInterface = MouseOverInterface()
        interface_1._initialize_mouse_over_handlers_if_not_initialized()
        assert interface_1._mouse_over_handlers == {}

        interface_1._initialize_mouse_over_handlers_if_not_initialized()
        assert interface_1._mouse_over_handlers == {}
