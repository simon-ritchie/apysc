from random import randint

from retrying import retry

from apysc._type.attr_to_apysc_val_from_builtin_interface import \
    AttrToApyscValFromBuiltinInterface
from apysc._type.variable_name_suffix_attr_interface import \
    VariableNameSuffixAttrInterface
from apysc._type.variable_name_suffix_interface import \
    VariableNameSuffixInterface
import apysc as ap


class _TestClass1(AttrToApyscValFromBuiltinInterface):
    pass


class _TestClass2(
        AttrToApyscValFromBuiltinInterface,
        VariableNameSuffixAttrInterface,
        VariableNameSuffixInterface):
    pass


class TestAttrToApyscValFromBuiltinInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_copied_int_from_builtin_val(self) -> None:
        instance_1: _TestClass1 = _TestClass1()
        int_1: ap.Int = instance_1._get_copied_int_from_builtin_val(
            integer=10, attr_identifier='x')
        assert int_1._variable_name_suffix == ''
        assert int_1 == 10
        assert isinstance(int_1, ap.Int)

        instance_2: _TestClass2 = _TestClass2()
        instance_2._variable_name_suffix = 'test_instance'
        int_2: ap.Int = instance_2._get_copied_int_from_builtin_val(
            integer=10, attr_identifier='x')
        assert int_2._variable_name_suffix == 'test_instance__x'
