import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.month_mixin import MonthMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestObject(
    MonthMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestMonthMixIn:
    @apply_test_settings()
    def test__set_init_month_value(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_month_value(month=5)
        assert instance._initial_month == 5
        assert isinstance(instance._initial_month, int)
        assert instance._month == 5
        assert isinstance(instance._month, ap.Int)

    @apply_test_settings()
    def test__get_init_month_argument_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_month_value(month=5)
        expression: str = instance._get_init_month_argument_expression()
        assert expression == ", 4"

        int_val: ap.Int = ap.Int(5)
        instance._set_init_month_value(month=int_val)
        expression = instance._get_init_month_argument_expression()
        assert expression == f", {int_val.variable_name} - 1"

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_month_value(month=5)
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance._month._value = 6
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance._month == 5

    @apply_test_settings()
    def test__append_month_getter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_month_mixin"
        instance._set_init_month_value(month=5)
        month_val: ap.Int = ap.Int(7)
        instance._append_month_getter_expression(month_val=month_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{month_val.variable_name} = {instance.variable_name}.getMonth() + 1;"
        )
        assert expected in expression

    @apply_test_settings()
    def test_month(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_month_mixin"
        instance._set_init_month_value(month=5)
        month: ap.Int = instance.month
        assert month == 5
        assert isinstance(month, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{month.variable_name} = {instance.variable_name}.getMonth() + 1;"
        )
        assert expected in expression

        month.value = 7
        instance.month = month
        assert instance.month == 7
        assert isinstance(instance.month, ap.Int)
        expression = expression_data_util.get_current_expression()
        expected = f"{instance.variable_name}.setMonth({month.variable_name} - 1);"

    @apply_test_settings()
    def test__append_month_setter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_month_mixin"
        instance._set_init_month_value(month=5)
        month_val: ap.Int = ap.Int(7)
        instance._append_month_setter_expression(month_val=month_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{instance.variable_name}.setMonth({month_val.variable_name} - 1);"
        )
        assert expected in expression
