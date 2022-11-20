from random import randint

from retrying import retry

import apysc as ap
from apysc._time.hour_mixin import HourMixIn


class TestHourMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_hour_value(self) -> None:
        mixin: HourMixIn = HourMixIn()
        mixin._set_init_hour_value(hour=10)
        assert mixin._initial_hour == 10
        assert isinstance(mixin._initial_hour, int)
        assert mixin._hour == 10
        assert isinstance(mixin._hour, ap.Int)
