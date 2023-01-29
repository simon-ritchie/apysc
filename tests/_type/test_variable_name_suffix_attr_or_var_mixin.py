from random import randint

from retrying import retry

from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._testing.testing_helper import apply_test_settings


class _TestClass1(VariableNameSuffixAttrOrVarMixIn):
    pass


class _TestClass2(VariableNameSuffixMixIn, VariableNameSuffixAttrOrVarMixIn):
    pass


class TestVariableNameSuffixAttrOrVarMixIn:
    @apply_test_settings()
    def test__get_attr_or_variable_name_suffix(self) -> None:
        instance_1: _TestClass1 = _TestClass1()
        assert instance_1._get_attr_or_variable_name_suffix(value_identifier="x") == ""

        instance_2: _TestClass2 = _TestClass2()
        assert instance_2._get_attr_or_variable_name_suffix(value_identifier="x") == ""

        instance_2._variable_name_suffix = "test_instance"
        assert (
            instance_2._get_attr_or_variable_name_suffix(value_identifier="x")
            == "test_instance__x"
        )
