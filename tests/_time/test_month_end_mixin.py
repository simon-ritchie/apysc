import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.month_end_mixin import MonthEndMixin


class TestMonthEndMixin:
    @apply_test_settings()
    def test_set_month_end(self) -> None:
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
