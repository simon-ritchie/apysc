import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.millisecond_mixin import MillisecondMixIn


class TestMillisecondMixIn:
    @apply_test_settings()
    def test__set_init_millisecond_value(self) -> None:
        mixin: MillisecondMixIn = MillisecondMixIn()
        mixin._set_init_millisecond_value(millisecond=500)
        assert mixin._initial_millisecond == 500
        assert isinstance(mixin._initial_millisecond, int)
        assert mixin._millisecond == 500
        assert isinstance(mixin._millisecond, ap.Int)

    @apply_test_settings()
    def test__get_init_millisecond_argument_expression(self) -> None:
        mixin: MillisecondMixIn = MillisecondMixIn()
        mixin._set_init_millisecond_value(millisecond=500)
        expression: str = mixin._get_init_millisecond_argument_expression()
        assert expression == ", 500"

        int_val: ap.Int = ap.Int(500)
        mixin._set_init_millisecond_value(millisecond=int_val)
        expression = mixin._get_init_millisecond_argument_expression()
        assert expression == f", {int_val.variable_name}"

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        mixin: MillisecondMixIn = MillisecondMixIn()
        mixin._set_init_millisecond_value(millisecond=500)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._millisecond._value = 600
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._millisecond == 500

    @apply_test_settings()
    def test__append_millisecond_getter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: MillisecondMixIn = MillisecondMixIn()
        mixin.variable_name = "test_millisecond_mixin"
        millisecond_val: ap.Int = ap.Int(500)
        mixin._append_millisecond_getter_expression(millisecond_val=millisecond_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{millisecond_val.variable_name} = "
            f"{mixin.variable_name}.getMilliseconds();"
        )
        assert expected in expression

    @apply_test_settings()
    def test_millisecond(self) -> None:
        expression_data_util.empty_expression()
        mixin: MillisecondMixIn = MillisecondMixIn()
        mixin.variable_name = "test_millisecond_mixin"
        mixin._set_init_millisecond_value(millisecond=500)
        millisecond: ap.Int = mixin.millisecond
        assert millisecond == 500
        assert isinstance(millisecond, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{millisecond.variable_name} = {mixin.variable_name}.getMilliseconds();"
        )
        assert expected in expression

        millisecond.value = 550
        mixin.millisecond = millisecond
        assert millisecond == 550
        assert isinstance(millisecond, ap.Int)
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{mixin.variable_name}.setMilliseconds({millisecond.variable_name});"
        )

    @apply_test_settings()
    def test__append_millisecond_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: MillisecondMixIn = MillisecondMixIn()
        mixin.variable_name = "test_millisecond_mixin"
        millisecond_val: ap.Int = ap.Int(500)
        mixin._append_millisecond_setter_expression(millisecond_val=millisecond_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin.variable_name}.setMilliseconds({millisecond_val.variable_name});"
        )
        assert expected in expression
