from random import randint

from retrying import retry

import apysc as ap
from apysc._time.month_mixin import MonthMixIn


class TestMonthMixIn:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_month_value(self) -> None:
        mixin: MonthMixIn = MonthMixIn()
        mixin._set_init_month_value(month=5)
        assert mixin._initial_month == 5
        assert isinstance(mixin._initial_month, int)
        assert mixin._month == 5
        assert isinstance(mixin._month, ap.Int)
