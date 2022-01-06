"""Type related common implementations.

Mainly following interface is defined:

- is_number
    - Get a boolean value whether specified value is Number value.
- is_float_or_number
    - Get a boolean value whether specified value is float or Nuber
    value.
- is_bool
    - Get a boolean value whether specified value is bool or Boolean
    value.
- is_same_class_instance
    - Get a boolean value whether specified class and instance's class
    are same or not.
- is_immutable_type
    - Get a boolean value whether specified value is immutable
    type or not.
"""

from typing import Any
from typing import Tuple
from typing import Type


def is_number(*, value: Any) -> bool:
    """
    Get a boolean value whether specified value is Number value.

    Parameters
    ----------
    value : *
        Any value to check.

    Returns
    -------
    result : bool
        If Number value is specified, True will be returned.
    """
    import apysc as ap
    if isinstance(value, ap.Number):
        return True
    return False


def is_float_or_number(*, value: Any) -> bool:
    """
    Get a boolean value whether specified value is float or Nuber
    value.

    Parameters
    ----------
    value : *
        Any value to check.

    Returns
    -------
    result : bool
        If float or Number value is specified, True will be returned.
    """
    if isinstance(value, float):
        return True
    if is_number(value=value):
        return True
    return False


def is_bool(*, value: Any) -> bool:
    """
    Get a boolean value whether specified value is bool or Boolean
    value.

    Parameters
    ----------
    value : *
        Any value to check.

    Returns
    -------
    result : bool
        If bool or Boolean value is specified, True will be returned.
    """
    if is_same_class_instance(class_=bool, instance=value):
        return True
    import apysc as ap
    if isinstance(value, ap.Boolean):
        return True
    return False


def is_same_class_instance(*, class_: Type, instance: Any) -> bool:
    """
    Get a boolean value whether specified class and instance's class
    are same or not.

    Notes
    -----
    If instance is subclass of `cls` argument, differ from `isinstace`,
    then False will be returned.

    Parameters
    ----------
    class_ : Type
        Expected class.
    instance : *
        Intance to check it's class.

    Returns
    -------
    result : bool
        If a specified class and instance's class are same, then True
        will be set.
    """
    instance_type: Type = type(instance)  # type: ignore
    if instance_type == class_:
        return True
    return False


def is_immutable_type(value: Any) -> bool:
    """
    Get a boolean value whether specified value is immutable
    type or not.

    Notes
    -----
    apysc's value types, such as the `Int`, are checked
    as immutable since these js types are immutable.

    Parameters
    ----------
    value : Any
        Target value to check.

    Returns
    -------
    result : bool
        If a specified value is immutable, then True
        will be set.
    """
    import apysc as ap
    immutable_types: Tuple = (
        int, float, bool, str, complex, tuple, range, bytes,
        ap.Int, ap.Number, ap.String, ap.Boolean,
    )
    if isinstance(value, immutable_types):
        return True
    return False
