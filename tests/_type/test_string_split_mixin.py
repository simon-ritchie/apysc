import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.string_split_mixin import StringSplitMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    StringSplitMixIn,
):
    pass


class TestStringSplitMixIn:
    @apply_test_settings()
    def test__append_split_expression(self) -> None:
        ap.Stage()
        mixin: _TestMixIn = _TestMixIn()
        mixin.variable_name = "test_mixin"
        splitted_strs: ap.Array[ap.String] = ap.Array([ap.String("Test")])
        sep: ap.String = ap.String(",")
        mixin._append_split_expression(splitted_strs=splitted_strs, sep=sep)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{splitted_strs.variable_name} = "
            f"{mixin.variable_name}.split({sep.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test_split(self) -> None:
        ap.Stage()
        mixin: _TestMixIn = _TestMixIn()
        mixin.variable_name = "test_mixin"
        mixin._variable_name_suffix = "test_suffix"
        sep: ap.String = ap.String(",")
        splitted_strs: ap.Array[ap.String] = mixin.split(sep=sep)
        assert "test_suffix" in splitted_strs.variable_name
        assert "splitted_strs" in splitted_strs.variable_name
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{splitted_strs.variable_name} = "
            f"{mixin.variable_name}.split({sep.variable_name});"
        )
        assert expected in expression
