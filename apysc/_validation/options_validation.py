"""Validation interfaces for the handler's options argument.
"""

import inspect
from inspect import Signature
from typing import Any, Dict, List

from typing_extensions import TypedDict

from apysc._event.handler import Handler


def validate_options(handler: Handler, options: Any) -> None:
    """
    Validate handler's optional argument dictionary type.

    Parameters
    ----------
    handler : Handler
        Target handler.
    options : dict or None
        Optional argument dictionary.
    """
    if options is None:
        return
    _validate_dict_type(options=options)
    handler_arg_data_list: List[_ArgData] = _get_handler_arg_data_list(
        handler=handler)
    _validate_arg_names(handler_arg_data_list=handler_arg_data_list)
    pass


class _ArgData(TypedDict):
    arg_name: str
    annotation: Any


class _HandlerArgumentsLengthError(Exception):
    pass


class _HandlerFirstArgumentNameError(Exception):
    pass


class _HandlerSecondArgumentNameError(Exception):
    pass


def _validate_arg_names(handler_arg_data_list: List[_ArgData]) -> None:
    """
    Validate handler's argument names and order of arguments.

    Parameters
    ----------
    handler_arg_data_list : list of _ArgData
        Target handler's arguments data list.

    Raises
    ------
    _HandlerArgumentsLengthError
        If a specified arguments length is invalid.
    _HandlerFirstArgumentNameError
        If a specified first argument name is not 'e'.
    _HandlerSecondArgumentNameError
        If a specified second argument name is not 'options'.
    """
    expected_length: int = 2
    actual_length: int = len(handler_arg_data_list)
    if actual_length != expected_length:
        raise _HandlerArgumentsLengthError(
            'Passed handler arguments length is invalid.'
            f'\nExpected length: {expected_length}, passed: {actual_length}')

    first_arg_name: str = handler_arg_data_list[0]['arg_name']
    expected_name: str = 'e'
    if first_arg_name != expected_name:
        raise _HandlerFirstArgumentNameError(
            "Passed handler's first argument name is invalid."
            f'\nExpected argument name: {expected_name}, '
            f'actual: {first_arg_name}')

    second_arg_name: str = handler_arg_data_list[1]['arg_name']
    expected_name = 'options'
    if second_arg_name != expected_name:
        raise _HandlerSecondArgumentNameError(
            "Passed handler's second argument name is invalid."
            f'\nExpected argument name: {expected_name}, '
            f'actual: {second_arg_name}')


def _get_handler_arg_data_list(handler: Handler) -> List[_ArgData]:
    """
    Get a handler's argument(s) data list.

    Parameters
    ----------
    handler : Handler
        Target handler.

    Returns
    -------
    handler_arg_data_list : list of _ArgData
        Argument(s) data list.
    """
    signature: Signature = inspect.signature(handler)
    handler_arg_data_list: List[_ArgData] = []
    for arg_name, parameter in signature.parameters.items():
        handler_arg_data_list.append({
            'arg_name': arg_name,
            'annotation': parameter.annotation,
        })
    return handler_arg_data_list


def _validate_dict_type(options: Any) -> None:
    """
    Validate whether a specified value is dictionary type or not.

    Parameters
    ----------
    options : dict
        Optional argument dictionary.

    Raises
    ------
    TypeError
        If a specified value is not a dictionary type one.
    """
    if isinstance(options, dict):
        return
    raise TypeError(
        'Specified options argument is not dict type or None: '
        f'{type(options)}, {options}')
