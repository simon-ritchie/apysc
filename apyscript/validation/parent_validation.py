"""Parent related validation interfaces.
"""

from typing import Any
from typing import Optional


def validate_parent_instance(parent: Optional[Any]) -> None:
    """
    Validate specified parent is `ChildInterface` instance.

    Parameters
    ----------
    parent : *
        Any parent instance or None.

    Raises
    ------
    ValueError
        If specified parent is not None and not `ChildInterface`
        instance.
    """
    if parent is None:
        return
    from apyscript.display.child_interface import ChildInterface
    if isinstance(parent, ChildInterface):
        return
    raise ValueError(
        'Specified parent is not None and not `ChildInterface` instance,'
        f' like a Sprite: {type(parent)}')
