import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.minute_mixin import MinuteMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import VariableNameSuffixAttrOrVarMixIn


class _TestObject(
    MinuteMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestMinuteMixIn:
    @apply_test_settings()
    def test__set_init_minute_value(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_minute_value(minute=30)
        assert instance._initial_minute == 30
        assert isinstance(instance._initial_minute, int)
        assert instance._minute == 30
        assert isinstance(instance._minute, ap.Int)

    @apply_test_settings()
    def test__get_init_minute_argument_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_minute_value(minute=30)
        expression: str = instance._get_init_minute_argument_expression()
        assert expression == ", 30"

        int_val: ap.Int = ap.Int(30)
        instance._set_init_minute_value(minute=int_val)
        expression = instance._get_init_minute_argument_expression()
        assert expression == f", {int_val.variable_name}"

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_minute_value(minute=30)
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance._minute._value = 35
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance._minute == 30

    @apply_test_settings()
    def test__append_minute_getter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_minute_mixin"
        minute_val: ap.Int = ap.Int(30)
        instance._append_minute_getter_expression(minute_val=minute_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{minute_val.variable_name} = {instance.variable_name}.getMinutes();"
        )
        assert expected in expression

    @apply_test_settings()
    def test_minute(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_minute_mixin"
        instance._set_init_minute_value(minute=30)
        minute: ap.Int = instance.minute
        assert minute == 30
        assert isinstance(minute, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{minute.variable_name} = {instance.variable_name}.getMinutes();"
        assert expected in expression

        minute.value = 35
        instance.minute = minute
        assert instance.minute == 35
        expression = expression_data_util.get_current_expression()
        expected = f"{instance.variable_name}.setMinutes({minute.variable_name});"
        assert expected in expression

    @apply_test_settings()
    def test__append_minute_setter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_minute_mixin"
        minute_val: ap.Int = ap.Int(30)
        instance._append_minute_setter_expression(minute_val=minute_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{instance.variable_name}.setMinutes({minute_val.variable_name});"
        assert expected in expression
