"""Boolean value's validation implementations.
"""

from typing import Union

import apysc as ap


def validate_bool(value: Union[bool, ap.Boolean]) -> None:
    """
    Validate specified value is bool or Boolean type.

    Parameters
    ----------
    value : bool or Boolean
        Boolean value to check.

    Raises
    ------
    ValueError
        If specified value isn't bool or Boolean type.
    """
    from apysc._type import type_util
    is_bool: bool = type_util.is_bool(value=value)
    if is_bool:
        return
    raise ValueError(
        f'Specified value is not bool or Boolean type: {type(value)}')
