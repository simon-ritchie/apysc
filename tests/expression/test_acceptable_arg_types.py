from typing import List, Type
from apyscript.expression import acceptable_arg_types
from apyscript.display.stage import Stage
from apyscript.display.sprite import DisplayObject


def test_get_acceptable_arg_types() -> None:
    arg_types: List[Type] = acceptable_arg_types.get_acceptable_arg_types()
    assert Stage in arg_types
    assert DisplayObject in arg_types
