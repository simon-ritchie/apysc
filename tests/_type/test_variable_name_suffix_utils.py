from apysc._type import variable_name_suffix_utils
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestClass1:
    pass


class _TestClass2(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    VariableNameMixIn,
):
    pass


@apply_test_settings()
def test_get_attr_or_variable_name_suffix() -> None:
    instance_1: _TestClass1 = _TestClass1()
    suffix: str = variable_name_suffix_utils.get_attr_or_variable_name_suffix(
        instance=instance_1,
        value_identifier="test_1",
    )
    assert suffix == ""

    instance_2: _TestClass2 = _TestClass2()
    instance_2.variable_name = "test_instance"
    instance_2._variable_name_suffix = "test_suffix"
    suffix = variable_name_suffix_utils.get_attr_or_variable_name_suffix(
        instance=instance_2,
        value_identifier="test_2",
    )
    assert "test_suffix" in suffix
    assert "test_2" in suffix
