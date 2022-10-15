from random import randint

from retrying import retry

from apysc._time import datetime_
import apysc as ap
from apysc._testing.testing_helper import assert_attrs
from apysc._expression import var_names


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__convert_to_apysc_int() -> None:
    value: ap.Int = datetime_._convert_to_apysc_int(
        value=None, variable_name_suffix="test"
    )
    assert isinstance(value, ap.Int)
    assert value == 0
    assert value._variable_name_suffix == "test"

    value = datetime_._convert_to_apysc_int(value=10, variable_name_suffix="")
    assert isinstance(value, ap.Int)
    assert value == 10

    prev_value: ap.Int = ap.Int(20)
    value = datetime_._convert_to_apysc_int(value=prev_value, variable_name_suffix="")
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
        assert datetime.variable_name.startswith(var_names.DATETIME)

        datetime: ap.DateTime = ap.DateTime(
            year=2022,
            month=3,
            day=5,
            hour=10,
            minute=30,
            second=50,
            millisecond=500,
            variable_name_suffix="test",
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
                "_variable_name_suffix": "test",
            },
            any_obj=datetime,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot_and__revert(self) -> None:
        datetime: ap.DateTime = ap.DateTime(
            year=2022,
            month=3,
            day=5,
            hour=10,
            minute=30,
            second=50,
            millisecond=500,
        )
        snapshot_name: str = datetime._get_next_snapshot_name()
        datetime._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        datetime._year._value = 2023
        datetime._month._value = 5
        datetime._day._value = 6
        datetime._hour._value = 11
        datetime._minute._value = 31
        datetime._second._value = 51
        datetime._millisecond._value = 501
        datetime._run_all_revert_methods(snapshot_name=snapshot_name)

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
