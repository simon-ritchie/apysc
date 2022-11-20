from random import randint

from retrying import retry

import apysc as ap
from apysc._time.year_mixin import YearMixIn


class TestYearMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_init_year_value(self) -> None:
        mixin: YearMixIn = YearMixIn()
        mixin._set_init_year_value(year=2022)
        assert mixin._initial_year == 2022
        assert isinstance(mixin._initial_year, int)
        assert mixin._year == 2022
        assert isinstance(mixin._year, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_init_year_argument_expression(self) -> None:
        mixin: YearMixIn = YearMixIn()
        mixin._set_init_year_value(year=2022)
        expression: str = mixin._get_init_year_argument_expression()
        assert expression == "2022"

        int_val: ap.Int = ap.Int(2022)
        mixin._set_init_year_value(year=int_val)
        expression = mixin._get_init_year_argument_expression()
        assert expression == int_val.variable_name
