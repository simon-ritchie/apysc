import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._type import attr_to_apysc_val_from_builtin_mixin
from apysc._type.attr_to_apysc_val_from_builtin_mixin import (
    AttrToApyscValFromBuiltinMixIn,
)
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestClass1(AttrToApyscValFromBuiltinMixIn):
    pass


class _TestClass2(
    AttrToApyscValFromBuiltinMixIn,
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
):
    pass


class TestAttrToApyscValFromBuiltinMixIn:
    @apply_test_settings()
    def test__get_copied_int_from_builtin_val(self) -> None:
        instance_1: _TestClass1 = _TestClass1()
        int_1: ap.Int = instance_1._get_copied_int_from_builtin_val(
            integer=10, attr_identifier="x"
        )
        assert int_1._variable_name_suffix == ""
        assert int_1 == 10
        assert isinstance(int_1, ap.Int)

        instance_2: _TestClass2 = _TestClass2()
        instance_2._variable_name_suffix = "test_instance"
        int_2: ap.Int = instance_2._get_copied_int_from_builtin_val(
            integer=10, attr_identifier="x"
        )
        assert int_2._variable_name_suffix == "test_instance__x"

    @apply_test_settings()
    def test__get_copied_number_from_builtin_val(self) -> None:
        instance_2: _TestClass2 = _TestClass2()
        instance_2._variable_name_suffix = "test_instance"
        copied: ap.Number = instance_2._get_copied_number_from_builtin_val(
            float_or_num=10.5, attr_identifier="fill_alpha"
        )
        assert copied == 10.5
        assert isinstance(copied, ap.Number)
        assert copied._variable_name_suffix == "test_instance__fill_alpha"

    @apply_test_settings()
    def test__get_copied_string_from_builtin_val(self) -> None:
        instance_2: _TestClass2 = _TestClass2()
        instance_2._variable_name_suffix = "test_instance"
        copied: ap.String = instance_2._get_copied_string_from_builtin_val(
            string="Hello", attr_identifier="fill_color"
        )
        assert copied == "Hello"
        assert isinstance(copied, ap.String)
        assert copied._variable_name_suffix == "test_instance__fill_color"

    @apply_test_settings()
    def test__get_copied_boolean_from_builtin_val(self) -> None:
        instance_2: _TestClass2 = _TestClass2()
        instance_2._variable_name_suffix = "test_instance"
        copied: ap.Boolean = instance_2._get_copied_boolean_from_builtin_val(
            bool_val=True, attr_identifier="visible"
        )
        assert copied
        assert isinstance(copied, ap.Boolean)
        assert copied._variable_name_suffix == "test_instance__visible"


@apply_test_settings()
def test__get_variable_name_suffix() -> None:
    instance_1: _TestClass1 = _TestClass1()
    suffix: str = attr_to_apysc_val_from_builtin_mixin._get_variable_name_suffix(
        instance=instance_1, attr_identifier="x"
    )
    assert suffix == ""

    instance_2: _TestClass2 = _TestClass2()
    instance_2._variable_name_suffix = "test_instance"
    suffix = attr_to_apysc_val_from_builtin_mixin._get_variable_name_suffix(
        instance=instance_2, attr_identifier="x"
    )
    assert suffix == "test_instance__x"
