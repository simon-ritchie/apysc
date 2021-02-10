"""Each display's validation implementations.
"""


def validate_stage(stage):
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
    from apyscript.display.stage import Stage
    if isinstance(stage, Stage):
        return
    raise ValueError(
        f'Specified instance is not Stage type: {type(stage)}')


def validate_display_object(display_object):
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
    from apyscript.display.display_object import DisplayObject
    if isinstance(display_object, DisplayObject):
        return
    raise ValueError(
        'Specified instance is not DisplayObject or it\'s subclass type: '
        f'{type(display_object)}')
