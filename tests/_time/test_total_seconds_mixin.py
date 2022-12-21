from random import randint

from retrying import retry

from apysc._time.total_seconds_mixin import TotalSecondsMixIn
import apysc as ap


class TestTotalSecondsMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_total_seconds_value_for_python(self) -> None:
        left_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=2)
        right_datetime: ap.DateTime = ap.DateTime(
            year=2022,
            month=12,
            day=1,
            millisecond=500,
        )
        mixin: TotalSecondsMixIn = TotalSecondsMixIn()
        mixin._set_init_total_seconds_value_for_python(
            left_datetime=left_datetime,
            right_datetime=right_datetime,
        )
        assert mixin._total_seconds_value == 86399.5
