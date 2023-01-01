"""Each types common value utilities.

Mainly following interfaces are defined:

- get_value_str_for_expression
    - Get a value string for expression.
- get_copy
    - Get a copy of a specified instance if it is an instance
    of CopyMixIn.
"""

from typing import Any
from typing import Dict
from typing import List
from typing import TypeVar
from typing import Union

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array


def get_value_str_for_expression(*, value: Any) -> str:
    """
    Get a value string for expression.

    Parameters
    ----------
    value : *
        Any value to convert to string.

    Returns
    -------
    value_str : str
        String for expression. If a value is an instance of
        VariableNameMixIn, this interface returns
        a variable's name. Otherwise, this interface returns
        a string-casted value. A bool value becomes lowercase
        (true or false), and this interface quotes a string
        value by double quotation. This interface converts
        a List or tuple value to a JavaScript Array expression,
        e.g., '[10, "Hello!", true, any_variable]'.
        None becomes NaN.
    """
    from apysc._type.expression_string import ExpressionString
    from apysc._type.variable_name_mixin import VariableNameMixIn

    if isinstance(value, ExpressionString):
        return value.value
    if isinstance(value, VariableNameMixIn):
        return value.variable_name
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, (list, tuple)):
        value_str: str = _get_value_str_from_iterable(value=value)
        return value_str
    if isinstance(value, dict):
        values_str = _get_value_str_from_dict(value=value)
        return values_str
    if value is None:
        return "null"
    return str(value)


def _get_value_str_from_dict(*, value: Dict[Any, Any]) -> str:
    """
    Get a value string from a dictionary object.

    Parameters
    ----------
    value : dict
        Dictionary object to convert to string.

    Returns
    -------
    value_str : str
        Converted string, e.g., '{"any_key": 10, "other_key": any_variable}'
    """
    value_str: str = "{"
    for key, value_ in value.items():
        if value_str != "{":
            value_str += ", "
        _validate_dict_key_type(key=key)
        value_str += f'"{key}": {get_value_str_for_expression(value=value_)}'
    value_str += "}"
    return value_str


def _validate_dict_key_type(*, key: Any) -> None:
    """
    Validate whether a dictionary key type is an int or str.

    Parameters
    ----------
    key : *
        Dictionary key to validate.

    Raises
    ------
    TypeError
        If a key-type isn't str or int.
    """
    if isinstance(key, (str, int, float)):
        return
    raise TypeError(f"Dictionary key type only supports str and int: {type(key)}")


def _get_value_str_from_iterable(*, value: Union[list, tuple, Array]) -> str:
    """
    Get a value string from an iterable object.

    Parameters
    ----------
    value : list or tuple or Array
        Target iterable object.

    Returns
    -------
    value_str : str
        Converted string, e.g., '[10, "Hello!", true, any_variable]'.
    """
    from apysc._type.variable_name_mixin import VariableNameMixIn

    if isinstance(value, Array):
        value_: List[Any] = value.value  # type: ignore
    else:
        value_ = list(value)  # type: ignore[arg-type]
    value_str: str = "["
    for unit_value in value_:
        if value_str != "[":
            value_str += ", "
        if isinstance(unit_value, VariableNameMixIn):
            value_str += f"{unit_value.variable_name}"
            continue
        value_str += get_value_str_for_expression(value=unit_value)
    value_str += "]"
    return value_str


_Type = TypeVar("_Type")


@add_debug_info_setting(module_name=__name__)
def get_copy(*, value: _Type) -> _Type:
    """
    Get a copy of a specified instance if it is an instance
    of CopyMixIn.

    Parameters
    ----------
    value : *
        Any value to copy.

    Returns
    -------
    copied : *
        Copied value. If a value is not an instance of
        CopyMixIn, this interface returns an argument
        value directly.
    """
    from apysc._type.copy_mixin import CopyMixIn

    if not isinstance(value, CopyMixIn):
        return value
    return value._copy()
