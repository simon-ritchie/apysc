from random import randint

from retrying import retry

from apysc._event.enter_frame_mixin import EnterFrameMixIn


class TestEnterFrameMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_enter_frame_handlers_if_not_initialized(self) -> None:
        interface: EnterFrameMixIn = EnterFrameMixIn()
        interface._initialize_enter_frame_handlers_if_not_initialized()
        assert interface._enter_frame_handlers == {}

        prev_id: int = id(interface._enter_frame_handlers)
        interface._initialize_enter_frame_handlers_if_not_initialized()
        assert prev_id == id(interface._enter_frame_handlers)
