from random import randint
from typing import List, Type

from retrying import retry

from apyscript.expression import acceptable_arg_and_ret_types
from apyscript.display.stage import Stage
from apyscript.display.sprite import DisplayObject, Sprite
from apyscript.display.variable_name_interface import VariableNameInterface


def test_get_acceptable_arg_types() -> None:
    arg_types: List[Type[VariableNameInterface]] = \
        acceptable_arg_and_ret_types.get_acceptable_arg_types()
    assert Stage in arg_types
    assert DisplayObject in arg_types


def test_acceptable_arg_types_have_variable_name_interface() -> None:
    arg_types: List[Type[VariableNameInterface]] = \
        acceptable_arg_and_ret_types.get_acceptable_arg_types()
    for arg_type in arg_types:
        assert issubclass(arg_type, VariableNameInterface)


def test_get_common_acceptable_types() -> None:
    acceptable_types: List[Type[VariableNameInterface]] = \
        acceptable_arg_and_ret_types.get_common_acceptable_types()
    assert Stage in acceptable_types
    assert DisplayObject in acceptable_types


def test_get_acceptable_return_val_types() -> None:
    return_val_types: List[Type] = acceptable_arg_and_ret_types.\
        get_acceptable_return_val_types()
    assert tuple in return_val_types
    assert Stage in return_val_types


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_is_acceptable_return_val_tuple() -> None:
    stage: Stage = Stage()
    result: bool = acceptable_arg_and_ret_types.\
        is_acceptable_return_val_tuple(
            return_val_tuple=(100, stage))
    assert not result

    sprite: Sprite = Sprite(stage=stage)
    result = acceptable_arg_and_ret_types.is_acceptable_return_val_tuple(
        return_val_tuple=(stage, sprite))
    assert result
