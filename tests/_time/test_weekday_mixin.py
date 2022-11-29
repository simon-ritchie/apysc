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

        mixin._day = ap.Int(26)
        weekday_js_val = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 6

        mixin._day = ap.Int(27)
        weekday_js_val = mixin._get_weekday_js_val_with_attrs()
        assert weekday_js_val == 0

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_weekday_js_getter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: WeekdayMixin = WeekdayMixin()
        mixin.variable_name = "test_weekday_mixin"
        weekday_val: ap.Int = ap.Int(3)
        mixin._append_weekday_js_getter_expression(weekday_val=weekday_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{weekday_val.variable_name} = {mixin.variable_name}.getDay();"
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_weekday_js(self) -> None:
        expression_data_util.empty_expression()
        mixin: WeekdayMixin = WeekdayMixin()
        mixin.variable_name = "test_weekday_mixin"
        mixin._year = ap.Int(2022)
        mixin._month = ap.Int(11)
        mixin._day = ap.Int(29)
        weekday: ap.Int = mixin.weekday_js
        assert weekday == 2
        assert isinstance(weekday, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{weekday.variable_name} = {mixin.variable_name}.getDay();"
        )
        assert expected in expression
