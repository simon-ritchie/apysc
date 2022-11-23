from random import randint

from retrying import retry

import apysc as ap
from apysc._time.month_mixin import MonthMixIn


class TestMonthMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_month_value(self) -> None:
        mixin: MonthMixIn = MonthMixIn()
        mixin._set_init_month_value(month=5)
        assert mixin._initial_month == 5
        assert isinstance(mixin._initial_month, int)
        assert mixin._month == 5
        assert isinstance(mixin._month, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_init_month_argument_expression(self) -> None:
        mixin: MonthMixIn = MonthMixIn()
        mixin._set_init_month_value(month=5)
        expression: str = mixin._get_init_month_argument_expression()
        assert expression == ", 4"

        int_val: ap.Int = ap.Int(5)
        mixin._set_init_month_value(month=int_val)
        expression = mixin._get_init_month_argument_expression()
        assert expression == f", {int_val.variable_name} - 1"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot_and_revert(self) -> None:
        mixin: MonthMixIn = MonthMixIn()
        mixin._set_init_month_value(month=5)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._month._value = 6
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._month == 5
