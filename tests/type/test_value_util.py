from apyscript.type import value_util
from apyscript.type.int import Int


def test_get_value_str_for_expression() -> None:
    int_val: Int = Int(value=10)
    value_str: str = value_util.get_value_str_for_expression(
        value=int_val)
    assert value_str == int_val.variable_name

    value_str = value_util.get_value_str_for_expression(value=10)
    assert value_str == '10'


def test_get_copy() -> None:
    int_val: Int = Int(value=10)
    copied_val_1: Int = value_util.get_copy(value=int_val)
    assert int_val == copied_val_1
    assert int_val.variable_name != copied_val_1.variable_name

    copied_val_2: int = value_util.get_copy(value=100)
    assert copied_val_2 == 100
