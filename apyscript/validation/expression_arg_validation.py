"""Validation module for expression callable's argument.
"""

from typing import Any, List, Type
from apyscript.expression.acceptable_arg_types import get_acceptable_arg_types

_ACCEPTABLE_TYPES_ERR_MSG: str = (
    'Not acceptable argument type is specified.'
    ' Currently decorated by scope decorator function or'
    ' method\'s acceptable argument types are as follows:'
)


def validate_acceptable_arg_types(args: list, kwargs: dict) -> None:
    """
    Validate expression callable's argument types.

    Parameters
    ----------
    args : list
        Positional arguments to check.
    kwargs : dict
        Keyword arguments to check.

    Raises
    ------
    ValueError
        If not acceptable argument type is specified.
    """
    acceptable_arg_types: List[Type] = get_acceptable_arg_types()
    _validate_args(args=args, acceptable_arg_types=acceptable_arg_types)
    _validate_kwargs(
        kwargs=kwargs, acceptable_arg_types=acceptable_arg_types)
    pass


def _validate_args(args: list, acceptable_arg_types: List[Type]) -> None:
    """
    Validate expression callable's positional argument types.

    Parameters
    ----------
    args : list
        Positional arguments to check.
    acceptable_arg_types : list of types
        Expression callable's acceptable argument types.

    Raises
    ------
    ValueError
        If not acceptable argument type is specified.
    """
    for i, arg in enumerate(args):
        if _is_acceptable_arg(arg=arg, acceptable_types=acceptable_arg_types):
            continue
        raise ValueError(
            f'{_ACCEPTABLE_TYPES_ERR_MSG}'
            f'\n{acceptable_arg_types}'
            f'\n\nArgument index: {i}'
            f'\nArgument type: {type(arg)}'
            f'\nArgument value: {arg}')


def _is_acceptable_arg(arg: Any, acceptable_types: List[Type]) -> bool:
    """
    Get a boolean value whether specified argument type is
    acceptable or not.

    Parameters
    ----------
    arg : *
        Any argument value.
    acceptable_arg_types : list of types
        Expression callable's acceptable argument types.

    Returns
    -------
    result : bool
        If acceptable, True will be set.
    """
    arg_type: Type = type(arg)
    if arg_type in acceptable_types:
        return True
    return False


def _validate_kwargs(kwargs: dict, acceptable_arg_types: List[Type]) -> None:
    """
    Validate expression callable's keyword argument types.

    Parameters
    ----------
    kwargs : dict
        Keyword arguments to check.
    acceptable_arg_types : list of types
        Expression callable's acceptable argument types.

    Raises
    ------
    ValueError
        If not acceptable argument type is specified.
    """
    for arg_name, arg_value in kwargs.items():
        if _is_acceptable_arg(
                arg=arg_value, acceptable_types=acceptable_arg_types):
            continue
        raise ValueError(
            f'{_ACCEPTABLE_TYPES_ERR_MSG}'
            f'\n{acceptable_arg_types}'
            f'\n\nArgument name: {arg_name}'
            f'\nArgument type: {type(arg_value)}'
            f'\nArgument value: {arg_value}')
