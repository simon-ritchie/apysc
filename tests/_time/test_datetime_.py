from random import randint

from retrying import retry

from apysc._time import datetime_
import apysc as ap
from apysc._testing.testing_helper import assert_attrs


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


class TestDateTime:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        datetime: ap.DateTime = ap.DateTime(year=2022, month=3, day=5)
        assert_attrs(
            expected_attrs={
                "_year": ap.Int(2022),
                "_month": ap.Int(3),
                "_day": ap.Int(5),
                "_hour": ap.Int(0),
                "_minute": ap.Int(0),
                "_second": ap.Int(0),
                "_millisecond": ap.Int(0),
            },
            any_obj=datetime,
        )

        datetime: ap.DateTime = ap.DateTime(
            year=2022,
            month=3,
            day=5,
            hour=10,
            minute=30,
            second=50,
            millisecond=500,
        )
        assert_attrs(
            expected_attrs={
                "_year": ap.Int(2022),
                "_month": ap.Int(3),
                "_day": ap.Int(5),
                "_hour": ap.Int(10),
                "_minute": ap.Int(30),
                "_second": ap.Int(50),
                "_millisecond": ap.Int(500),
            },
            any_obj=datetime,
        )
