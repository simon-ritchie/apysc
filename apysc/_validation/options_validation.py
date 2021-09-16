"""Validation interfaces for the handler's options argument.
"""

import inspect
from inspect import Signature
from typing import Any, Dict

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
    pass


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
