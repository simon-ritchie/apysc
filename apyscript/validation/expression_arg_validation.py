"""Validation module for expression callable's argument.

Mainly following interfaces are defined:

- validate_acceptable_arg_types
    Validate expression callable's argument types.
- validate_default_values_not_exist
    Validate specified function's arguments have no default value.
"""

from typing import Any, Callable, Dict, List, Type
from apyscript.expression.acceptable_arg_and_ret_types import \
    get_acceptable_arg_types, get_acceptable_return_val_types
from apyscript.expression.acceptable_arg_and_ret_types import \
    is_acceptable_return_val_tuple, get_common_acceptable_types
from apyscript.callable import callable_util

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


def validate_default_values_not_exist(func: Callable) -> None:
    """
    Validate specified function has no default value.

    Parameters
    ----------
    func : Callable
        Target function (or method) to check.

    Raises
    ------
    ValueError
        If any argument has a default value.
    """
    default_vals: Dict[str, Any] = callable_util.get_func_default_vals(
        func=func)
    for arg_name, default_val in default_vals.items():
        if default_val is callable_util.empty:
            continue
        raise ValueError(
            'This function can not be set default value.'
            f'\nArgument name: {arg_name}'
            f'\nDefault value: {default_val}')


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
    for acceptable_type in acceptable_types:
        if issubclass(arg_type, acceptable_type):
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


def _is_acceptable_return_val(
        return_val: Any, acceptable_types: List[Type]) -> bool:
    """
    Get a boolean value whether specified return value's type is
    acceptable or not.

    Parameters
    ----------
    return_val : *
        Any return value.
    acceptable_types : list of types
        Expression callable's acceptable return value types.

    Returns
    -------
    result : bool
        If acceptable, True will be set.
    """
    return_val_type: Type = type(return_val)
    if return_val_type in acceptable_types:
        return True
    for acceptable_type in acceptable_types:
        if issubclass(return_val_type, acceptable_type):
            return True
    return False


def validate_acceptable_return_types(returned_val: Any) -> None:
    """
    Validate expression callable's return value(s) types.

    Parameters
    ----------
    returned_val : *
        Return value(s) that obtained by function call.

    Raises
    ------
    ValueError
        If not acceptable return value(s) type is specified.
    """
    if returned_val is None:
        return
    acceptable_types: List[Type] = get_acceptable_return_val_types()
    is_acceptable_return_val: bool = _is_acceptable_return_val(
        return_val=returned_val,
        acceptable_types=acceptable_types)
    if not is_acceptable_return_val:
        raise ValueError(
            'Return value\'s type is not acceptable.'
            f'\nAcceptable types: {acceptable_types}'
            f'\nReturn value\'s type: {type(returned_val)}')
    if not isinstance(returned_val, tuple):
        return
    if is_acceptable_return_val_tuple(return_val_tuple=returned_val):
        return
    acceptable_types = get_common_acceptable_types()
    tuple_vals_types: List[Type] = [
        type(tuple_value) for tuple_value in returned_val]
    raise ValueError(
        'Return value in tuple\'s type is not acceptable.'
        f'\nAcceptable types: {acceptable_types}'
        f'\nTuple values types: {tuple_vals_types}')
