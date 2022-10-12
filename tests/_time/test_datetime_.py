from random import randint

from retrying import retry

from apysc._time import datetime_
from apysc._time.datetime_ import DateTime
import apysc as ap


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__convert_to_apysc_int() -> None:
    value: ap.Int = datetime_._convert_to_apysc_int(value=None)
    assert isinstance(value, ap.Int)
    assert value == 0

    value = datetime_._convert_to_apysc_int(value=10)
    assert isinstance(value, ap.Int)
    assert value == 10

    prev_value: ap.Int = ap.Int(20)
    value = datetime_._convert_to_apysc_int(value=prev_value)
    assert isinstance(value, ap.Int)
    assert value == 20
    assert value.variable_name != prev_value.variable_name
