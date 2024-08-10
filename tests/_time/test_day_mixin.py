import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.day_mixin import DayMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import VariableNameSuffixAttrOrVarMixIn


class _TestObject(
    DayMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestDayMixIn:
    @apply_test_settings()
    def test__set_init_day_value(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_day_value(day=15)
        assert instance._initial_day == 15
        assert isinstance(instance._initial_day, int)
        assert instance._day == 15
        assert isinstance(instance._day, ap.Int)

    @apply_test_settings()
    def test__get_init_day_argument_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_day_value(day=15)
        expression: str = instance._get_init_day_argument_expression()
        assert expression == ", 15"

        int_val: ap.Int = ap.Int(15)
        instance._set_init_day_value(day=int_val)
        expression = instance._get_init_day_argument_expression()
        assert expression == f", {int_val.variable_name}"

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_day_value(day=15)
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance._day._value = 16
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance._day == 15

    @apply_test_settings()
    def test__append_day_getter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_day_mixin"
        instance._set_init_day_value(day=15)
        day_val: ap.Int = ap.Int(17)
        instance._append_day_getter_expression(day_val=day_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{day_val.variable_name} = {instance.variable_name}.getDate();"
        assert expected in expression

    @apply_test_settings()
    def test_day(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_day_mixin"
        instance._set_init_day_value(day=15)
        day: ap.Int = instance.day
        assert day == 15
        assert isinstance(day, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{day.variable_name} = {instance.variable_name}.getDate();"
        assert expected in expression

        day.value = 17
        instance.day = day
        assert instance.day == 17
        expression = expression_data_util.get_current_expression()
        expected = f"{instance.variable_name}.setDate({day.variable_name});"

    @apply_test_settings()
    def test__append_day_setter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_day_mixin"
        day_val: ap.Int = ap.Int(15)
        instance._append_day_setter_expression(day_val=day_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{instance.variable_name}.setDate({day_val.variable_name});"
        assert expected in expression
