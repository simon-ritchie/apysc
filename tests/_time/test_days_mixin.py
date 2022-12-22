from random import randint

from retrying import retry

import apysc as ap
from apysc._time.days_mixin import DaysMixIn


class TestDaysMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_days_value_for_python(self) -> None:
        left_datetime: ap.DateTime = ap.DateTime(
            year=2022,
            month=12,
            day=5,
        )
        right_datetime: ap.DateTime = ap.DateTime(
            year=2022,
            month=12,
            day=2,
            hour=10,
        )
        mixin: DaysMixIn = DaysMixIn()
        mixin._set_init_days_value_for_python(
            left_datetime=left_datetime,
            right_datetime=right_datetime,
        )
        assert mixin._days_value == 2
