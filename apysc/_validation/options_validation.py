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
    pass


class _ArgData(TypedDict):
    arg_name: str
    annotation: Any


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
