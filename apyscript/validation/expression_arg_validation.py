"""Validation module for expression callable's argument.
"""

from typing import List, Type
from apyscript.expression.acceptable_arg_types import get_acceptable_arg_types


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
        arg_type: Type = type(arg)
        if arg_type in acceptable_arg_types:
            continue
        raise ValueError(
            'Not acceptable argument type is specified.'
            ' Currently decorated by scope decorator function or'
            ' method\'s acceptable argument types are as follows:'
            f'\n{acceptable_arg_types}'
            f'\n\nInvalid argument index: {i}'
            f'\nSpecified argument type: {type(arg)}'
            f'\nSpecified argument value: {arg}')
