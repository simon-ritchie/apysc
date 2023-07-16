import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.day_mixin import DayMixIn


class TestDayMixIn:
    @apply_test_settings()
    def test__set_init_day_value(self) -> None:
        mixin: DayMixIn = DayMixIn()
        mixin._set_init_day_value(day=15)
        assert mixin._initial_day == 15
        assert isinstance(mixin._initial_day, int)
        assert mixin._day == 15
        assert isinstance(mixin._day, ap.Int)

    @apply_test_settings()
    def test__get_init_day_argument_expression(self) -> None:
        mixin: DayMixIn = DayMixIn()
        mixin._set_init_day_value(day=15)
        expression: str = mixin._get_init_day_argument_expression()
        assert expression == ", 15"

        int_val: ap.Int = ap.Int(15)
        mixin._set_init_day_value(day=int_val)
        expression = mixin._get_init_day_argument_expression()
        assert expression == f", {int_val.variable_name}"

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        mixin: DayMixIn = DayMixIn()
        mixin._set_init_day_value(day=15)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._day._value = 16
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._day == 15

    @apply_test_settings()
    def test__append_day_getter_expression(self) -> None:
        ap.Stage()
        mixin: DayMixIn = DayMixIn()
        mixin.variable_name = "test_day_mixin"
        mixin._set_init_day_value(day=15)
        day_val: ap.Int = ap.Int(17)
        mixin._append_day_getter_expression(day_val=day_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{day_val.variable_name} = {mixin.variable_name}.getDate();"
        assert expected in expression

    @apply_test_settings()
    def test_day(self) -> None:
        ap.Stage()
        mixin: DayMixIn = DayMixIn()
        mixin.variable_name = "test_day_mixin"
        mixin._set_init_day_value(day=15)
        day: ap.Int = mixin.day
        assert day == 15
        assert isinstance(day, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{day.variable_name} = {mixin.variable_name}.getDate();"
        assert expected in expression

        day.value = 17
        mixin.day = day
        assert mixin.day == 17
        expression = expression_data_util.get_current_expression()
        expected = f"{mixin.variable_name}.setDate({day.variable_name});"

    @apply_test_settings()
    def test__append_day_setter_expression(self) -> None:
        ap.Stage()
        mixin: DayMixIn = DayMixIn()
        mixin.variable_name = "test_day_mixin"
        day_val: ap.Int = ap.Int(15)
        mixin._append_day_setter_expression(day_val=day_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.setDate({day_val.variable_name});"
        assert expected in expression
