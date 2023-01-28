from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestEnterFrameEvent:
    @apply_test_settings()
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        event: ap.EnterFrameEvent = ap.EnterFrameEvent(this=stage)
        assert event.this == stage
        assert event.variable_name.startswith(var_names.ENTER_FRAME_EVENT)
