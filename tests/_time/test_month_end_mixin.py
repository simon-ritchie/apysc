from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._time.month_end_mixin import MonthEndMixin


class TestMonthEndMixin:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_set_month_end(self) -> None:
        expression_data_util.empty_expression()
        mixin: MonthEndMixin = MonthEndMixin()
        mixin.variable_name = "test_mixin"
        mixin._year = ap.Int(2022)
        mixin._month = ap.Int(12)
        mixin._day = ap.Int(5)
        mixin.set_month_end()
        assert mixin._day == 31

        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin.variable_name}.setDate(1);"
            f"\n{mixin.variable_name}.setMonth({mixin.variable_name}.getMonth() + 1);"
            f"\n{mixin.variable_name}.setDate(0);"
        )
        assert expected in expression
