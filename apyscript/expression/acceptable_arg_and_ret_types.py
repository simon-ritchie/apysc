"""Definition of callable's acceptable arguments and return value(s).
"""


from typing import List, Type

from apyscript.display.variable_name_interface import VariableNameInterface


def get_common_acceptable_types() -> List[Type[VariableNameInterface]]:
    """
    Get argument and return value(s) common acceptable types.

    Notes
    -----
    To avoid recursive import, each modules are imported in
    this function (not on top-level scope).

    Returns
    -------
    acceptable_types : list of type
        Common acceptable types.
    """
    from apyscript.display.stage import Stage
    from apyscript.display.sprite import DisplayObject
    from apyscript.display.graphics import Graphics
    from apyscript.display.graphic_base import GraphicBase
    acceptable_types: List[Type] = [
        Stage,
        DisplayObject,
        Graphics,
        GraphicBase,
    ]
    return acceptable_types


def get_acceptable_arg_types() -> List[Type[VariableNameInterface]]:
    """
    Get expression callable's acceptable argument types.

    Notes
    -----
    To avoid recursive import, each modules are imported in
    this function (not on top-level scope).

    Returns
    -------
    arg_types : list of type
        Acceptable argument types.
    """
    arg_types: List[Type[VariableNameInterface]] = \
        get_common_acceptable_types()
    return arg_types


def get_acceptable_return_val_types() -> List[Type]:
    """
    Get expression callable's acceptable return value(s) types.

    Notes
    -----
    To avoid recursive import, each modules are imported in
    this function (not on top-level scope).

    Returns
    -------
    return_val_types : list of type
        Acceptable return value(s) types.
    """
    return_val_types: List[Type] = [tuple, *get_common_acceptable_types()]
    return return_val_types
