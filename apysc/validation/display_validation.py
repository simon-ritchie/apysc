"""Each display's validation implementations.
"""


from typing import Any


def validate_stage(stage: Any) -> None:
    """
    Validate whether the specified instance is Stage type or not.

    Parameters
    ----------
    stage : Stage
        Stage instance to check.

    Raises
    ------
    ValueError
        If specified instance is not stage type.
    """
    from apysc import Stage
    if isinstance(stage, Stage):
        return
    raise ValueError(
        f'Specified instance is not Stage type: {type(stage)}')


def validate_display_object(display_object: Any) -> None:
    """
    Validate specified instance is DisplayObject type or it's subclass
    type (e.g., Sprite).

    Parameters
    ----------
    display_object : DisplayObject
        DisplayObject instance to check.

    Raises
    ------
    ValueError
        If specified instance is not DisplayObject type or it's subclass
        type.
    """
    from apysc.display.display_object import DisplayObject
    if isinstance(display_object, DisplayObject):
        return
    raise ValueError(
        'Specified instance is not DisplayObject or it\'s subclass type: '
        f'{type(display_object)}')


def validate_sprite(sprite: Any) -> None:
    """
    Validate specified instance is Sprite type.

    Parameters
    ----------
    sprite : Sprite
        Sprite instance to check.

    Raises
    ------
    ValueError
        If specified instance is not Sprite type.
    """
    from apysc import Sprite
    if isinstance(sprite, Sprite):
        return
    raise ValueError(
        f'Specified instance is not Sprite type: {type(sprite)}')


def validate_graphics(graphics: Any) -> None:
    """
    Validate specified instance is Graphics type.

    Parameters
    ----------
    graphics : Graphics
        Graphics instance to check.

    Raises
    ------
    ValueError
        If specified instance is not Graphics type.
    """
    from apysc.display.graphics import Graphics
    if isinstance(graphics, Graphics):
        return
    raise ValueError(
        f'Specified instance is not Graphics type: {type(graphics)}')
