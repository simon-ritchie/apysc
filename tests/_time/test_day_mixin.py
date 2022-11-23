from random import randint

from retrying import retry

import apysc as ap
from apysc._time.day_mixin import DayMixIn


class TestDayMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_day_value(self) -> None:
        mixin: DayMixIn = DayMixIn()
        mixin._set_init_day_value(day=15)
        assert mixin._initial_day == 15
        assert isinstance(mixin._initial_day, int)
        assert mixin._day == 15
        assert isinstance(mixin._day, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_init_day_argument_expression(self) -> None:
        mixin: DayMixIn = DayMixIn()
        mixin._set_init_day_value(day=15)
        expression: str = mixin._get_init_day_argument_expression()
        assert expression == ", 15"

        int_val: ap.Int = ap.Int(15)
        mixin._set_init_day_value(day=int_val)
        expression = mixin._get_init_day_argument_expression()
        assert expression == f", {int_val.variable_name}"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot_and_revert(self) -> None:
        mixin: DayMixIn = DayMixIn()
        mixin._set_init_day_value(day=15)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._day._value = 16
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._day == 15
