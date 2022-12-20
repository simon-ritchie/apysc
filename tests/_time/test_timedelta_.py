from random import randint

from retrying import retry

from apysc._time.timedelta_ import TimeDelta
from apysc._time import timedelta_
import apysc as ap


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_variable_name_suffix_from_datetimes() -> None:
    left_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=5)
    right_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=3)
    variable_name_suffix: str = timedelta_._get_variable_name_suffix_from_datetimes(
        left_datetime=left_datetime,
        right_datetime=right_datetime,
    )
    assert variable_name_suffix == ""

    right_datetime._variable_name_suffix = "right_datetime"
    variable_name_suffix = timedelta_._get_variable_name_suffix_from_datetimes(
        left_datetime=left_datetime,
        right_datetime=right_datetime,
    )
    assert variable_name_suffix == "right_datetime"

    right_datetime._variable_name_suffix = ""
    left_datetime._variable_name_suffix = "left_datetime"
    variable_name_suffix = timedelta_._get_variable_name_suffix_from_datetimes(
        left_datetime=left_datetime,
        right_datetime=right_datetime,
    )
    assert variable_name_suffix == "left_datetime"

    right_datetime._variable_name_suffix = "right_datetime"
    variable_name_suffix = timedelta_._get_variable_name_suffix_from_datetimes(
        left_datetime=left_datetime,
        right_datetime=right_datetime,
    )
    assert variable_name_suffix == "left_datetime_right_datetime"
