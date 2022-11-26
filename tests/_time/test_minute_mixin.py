from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot_and_revert(self) -> None:
        mixin: MinuteMixIn = MinuteMixIn()
        mixin._set_init_minute_value(minute=30)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._minute._value = 35
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._minute == 30

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_minute_getter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: MinuteMixIn = MinuteMixIn()
        mixin.variable_name = "test_minute_mixin"
        minute_val: ap.Int = ap.Int(30)
        mixin._append_minute_getter_expression(minute_val=minute_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{minute_val.variable_name} = {mixin.variable_name}.getMinutes();"
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_minute(self) -> None:
        expression_data_util.empty_expression()
        mixin: MinuteMixIn = MinuteMixIn()
        mixin.variable_name = "test_minute_mixin"
        mixin._set_init_minute_value(minute=30)
        minute: ap.Int = mixin.minute
        assert minute == 30
        assert isinstance(minute, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{minute.variable_name} = {mixin.variable_name}.getMinutes();"
        assert expected in expression

        minute.value = 35
        mixin.minute = minute
        assert mixin.minute == 35
        expression = expression_data_util.get_current_expression()
        expected = f"{mixin.variable_name}.setMinutes({minute.variable_name});"
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_minute_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: MinuteMixIn = MinuteMixIn()
        mixin.variable_name = "test_minute_mixin"
        minute_val: ap.Int = ap.Int(30)
        mixin._append_minute_setter_expression(minute_val=minute_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.setMinutes({minute_val.variable_name});"
        assert expected in expression
