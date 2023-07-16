import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestDateTime:
    @apply_test_settings()
    def test___init__(self) -> None:
        datetime: ap.DateTime = ap.DateTime(year=2022, month=3, day=5)
        assert_attrs(
            expected_attrs={
                "_initial_year": 2022,
                "_initial_month": 3,
                "_initial_day": 5,
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

        datetime = ap.DateTime(
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

    @apply_test_settings()
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

    @apply_test_settings()
    def test__create_initial_substitution_expression(self) -> None:
        datetime: ap.DateTime = ap.DateTime(
            year=2022,
            month=3,
            day=5,
            hour=10,
            minute=30,
            second=50,
            millisecond=500,
        )
        expression: str = datetime._create_initial_substitution_expression()
        expected: str = (
            f"{datetime.variable_name} = new Date(2022, 2, 5, 10, 30, 50, 500);"
        )
        assert expression == expected

        datetime = ap.DateTime(
            year=ap.Int(2022, variable_name_suffix="year"),
            month=ap.Int(3, variable_name_suffix="month"),
            day=ap.Int(5, variable_name_suffix="day"),
            hour=ap.Int(10, variable_name_suffix="hour"),
            minute=ap.Int(30, variable_name_suffix="minute"),
            second=ap.Int(50, variable_name_suffix="second"),
            millisecond=ap.Int(500, variable_name_suffix="millisecond"),
            variable_name_suffix="test_datetime",
        )
        expression = datetime._create_initial_substitution_expression()
        print(expression)
        match: Optional[Match] = re.search(
            pattern=(
                rf"{datetime.variable_name} = new Date\(.*?year.*?, .*?month.*?, "
                r".*?day.*?, .*?hour.*?, .*?minute.*?, .*?second.*, "
                r".*?millisecond.*\);"
            ),
            string=expression,
        )
        assert match is not None

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        ap.Stage()
        datetime: ap.DateTime = ap.DateTime(
            year=2022,
            month=3,
            day=5,
            hour=10,
            minute=30,
            second=50,
            millisecond=500,
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"var {datetime.variable_name} = new Date("
        assert expected in expression

    @apply_test_settings()
    def test___sub__(self) -> None:
        ap.Stage()
        left_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=2)
        right_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
        timedelta_: ap.TimeDelta = left_datetime - right_datetime
        assert timedelta_.total_seconds() == 60 * 60 * 24
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{timedelta_.variable_name} = {left_datetime.variable_name}.getTime()"
            f" - {right_datetime.variable_name}.getTime();"
        )
        assert expected in expression
