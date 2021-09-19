"""Validation implementations for the handler's options value.
"""

from typing import Any


def validate_options_type(options: Any) -> None:
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
