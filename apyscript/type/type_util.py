"""Type related common implementations.

Mainly following interface is defined:

- is_same_class_instance
    Get a boolean value whether specified class and instance's class
    are same or not.
"""

from typing import Any
from typing import Type


def is_same_class_instance(class_: Type, instance: Any) -> bool:
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
    instance_type: Type = type(instance)
    if instance_type == class_:
        return True
    return False
