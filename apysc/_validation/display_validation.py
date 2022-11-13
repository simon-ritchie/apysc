"""Each display's validation implementations.

Mainly following interfaces are defined:

- validate_stage
    Validate whether the specified instance is Stage type or not.
- validate_display_object
    Validate whether a specified instance is the
    `DisplayObject` type or its subclass type (e.g., `Sprite`).
- validate_display_object_container
    Validate whether a specified instance is a container type
    of a `DisplayObject` instance (e.g., `Sprite`, `Stage`).
- validate_sprite
    Validate specified instance is Sprite type.
- validate_graphics
    Validate specified instance is Graphics type.
- validate_line_cap
    Validate specified line cap style setting.
- validate_line_joints
    Validate specified line joints style setting.
- validate_multiple_line_settings_are_not_set
    Validate that there are no multiple line settings
    (dotted, dashed, and so on).
"""


from typing import Any
from typing import List


def validate_stage(*, stage: Any) -> None:
    """
    Validate whether the specified instance is Stage type or not.

    Parameters
    ----------
    stage : Stage
        Stage instance to check.

    Raises
    ------
    ValueError
        If a specified instance is not stage type.
    """
    import apysc as ap

    if isinstance(stage, ap.Stage):
        return
    raise ValueError(f"Specified instance is not Stage type: {type(stage)}")


def validate_display_object(
    *, display_object: Any, additional_err_msg: str = ""
) -> None:
    """
    Validate whether a  specified instance is the
    `DisplayObject` type or its subclass type (e.g., Sprite).

    Parameters
    ----------
    display_object : DisplayObject
        A `DisplayObject` instance to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified instance is not `DisplayObject` type
        or its subclass type.
    """
    from apysc._display.display_object import DisplayObject

    if isinstance(display_object, DisplayObject):
        return
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    raise ValueError(
        "A specified instance is not DisplayObject or it's subclass type: "
        f"{type(display_object)}{additional_err_msg}"
    )


def validate_display_object_container(
    *, container_object: Any, additional_err_msg: str = ""
) -> None:
    """
    Validate whether a specified instance is a container type
    of a `DisplayObject` instance (e.g., `Sprite`, `Stage`).

    Parameters
    ----------
    container_object : Any
        A target container instance to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified instance is not a container type instance.
    """
    from apysc._display.child_mixin import ChildMixIn

    if isinstance(container_object, ChildMixIn):
        return
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    raise ValueError(
        "A specified instance is not a container type (e.g., "
        f"`Sprite`, `Stage`) instance: {type(container_object)}"
        f"{additional_err_msg}"
    )


def validate_sprite(*, sprite: Any) -> None:
    """
    Validate specified instance is Sprite type.

    Parameters
    ----------
    sprite : Sprite
        Sprite instance to check.

    Raises
    ------
    ValueError
        If a specified instance is not Sprite type.
    """
    import apysc as ap

    if isinstance(sprite, ap.Sprite):
        return
    raise ValueError(f"Specified instance is not Sprite type: {type(sprite)}")


def validate_graphics(*, graphics: Any) -> None:
    """
    Validate specified instance is Graphics type.

    Parameters
    ----------
    graphics : Graphics
        Graphics instance to check.

    Raises
    ------
    ValueError
        If a specified instance is not Graphics type.
    """
    from apysc._display.graphics import Graphics

    if isinstance(graphics, Graphics):
        return
    raise ValueError(f"Specified instance is not Graphics type: {type(graphics)}")


def validate_line_cap(*, cap: Any, additional_err_msg: str = "") -> None:
    """
    Validate specified line cap style setting.

    Parameters
    ----------
    cap : LineCaps or String
        Target line cap style setting to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified cap setting type is not LineCaps or not defined
        string value.
    """
    import apysc as ap

    if isinstance(cap, ap.LineCaps):
        return
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    if isinstance(cap, ap.String):
        for line_cap in ap.LineCaps:
            if line_cap.value == cap._value:
                return
        raise ValueError(
            f"Not defined cap string is specified: {cap}"
            "\nPlease see definitions of LineCaps."
            f"{additional_err_msg}"
        )
    raise ValueError(
        f"Specified cap style type is not LineCaps or String one: {type(cap)}"
        f"{additional_err_msg}"
    )


def validate_line_joints(*, joints: Any, additional_err_msg: str = "") -> None:
    """
    Validate specified line joints style setting.

    Parameters
    ----------
    joints : LineJoints or String
        Target line joints style setting to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If specified joints setting type is not LineJoints or not defined
        string value.
    """
    import apysc as ap

    if isinstance(joints, ap.LineJoints):
        return
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    if isinstance(joints, ap.String):
        for line_joints in ap.LineJoints:
            if line_joints.value == joints._value:
                return
        raise ValueError(
            f"Not defined joints string is specified: {joints}"
            f"\nPlease see definitions of LineJoints."
            f"\n{additional_err_msg}"
        )
    raise ValueError(
        "Specified joints type is not LineJoints or String one: "
        f"{type(joints)}"
        f"\n{additional_err_msg}"
    )


def validate_multiple_line_settings_are_not_set(
    *, any_instance: Any, additional_err_msg: str = ""
) -> None:
    """
    Validate that there are no multiple line settings
    (dotted, dashed, and so on).

    Parameters
    ----------
    any_instance : Any
        Any instance to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If there are multiple line settings.
    """
    from apysc._display.line_dash_dot_setting_mixin import LineDashDotSettingMixIn
    from apysc._display.line_dash_setting_mixin import LineDashSettingMixIn
    from apysc._display.line_dot_setting_mixin import LineDotSettingMixIn
    from apysc._display.line_round_dot_setting_mixin import LineRoundDotSettingMixIn
    from apysc._display.line_style_mixin import LineStyleMixIn

    valid_setting_names: List[str] = []
    if isinstance(any_instance, (LineStyleMixIn, LineDotSettingMixIn)):
        if (
            hasattr(any_instance, "_line_dot_setting")
            and any_instance._line_dot_setting is not None
        ):
            valid_setting_names.append("LineDotSetting")
    if isinstance(any_instance, (LineStyleMixIn, LineDashSettingMixIn)):
        if (
            hasattr(any_instance, "_line_dash_setting")
            and any_instance._line_dash_setting is not None
        ):
            valid_setting_names.append("LineDashSetting")
    if isinstance(any_instance, (LineStyleMixIn, LineRoundDotSettingMixIn)):
        if (
            hasattr(any_instance, "_line_round_dot_setting")
            and any_instance._line_round_dot_setting is not None
        ):
            valid_setting_names.append("LineRoundDotSetting")
    if isinstance(any_instance, (LineStyleMixIn, LineDashDotSettingMixIn)):
        if (
            hasattr(any_instance, "_line_dash_dot_setting")
            and any_instance._line_dash_dot_setting is not None
        ):
            valid_setting_names.append("LineDashDotSetting")
    if len(valid_setting_names) < 2:
        return
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    raise ValueError(
        "Multiple line settings can not be set."
        f" Current settings: {valid_setting_names}"
        f"{additional_err_msg}"
    )
