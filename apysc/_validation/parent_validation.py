"""Parent-related validation interfaces.
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
        If a specified parent isn't the `None` and
        `ChildInterface` instance.
    """
    if parent is None:
        return
    from apysc._display.child_interface import ChildInterface
    if isinstance(parent, ChildInterface):
        return
    raise ValueError(
        'Specified parent is not None and not `ChildInterface` instance,'
        f' like a Sprite: {type(parent)}')


def validate_parent_contains_child(
        parent: Optional[Any], child: Any) -> None:
    """
    Validate whether a parent contains a specified child.

    Parameters
    ----------
    parent : ChildInterface or None
        Parent instance.
    child : DisplayObject
        Child instance.

    Raises
    ------
    ValueError
        If a parent does not contain a specified child.
        If a parent is None, this interface skips the checking.
    """
    from apysc._display.child_interface import ChildInterface
    from apysc._display.display_object import DisplayObject
    parent_: Optional[ChildInterface] = parent
    child_: DisplayObject = child
    if parent_ is None:
        return
    if parent_.contains(child=child_):
        return
    raise ValueError(
        'Parent not containts specified child.'
        f'\nParent type: {type(parent_)}'
        f'\nChild type: {type(child_)}'
        f'\nChild name: {child_.variable_name}')
