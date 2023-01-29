import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.hour_mixin import HourMixIn


class TestHourMixIn:
    @apply_test_settings()
    def test__set_init_hour_value(self) -> None:
        mixin: HourMixIn = HourMixIn()
        mixin._set_init_hour_value(hour=10)
        assert mixin._initial_hour == 10
        assert isinstance(mixin._initial_hour, int)
        assert mixin._hour == 10
        assert isinstance(mixin._hour, ap.Int)

    @apply_test_settings()
    def test__get_init_hour_argument_expression(self) -> None:
        mixin: HourMixIn = HourMixIn()
        mixin._set_init_hour_value(hour=10)
        expression: str = mixin._get_init_hour_argument_expression()
        assert expression == ", 10"

        int_val: ap.Int = ap.Int(10)
        mixin._set_init_hour_value(hour=int_val)
        expression = mixin._get_init_hour_argument_expression()
        assert expression == f", {int_val.variable_name}"

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        mixin: HourMixIn = HourMixIn()
        mixin._set_init_hour_value(hour=10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._hour._value = 11
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._hour == 10

    @apply_test_settings()
    def test__append_hour_getter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: HourMixIn = HourMixIn()
        mixin.variable_name = "test_hour_mixin"
        hour_val: ap.Int = ap.Int(12)
        mixin._append_hour_getter_expression(hour_val=hour_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{hour_val.variable_name} = {mixin.variable_name}.getHours();"
        assert expected in expression

    @apply_test_settings()
    def test_hour(self) -> None:
        expression_data_util.empty_expression()
        mixin: HourMixIn = HourMixIn()
        mixin.variable_name = "test_hour_mixin"
        mixin._set_init_hour_value(hour=10)
        hour: ap.Int = mixin.hour
        assert hour == 10
        assert isinstance(hour, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{hour.variable_name} = {mixin.variable_name}.getHours();"
        assert expected in expression

        hour.value = 12
        mixin.hour = hour
        assert mixin.hour == 12
        assert isinstance(hour, ap.Int)
        expression = expression_data_util.get_current_expression()
        expected = f"{mixin.variable_name}.setHours({hour.variable_name});"
        assert expected in expression

    @apply_test_settings()
    def test__append_hour_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: HourMixIn = HourMixIn()
        mixin.variable_name = "test_hour_mixin"
        hour_val: ap.Int = ap.Int(12)
        mixin._append_hour_setter_expression(hour_val=hour_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.setHours({hour_val.variable_name});"
        assert expected in expression
