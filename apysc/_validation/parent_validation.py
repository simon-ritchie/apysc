"""Parent-related validation interfaces.
"""

from typing import Any
from typing import Optional


def validate_parent_contains_child(*, parent: Optional[Any], child: Any) -> None:
    """
    Validate whether a parent contains a specified child.

    Parameters
    ----------
    parent : ChildMixIn or None
        Parent instance.
    child : DisplayObject
        Child instance.

    Raises
    ------
    ValueError
        If a parent does not contain a specified child.
        If a parent is None, this interface skips the checking.
    """
    from apysc._display.child_mixin import ChildMixIn
    from apysc._display.display_object import DisplayObject

    parent_: Optional[ChildMixIn] = parent
    child_: DisplayObject = child
    if parent_ is None:
        return
    if parent_.contains(child=child_):
        return
    raise ValueError(
        "Parent not containts specified child."
        f"\nParent type: {type(parent_)}"
        f"\nChild type: {type(child_)}"
        f"\nChild name: {child_.variable_name}"
    )
