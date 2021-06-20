"""Each display's validation implementations.

Mainly following interfaces are defined:

- validate_stage
    Validate whether the specified instance is Stage type or not.
- validate_display_object
    Validate specified instance is DisplayObject type or it's
    subclass type (e.g., Sprite).
- validate_sprite
    Validate specified instance is Sprite type.
- validate_graphics
    Validate specified instance is Graphics type.
- validate_line_cap
    Validate specified line cap style setting.
- validate_line_joints
    Validate specified line joints style setting.
- validate_multiple_line_settings_isnt_set
    Validate multiple line settings (dotted, dashed, and so on)
    is not set.
"""


from typing import Any
from typing import List


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
    from apysc._display.display_object import DisplayObject
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
    from apysc._display.graphics import Graphics
    if isinstance(graphics, Graphics):
        return
    raise ValueError(
        f'Specified instance is not Graphics type: {type(graphics)}')


def validate_line_cap(cap: Any) -> None:
    """
    Validate specified line cap style setting.

    Parameters
    ----------
    cap : LineCaps or String
        Target line cap style setting to check.

    Raises
    ------
    ValueError
        If specified cap setting type is not LineCaps or not defined
        string value.
    """
    from apysc import LineCaps
    from apysc import String
    if isinstance(cap, LineCaps):
        return
    if isinstance(cap, String):
        for line_cap in LineCaps:
            if line_cap.value == cap:
                return
        raise ValueError(
            f'Not defined cap string is specified: {cap}'
            f'\nPlease see definitions of LineCaps.')
    raise ValueError(
        f'Specified cap style type is not LineCaps or String one: {type(cap)}'
    )


def validate_line_joints(joints: Any) -> None:
    """
    Validate specified line joints style setting.

    Parameters
    ----------
    joints : LineJoints or String
        Target line joints style setting to check.

    Raises
    ------
    ValueError
        If specified joints setting type is not LineJoints or not defined
        string value.
    """
    from apysc import LineJoints
    from apysc import String
    if isinstance(joints, LineJoints):
        return
    if isinstance(joints, String):
        for line_joints in LineJoints:
            if line_joints.value == joints:
                return
        raise ValueError(
            f'Not defined joints string is specified: {joints}'
            f'\nPlease see definitions of LineJoints.')
    raise ValueError(
        'Specified joints type is not LineJoints or String one: '
        f'{type(joints)}'
    )


def validate_multiple_line_settings_isnt_set(any_instance: Any) -> None:
    """
    Validate multiple line settings (dotted, dashed, and so on)
    is not set.

    Parameters
    ----------
    any_instance : Any
        Any instance to check.

    Raises
    ------
    ValueError
        If multiple line settings are set.
    """
    from apysc._display.line_dash_dot_setting_interface import \
        LineDashDotSettingInterface
    from apysc._display.line_dash_setting_interface import \
        LineDashSettingInterface
    from apysc._display.line_dot_setting_interface import \
        LineDotSettingInterface
    from apysc._display.line_round_dot_setting_interface import \
        LineRoundDotSettingInterface
    from apysc._display.line_style_interface import LineStyleInterface
    valid_setting_names: List[str] = []
    if isinstance(
            any_instance, (LineStyleInterface, LineDotSettingInterface)):
        if (hasattr(any_instance, '_line_dot_setting')
                and any_instance._line_dot_setting is not None):
            valid_setting_names.append('LineDotSetting')
    if isinstance(
            any_instance, (LineStyleInterface, LineDashSettingInterface)):
        if (hasattr(any_instance, '_line_dash_setting')
                and any_instance._line_dash_setting is not None):
            valid_setting_names.append('LineDashSetting')
    if isinstance(
            any_instance, (LineStyleInterface, LineRoundDotSettingInterface)):
        if (hasattr(any_instance, '_line_round_dot_setting')
                and any_instance._line_round_dot_setting is not None):
            valid_setting_names.append('LineRoundDotSetting')
    if isinstance(
            any_instance, (LineStyleInterface, LineDashDotSettingInterface)):
        if (hasattr(any_instance, '_line_dash_dot_setting')
                and any_instance._line_dash_dot_setting is not None):
            valid_setting_names.append('LineDashDotSetting')
    if len(valid_setting_names) < 2:
        return
    raise ValueError(
        'Multiple line settings can not be set.'
        f' Current settings: {valid_setting_names}')
