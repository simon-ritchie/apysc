from random import randint

from retrying import retry

import apysc as ap
from apysc._time.weekday_mixin import WeekdayMixin
from apysc._expression import expression_data_util


class TestWeekdayMixin:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_weekday_js_val_with_attrs(self) -> None:
        mixin: WeekdayMixin = WeekdayMixin()
        weekday_js_val: int = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 0

        mixin._year = ap.Int(2022)
        weekday_js_val = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 0

        mixin._month = ap.Int(11)
        weekday_js_val = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 0

        mixin._day = ap.Int(29)
        weekday_js_val = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 2

        mixin._day = ap.Int(27)
        weekday_js_val = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 0
