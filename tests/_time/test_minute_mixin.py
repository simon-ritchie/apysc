from random import randint

from retrying import retry

import apysc as ap
from apysc._time.minute_mixin import MinuteMixIn


class TestMinuteMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_minute_value(self) -> None:
        mixin: MinuteMixIn = MinuteMixIn()
        mixin._set_init_minute_value(minute=30)
        assert mixin._initial_minute == 30
        assert isinstance(mixin._initial_minute, int)
        assert mixin._minute == 30
        assert isinstance(mixin._minute, ap.Int)
