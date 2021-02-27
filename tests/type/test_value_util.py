from apyscript.type import value_util
from apyscript.type.int import Int


def test_get_value_str_for_expression() -> None:
    int_val: Int = Int(value=10)
    value_str: str = value_util.get_value_str_for_expression(
        value=int_val)
    assert value_str == int_val.variable_name

    value_str = value_util.get_value_str_for_expression(value=10)
    assert value_str == '10'
