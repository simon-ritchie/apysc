import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.millisecond_mixin import MillisecondMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import VariableNameSuffixAttrOrVarMixIn


class _TestObject(
    MillisecondMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestMillisecondMixIn:
    @apply_test_settings()
    def test__set_init_millisecond_value(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_millisecond_value(millisecond=500)
        assert instance._initial_millisecond == 500
        assert isinstance(instance._initial_millisecond, int)
        assert instance._millisecond == 500
        assert isinstance(instance._millisecond, ap.Int)

    @apply_test_settings()
    def test__get_init_millisecond_argument_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_millisecond_value(millisecond=500)
        expression: str = instance._get_init_millisecond_argument_expression()
        assert expression == ", 500"

        int_val: ap.Int = ap.Int(500)
        instance._set_init_millisecond_value(millisecond=int_val)
        expression = instance._get_init_millisecond_argument_expression()
        assert expression == f", {int_val.variable_name}"

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_millisecond_value(millisecond=500)
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance._millisecond._value = 600
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance._millisecond == 500

    @apply_test_settings()
    def test__append_millisecond_getter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_millisecond_mixin"
        millisecond_val: ap.Int = ap.Int(500)
        instance._append_millisecond_getter_expression(millisecond_val=millisecond_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{millisecond_val.variable_name} = "
            f"{instance.variable_name}.getMilliseconds();"
        )
        assert expected in expression

    @apply_test_settings()
    def test_millisecond(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_millisecond_mixin"
        instance._set_init_millisecond_value(millisecond=500)
        millisecond: ap.Int = instance.millisecond
        assert millisecond == 500
        assert isinstance(millisecond, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{millisecond.variable_name} = {instance.variable_name}.getMilliseconds();"
        )
        assert expected in expression

        millisecond.value = 550
        instance.millisecond = millisecond
        assert millisecond == 550
        assert isinstance(millisecond, ap.Int)
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{instance.variable_name}.setMilliseconds({millisecond.variable_name});"
        )

    @apply_test_settings()
    def test__append_millisecond_setter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_millisecond_mixin"
        millisecond_val: ap.Int = ap.Int(500)
        instance._append_millisecond_setter_expression(millisecond_val=millisecond_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{instance.variable_name}.setMilliseconds({millisecond_val.variable_name});"
        )
        assert expected in expression
