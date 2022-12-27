from random import randint

from retrying import retry

from apysc._event.enter_frame_mixin import EnterFrameMixIn
import apysc as ap


class TestEnterFrameMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_enter_frame_handlers_if_not_initialized(self) -> None:
        mixin: EnterFrameMixIn = EnterFrameMixIn()
        mixin._initialize_enter_frame_handlers_if_not_initialized()
        assert mixin._enter_frame_handlers == {}

        prev_id: int = id(mixin._enter_frame_handlers)
        mixin._initialize_enter_frame_handlers_if_not_initialized()
        assert prev_id == id(mixin._enter_frame_handlers)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_is_stopped_settings_if_not_initialized(self) -> None:
        mixin: EnterFrameMixIn = EnterFrameMixIn()
        mixin._initialize_is_stopped_settings_if_not_initialized()
        assert mixin._is_stopped_settings == {}

        mixin._is_stopped_settings["test"] = ap.Boolean(True)
        mixin._initialize_is_stopped_settings_if_not_initialized()
        assert mixin._is_stopped_settings == {"test": True}
