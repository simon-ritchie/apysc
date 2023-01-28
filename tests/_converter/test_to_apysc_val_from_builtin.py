from random import randint

from retrying import retry

import apysc as ap
from apysc._converter import to_apysc_val_from_builtin
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_get_copied_int_from_builtin_val() -> None:
    copied: ap.Int = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
        integer=10, variable_name_suffix="test_value"
    )
    assert copied == 10
    assert isinstance(copied, ap.Int)
    assert copied._variable_name_suffix == "test_value"

    int_1: ap.Int = ap.Int(20)
    copied = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(integer=int_1)
    assert copied == 20
    assert isinstance(copied, ap.Int)
    assert int_1.variable_name != copied.variable_name


@apply_test_settings()
def test_get_copied_string_from_builtin_val() -> None:
    copied: ap.String = to_apysc_val_from_builtin.get_copied_string_from_builtin_val(
        string="Hello", variable_name_suffix="test_string"
    )
    assert copied == "Hello"
    assert isinstance(copied, ap.String)
    assert copied._variable_name_suffix == "test_string"

    string: ap.String = ap.String("World")
    copied = to_apysc_val_from_builtin.get_copied_string_from_builtin_val(string=string)
    assert copied == "World"
    assert isinstance(copied, ap.String)
    assert string.variable_name != copied.variable_name


@apply_test_settings()
def test_get_copied_number_from_builtin_val() -> None:
    num: ap.Number = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
        float_or_num=10.5, variable_name_suffix="test_number"
    )
    assert isinstance(num, ap.Number)
    assert num == ap.Number(10.5)
    assert num._variable_name_suffix == "test_number"

    num = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
        float_or_num=ap.Number(20.5)
    )
    assert isinstance(num, ap.Number)
    assert num == ap.Number(20.5)


@apply_test_settings()
def test_get_copied_boolean_from_builtin_val() -> None:
    copied: ap.Boolean = to_apysc_val_from_builtin.get_copied_boolean_from_builtin_val(
        bool_val=True, variable_name_suffix="test_boolean"
    )
    assert isinstance(copied, ap.Boolean)
    assert copied
    assert copied._variable_name_suffix == "test_boolean"

    original_boolean: ap.Boolean = ap.Boolean(True)
    copied = to_apysc_val_from_builtin.get_copied_boolean_from_builtin_val(
        bool_val=original_boolean
    )
    assert isinstance(copied, ap.Boolean)
    assert copied
    assert original_boolean.variable_name != copied.variable_name
