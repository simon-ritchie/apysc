"""This module is for the handler interfaces'
validation implementations.
"""

import inspect
from inspect import Signature
from typing import Any, Callable, List


def validate_options_type(*, options: Any) -> None:
    """
    Validate a specified options type.

    Parameters
    ----------
    options : Any
        Target options value.

    Raises
    ------
    TypeError
        If a specified options type is not the dictionary or None.
    """
    if options is None:
        return
    if isinstance(options, dict):
        return
    raise TypeError(
        f"Handler's options argument must be a dictionary: {type(options)}"
        f'\n{options}')


def validate_handler_args_num(*, handler: Callable) -> None:
    """
    Validate specified handler's arguments number.

    Parameters
    ----------
    handler : Callable
        A target handler to validate.

    Raises
    ------
    ValueError
        - If handler's arguments number is not 2.
    """
    signature: Signature = inspect.signature(obj=handler)
    args_num: int = 0
    skipping_arg_names: List[str] = ['*', '**', 'self', 'cls']
    arg_names: List[str] = []
    for parameter in signature.parameters:
        if parameter in skipping_arg_names:
            continue
        args_num += 1
        arg_names.append(parameter)
    if args_num != 2:
        raise ValueError(
            'A specified handler\'s arguments number must be 2 '
            f'(actual: {args_num})'
            f'\nTarget argument names: {arg_names}'
            '\n\nThe first argument becomes event instance and the second '
            'one becomes the handler\'s option parameters.')
