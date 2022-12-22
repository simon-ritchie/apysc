from random import randint
from datetime import datetime

from retrying import retry

import apysc as ap
from apysc._time.left_and_right_datetimes_mixin import LeftAndRightDatetimesMixIn


class TestLeftAndRightDatetimesMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_left_and_right_py_datetimes_from_apysc_datetime(self) -> None:
        left_apysc_datetime: ap.DateTime = ap.DateTime(
            year=2022,
            month=7,
            day=5,
            hour=10,
            minute=30,
            second=50,
            millisecond=500,
        )
        right_apysc_datetime: ap.DateTime = ap.DateTime(
            year=2023,
            month=8,
            day=6,
            hour=11,
            minute=31,
            second=51,
            millisecond=501,
        )
        left_py_datetime: datetime
        right_py_datetime: datetime
        mixin: LeftAndRightDatetimesMixIn = LeftAndRightDatetimesMixIn()
        (
            left_py_datetime,
            right_py_datetime,
        ) = mixin._get_left_and_right_py_datetimes_from_apysc_datetime(
            left_apysc_datetime=left_apysc_datetime,
            right_apysc_datetime=right_apysc_datetime,
        )
        assert left_py_datetime.year == 2022
        assert left_py_datetime.month == 7
        assert left_py_datetime.day == 5
        assert left_py_datetime.hour == 10
        assert left_py_datetime.minute == 30
        assert left_py_datetime.second == 50
        assert left_py_datetime.microsecond == 500 * 1000
        assert right_py_datetime.year == 2023
        assert right_py_datetime.month == 8
        assert right_py_datetime.day == 6
        assert right_py_datetime.hour == 11
        assert right_py_datetime.minute == 31
        assert right_py_datetime.second == 51
        assert right_py_datetime.microsecond == 501 * 1000
