from typing import List, Type
from apyscript.expression import acceptable_arg_types
from apyscript.display.stage import Stage
from apyscript.display.sprite import DisplayObject
from apyscript.display.variable_name_interface import VariableNameInterface


def test_get_acceptable_arg_types() -> None:
    arg_types: List[Type] = acceptable_arg_types.get_acceptable_arg_types()
    assert Stage in arg_types
    assert DisplayObject in arg_types


def test_acceptable_arg_types_have_variable_name_interface() -> None:
    arg_types: List[Type] = acceptable_arg_types.get_acceptable_arg_types()
    for arg_type in arg_types:
        assert issubclass(arg_type, VariableNameInterface)
        print(arg_type)
