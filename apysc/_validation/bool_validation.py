"""Boolean value's validation implementations.
"""

from typing import Union

from apysc._type.boolean import Boolean


def validate_bool(
        *, value: Union[bool, Boolean],
        additional_err_msg: str = '') -> None:
    """
    Validate specified value is bool or Boolean type.

    Parameters
    ----------
    value : bool or Boolean
        Boolean value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If specified value isn't bool or Boolean type.
    """
    from apysc._type import type_util
    is_bool: bool = type_util.is_bool(value=value)
    if is_bool:
        return
    if additional_err_msg != '':
        additional_err_msg = f'\n{additional_err_msg}'
    raise ValueError(
        f'Specified value is not bool or Boolean type: {type(value)}'
        f'{additional_err_msg}')
