"""Each types common value utilities.
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
