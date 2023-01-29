import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.month_mixin import MonthMixIn


class TestMonthMixIn:
    @apply_test_settings()
    def test__set_init_month_value(self) -> None:
        mixin: MonthMixIn = MonthMixIn()
        mixin._set_init_month_value(month=5)
        assert mixin._initial_month == 5
        assert isinstance(mixin._initial_month, int)
        assert mixin._month == 5
        assert isinstance(mixin._month, ap.Int)

    @apply_test_settings()
    def test__get_init_month_argument_expression(self) -> None:
        mixin: MonthMixIn = MonthMixIn()
        mixin._set_init_month_value(month=5)
        expression: str = mixin._get_init_month_argument_expression()
        assert expression == ", 4"

        int_val: ap.Int = ap.Int(5)
        mixin._set_init_month_value(month=int_val)
        expression = mixin._get_init_month_argument_expression()
        assert expression == f", {int_val.variable_name} - 1"

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        mixin: MonthMixIn = MonthMixIn()
        mixin._set_init_month_value(month=5)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._month._value = 6
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._month == 5

    @apply_test_settings()
    def test__append_month_getter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: MonthMixIn = MonthMixIn()
        mixin.variable_name = "test_month_mixin"
        mixin._set_init_month_value(month=5)
        month_val: ap.Int = ap.Int(7)
        mixin._append_month_getter_expression(month_val=month_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{month_val.variable_name} = {mixin.variable_name}.getMonth() + 1;"
        )
        assert expected in expression

    @apply_test_settings()
    def test_month(self) -> None:
        expression_data_util.empty_expression()
        mixin: MonthMixIn = MonthMixIn()
        mixin.variable_name = "test_month_mixin"
        mixin._set_init_month_value(month=5)
        month: ap.Int = mixin.month
        assert month == 5
        assert isinstance(month, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{month.variable_name} = {mixin.variable_name}.getMonth() + 1;"
        assert expected in expression

        month.value = 7
        mixin.month = month
        assert mixin.month == 7
        assert isinstance(mixin.month, ap.Int)
        expression = expression_data_util.get_current_expression()
        expected = f"{mixin.variable_name}.setMonth({month.variable_name} - 1);"

    @apply_test_settings()
    def test__append_month_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: MonthMixIn = MonthMixIn()
        mixin.variable_name = "test_month_mixin"
        mixin._set_init_month_value(month=5)
        month_val: ap.Int = ap.Int(7)
        mixin._append_month_setter_expression(month_val=month_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin.variable_name}.setMonth({month_val.variable_name} - 1);"
        )
        assert expected in expression
