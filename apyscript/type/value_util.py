"""Each types common value utilities.

Mainly following interfaces are defined:

- get_value_str_for_expression
    Get a value string for expression.
- get_copy
    Get a copy of specified instance if it is instance of CopyInterface.
"""

from typing import Any


def get_value_str_for_expression(value: Any) -> str:
    """
    Get a value string for expression.

    Parameters
    ----------
    value : *
        Any value to convert to string.

    Returns
    -------
    value_str : str
        String for expression. If value is instance of
        VariableNameInterface, then variable's name will be returned,
        otherwise string casted value will be returned.
    """
    from apyscript.type.variable_name_interface import VariableNameInterface
    if isinstance(value, VariableNameInterface):
        return value.variable_name
    return str(value)


def get_copy(value: Any) -> Any:
    """
    Get a copy of specified instance if it is instance of CopyInterface.

    Parameters
    ----------
    value : *
        Any value to copy.

    Returns
    -------
    copied : *
        Copied value. If value is not instance of CopyInterface,
        then argument value will be returned directly.
    """
    from apyscript.type.copy_interface import CopyInterface
    if not isinstance(value, CopyInterface):
        return value
    return value._copy()
