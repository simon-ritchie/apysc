from random import randint

from retrying import retry

import apysc as ap
from apysc._time.second_mixin import SecondMixIn


class TestSecondMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_second_value(self) -> None:
        mixin: SecondMixIn = SecondMixIn()
        mixin._set_init_second_value(second=50)
        assert mixin._initial_second == 50
        assert isinstance(mixin._initial_second, int)
        assert mixin._second == 50
        assert isinstance(mixin._second, ap.Int)
