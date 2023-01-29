from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._time.days_mixin import DaysMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestDaysMixIn:
    @apply_test_settings()
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

    @apply_test_settings()
    def test__append_days_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: DaysMixIn = DaysMixIn()
        days: ap.Int = ap.Int(5)
        mixin.variable_name = "test_days_mixin"
        mixin._append_days_expression(days=days)
        expected: str = (
            f"{days.variable_name} = Math.trunc({mixin.variable_name} / "
            "(1000 * 60 * 60 * 24));"
        )
        expression: str = expression_data_util.get_current_expression()
        assert expected in expression

    # @apply_test_settings()
    def test_days(self) -> None:
        expression_data_util.empty_expression()
        mixin: DaysMixIn = DaysMixIn()
        mixin.variable_name = "test_days_mixin"
        mixin._days_value = 3
        days: ap.Int = mixin.days
        assert days == 3
        assert isinstance(days, ap.Int)
        expected: str = (
            f"{days.variable_name} = Math.trunc({mixin.variable_name} / "
            "(1000 * 60 * 60 * 24));"
        )
        expression: str = expression_data_util.get_current_expression()
        assert expected in expression
