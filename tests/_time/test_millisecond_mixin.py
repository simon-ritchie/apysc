from random import randint

from retrying import retry

import apysc as ap
from apysc._time.millisecond_mixin import MillisecondMixIn


class TestMillisecondMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_millisecond_value(self) -> None:
        mixin: MillisecondMixIn = MillisecondMixIn()
        mixin._set_init_millisecond_value(millisecond=500)
        assert mixin._initial_millisecond == 500
        assert isinstance(mixin._initial_millisecond, int)
        assert mixin._millisecond == 500
        assert isinstance(mixin._millisecond, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_init_millisecond_argument_expression(self) -> None:
        mixin: MillisecondMixIn = MillisecondMixIn()
        mixin._set_init_millisecond_value(millisecond=500)
        expression: str = mixin._get_init_millisecond_argument_expression()
        assert expression == ", 500"

        int_val: ap.Int = ap.Int(500)
        mixin._set_init_millisecond_value(millisecond=int_val)
        expression = mixin._get_init_millisecond_argument_expression()
        assert expression == f", {int_val.variable_name}"
