import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.second_mixin import SecondMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import VariableNameSuffixAttrOrVarMixIn


class _TestObject(
    SecondMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestSecondMixIn:
    @apply_test_settings()
    def test__set_init_second_value(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_second_value(second=50)
        assert instance._initial_second == 50
        assert isinstance(instance._initial_second, int)
        assert instance._second == 50
        assert isinstance(instance._second, ap.Int)

    @apply_test_settings()
    def test__get_init_second_argument_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_second_value(second=50)
        expression: str = instance._get_init_second_argument_expression()
        assert expression == ", 50"

        int_val: ap.Int = ap.Int(50)
        instance._set_init_second_value(second=int_val)
        expression = instance._get_init_second_argument_expression()
        assert expression == f", {int_val.variable_name}"

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_second_value(second=50)
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance._second._value = 55
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance._second == 50

    @apply_test_settings()
    def test__append_second_getter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_second_mixin"
        second_val: ap.Int = ap.Int(50)
        instance._append_second_getter_expression(second_val=second_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{second_val.variable_name} = {instance.variable_name}.getSeconds();"
        )
        assert expected in expression

    @apply_test_settings()
    def test_second(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_second_mixin"
        instance._set_init_second_value(second=50)
        second: ap.Int = instance.second
        assert second == 50
        assert isinstance(second, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{second.variable_name} = {instance.variable_name}.getSeconds();"
        assert expected in expression

        second.value = ap.Int(55)
        instance.second = second
        expression = expression_data_util.get_current_expression()
        expectd = f"{instance.variable_name}.setSeconds({second.variable_name});"
        assert expectd in expression

    @apply_test_settings()
    def test__append_second_setter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_second_mixin"
        second_val: ap.Int = ap.Int(50)
        instance._append_second_setter_expression(second_val=second_val)
        expression: str = expression_data_util.get_current_expression()
        expectd: str = f"{instance.variable_name}.setSeconds({second_val.variable_name});"
        assert expectd in expression
