import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.hour_mixin import HourMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import VariableNameSuffixAttrOrVarMixIn


class _TestObject(
    HourMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestHourMixIn:
    @apply_test_settings()
    def test__set_init_hour_value(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_hour_value(hour=10)
        assert instance._initial_hour == 10
        assert isinstance(instance._initial_hour, int)
        assert instance._hour == 10
        assert isinstance(instance._hour, ap.Int)

    @apply_test_settings()
    def test__get_init_hour_argument_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_hour_value(hour=10)
        expression: str = instance._get_init_hour_argument_expression()
        assert expression == ", 10"

        int_val: ap.Int = ap.Int(10)
        instance._set_init_hour_value(hour=int_val)
        expression = instance._get_init_hour_argument_expression()
        assert expression == f", {int_val.variable_name}"

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_hour_value(hour=10)
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance._hour._value = 11
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance._hour == 10

    @apply_test_settings()
    def test__append_hour_getter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_hour_mixin"
        hour_val: ap.Int = ap.Int(12)
        instance._append_hour_getter_expression(hour_val=hour_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{hour_val.variable_name} = {instance.variable_name}.getHours();"
        assert expected in expression

    @apply_test_settings()
    def test_hour(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_hour_mixin"
        instance._set_init_hour_value(hour=10)
        hour: ap.Int = instance.hour
        assert hour == 10
        assert isinstance(hour, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{hour.variable_name} = {instance.variable_name}.getHours();"
        assert expected in expression

        hour.value = 12
        instance.hour = hour
        assert instance.hour == 12
        assert isinstance(hour, ap.Int)
        expression = expression_data_util.get_current_expression()
        expected = f"{instance.variable_name}.setHours({hour.variable_name});"
        assert expected in expression

    @apply_test_settings()
    def test__append_hour_setter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_hour_mixin"
        hour_val: ap.Int = ap.Int(12)
        instance._append_hour_setter_expression(hour_val=hour_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{instance.variable_name}.setHours({hour_val.variable_name});"
        assert expected in expression
