from random import randint

from retrying import retry

import apysc as ap
from apysc._time.hour_mixin import HourMixIn


class TestHourMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_hour_value(self) -> None:
        mixin: HourMixIn = HourMixIn()
        mixin._set_init_hour_value(hour=10)
        assert mixin._initial_hour == 10
        assert isinstance(mixin._initial_hour, int)
        assert mixin._hour == 10
        assert isinstance(mixin._hour, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_init_hour_argument_expression(self) -> None:
        mixin: HourMixIn = HourMixIn()
        mixin._set_init_hour_value(hour=10)
        expression: str = mixin._get_init_hour_argument_expression()
        assert expression == ", 10"

        int_val: ap.Int = ap.Int(10)
        mixin._set_init_hour_value(hour=int_val)
        expression = mixin._get_init_hour_argument_expression()
        assert expression == f", {int_val.variable_name}"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot_and_revert(self) -> None:
        mixin: HourMixIn = HourMixIn()
        mixin._set_init_hour_value(hour=10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._hour._value = 11
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._hour == 10
