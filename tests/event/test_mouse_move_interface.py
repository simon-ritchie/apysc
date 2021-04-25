from random import randint

from retrying import retry

from apysc.event.mouse_move_interface import MouseMoveInterface


class TestMouseMoveInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_mouse_move_handlers_if_not_initialized(self) -> None:
        interface_1: MouseMoveInterface = MouseMoveInterface()
        interface_1._initialize_mouse_move_handlers_if_not_initialized()
        assert interface_1._mouse_move_handlers == {}

        interface_1._initialize_mouse_move_handlers_if_not_initialized()
        assert interface_1._mouse_move_handlers == {}
