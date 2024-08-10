import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._time.year_mixin import YearMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import VariableNameSuffixAttrOrVarMixIn


class _TestObject(
    YearMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestYearMixIn:
    @apply_test_settings()
    def test__set_init_year_value(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_year_value(year=2022)
        assert instance._initial_year == 2022
        assert isinstance(instance._initial_year, int)
        assert instance._year == 2022
        assert isinstance(instance._year, ap.Int)

    @apply_test_settings()
    def test__get_init_year_argument_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_year_value(year=2022)
        expression: str = instance._get_init_year_argument_expression()
        assert expression == "2022"

        int_val: ap.Int = ap.Int(2022)
        instance._set_init_year_value(year=int_val)
        expression = instance._get_init_year_argument_expression()
        assert expression == int_val.variable_name

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance._set_init_year_value(year=2022)
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance._year._value = 2021
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance._year == 2022

    @apply_test_settings()
    def test__append_year_getter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_year_mixin"
        year_val: ap.Int = ap.Int(2022)
        instance._append_year_getter_expression(year_val=year_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{year_val.variable_name} = {instance.variable_name}.getFullYear();"
        )
        assert expected in expression

    @apply_test_settings()
    def test_year(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_year_mixin"
        instance._set_init_year_value(year=2022)
        year: ap.Int = instance.year
        assert year == 2022
        assert isinstance(year, ap.Int)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{year.variable_name} = {instance.variable_name}.getFullYear();"
        assert expected in expression

        year = ap.Int(2023)
        instance.year = year
        assert instance.year == 2023
        assert isinstance(year, ap.Int)
        expression = expression_data_util.get_current_expression()
        expected = f"{instance.variable_name}.setFullYear({year.variable_name});"
        assert expected in expression

    @apply_test_settings()
    def test__append_year_setter_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_year_mixin"
        instance._set_init_year_value(year=2022)
        year_val: ap.Int = ap.Int(2023)
        instance._append_year_setter_expression(year_val=year_val)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{instance.variable_name}.setFullYear({year_val.variable_name});"
        assert expected in expression
