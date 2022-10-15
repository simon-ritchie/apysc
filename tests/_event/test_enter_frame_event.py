from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names


class TestEnterFrameEvent:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        event: ap.EnterFrameEvent = ap.EnterFrameEvent(this=stage)
        assert event.this == stage
        assert event.variable_name.startswith(var_names.ENTER_FRAME_EVENT)
