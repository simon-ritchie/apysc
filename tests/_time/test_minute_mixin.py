from random import randint

from retrying import retry

import apysc as ap
from apysc._time.minute_mixin import MinuteMixIn


class TestMinuteMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_minute_value(self) -> None:
        mixin: MinuteMixIn = MinuteMixIn()
        mixin._set_init_minute_value(minute=30)
        assert mixin._initial_minute == 30
        assert isinstance(mixin._initial_minute, int)
        assert mixin._minute == 30
        assert isinstance(mixin._minute, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_init_minute_argument_expression(self) -> None:
        mixin: MinuteMixIn = MinuteMixIn()
        mixin._set_init_minute_value(minute=30)
        expression: str = mixin._get_init_minute_argument_expression()
        assert expression == ", 30"

        int_val: ap.Int = ap.Int(30)
        mixin._set_init_minute_value(minute=int_val)
        expression = mixin._get_init_minute_argument_expression()
        assert expression == f", {int_val.variable_name}"
