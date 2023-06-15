"""The loop-related utilities implementations.
"""

from typing import Type, Union, TypeVar, cast

from apysc._type.string import String
from apysc._type.int import Int
from apysc._type.boolean import Boolean
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.initialize_for_loop_value_interface import (
    InitializeForLoopValueInterface
)

_DictKey = TypeVar("_DictKey", str, String, int, Int, bool, Boolean)


@add_debug_info_setting(module_name=__name__)
def get_dict_key_for_loop(
    *,
    dict_key_type: Type[_DictKey],
) -> _DictKey:
    """
    Get a dictionary key for a loop-related implementation.

    Parameters
    ----------
    dict_key_type : Type[_DictKey]
        A dictionary key type.

    Returns
    -------
    dict_key : _DictKey
        An initialized dictionary key.
    """
    if issubclass(dict_key_type, InitializeForLoopValueInterface):
        return cast(_DictKey, dict_key_type._initialize_for_loop_value())
    if issubclass(dict_key_type, str):
        return cast(_DictKey, "")
    if issubclass(dict_key_type, int):
        return cast(_DictKey, 0)
    if issubclass(dict_key_type, bool):
        return cast(_DictKey, False)

    raise TypeError(
        f"Unsupported dictionary key type: {type(dict_key_type).__name__}"
        "\nAcceptable types are: `str`, `ap.String`, `int`, `ap.Int`, `bool`, "
        "or `ap.Boolean`."
    )
