from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._time.total_seconds_mixin import TotalSecondsMixIn


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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_total_seconds_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: TotalSecondsMixIn = TotalSecondsMixIn()
        total_seconds: ap.Number = ap.Number(10.5)
        mixin.variable_name = "test_mixin"
        mixin._append_total_seconds_expression(total_seconds=total_seconds)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{total_seconds.variable_name} = {mixin.variable_name} / 1000;"
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_total_seconds(self) -> None:
        expression_data_util.empty_expression()
        left_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=2)
        right_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
        mixin: TotalSecondsMixIn = TotalSecondsMixIn()
        mixin.variable_name = "test_mixin"
        mixin._set_init_total_seconds_value_for_python(
            left_datetime=left_datetime,
            right_datetime=right_datetime,
        )
        total_seconds: ap.Number = mixin.total_seconds()
        assert total_seconds == 60 * 60 * 24
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{total_seconds.variable_name} = {mixin.variable_name} / 1000;"
        assert expected in expression
