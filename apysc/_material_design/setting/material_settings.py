"""The static class implementation for the material design settings.
"""

from typing import Optional

from apysc._material_design.color.material_brightness import MaterialBrightness
from apysc._material_design.color.material_color_scheme import MaterialColorScheme
from apysc._type.boolean import Boolean
from apysc._type.string import String


class MaterialSettings:

    @classmethod
    def _reset_settings(cls) -> None:
        """
        Reset all settings of this class.
        """
        cls._delete_current_brightness_string_attr()
        cls._light_color_scheme = None
        cls._dark_color_scheme = None
        if hasattr(cls, "_light_color_scheme_str"):
            del cls._light_color_scheme_str
        if hasattr(cls, "_dark_color_scheme_str"):
            del cls._dark_color_scheme_str

    _light_color_scheme: Optional[MaterialColorScheme] = None

    @classmethod
    def get_light_color_scheme(cls) -> Optional[MaterialColorScheme]:
        """
        Get a light color scheme setting.

        Returns
        -------
        color_scheme : MaterialColorScheme or None
            A light color scheme setting. If the color scheme is not set,
            this property becomes None.
        """
        return cls._light_color_scheme

    @classmethod
    def set_light_color_scheme(
        cls, *, color_scheme: Optional[MaterialColorScheme]
    ) -> None:
        """
        Set a color scheme setting.

        Parameters
        ----------
        color_scheme : MaterialColorScheme or None
            Color scheme to set. If None is specified, the color scheme
            will be removed.
        """
        cls._light_color_scheme = color_scheme

    _dark_color_scheme: Optional[MaterialColorScheme] = None

    @classmethod
    def get_dark_color_scheme(cls) -> Optional[MaterialColorScheme]:
        """
        Get a dark color scheme setting.

        Returns
        -------
        color_scheme : MaterialColorScheme or None
            A dark color scheme setting. If the color scheme is not set,
            this property becomes None.
        """
        return cls._dark_color_scheme

    @classmethod
    def set_dark_color_scheme(
        cls, *, color_scheme: Optional[MaterialColorScheme]
    ) -> None:
        """
        Set a dark color scheme setting.

        Parameters
        ----------
        color_scheme : MaterialColorScheme or None
            Color scheme to set. If None is specified, the color scheme
            will be removed.
        """
        cls._dark_color_scheme = color_scheme

    _current_brightness_string: String

    @classmethod
    def _initialize_current_brightness_string_if_not_initialized(cls) -> None:
        """
        Initialize the `_current_brightness_string` attribute string
        if it has not been initialized yet.
        """
        if hasattr(cls, "_current_brightness_string"):
            return
        cls._current_brightness_string = String(value=MaterialBrightness.LIGHT.value)

    @classmethod
    def _delete_current_brightness_string_attr(cls) -> None:
        """
        Delete the `_current_brightness_string` attribute.
        """
        if hasattr(cls, "_current_brightness_string"):
            del cls._current_brightness_string

    @classmethod
    def switch_to_light_color_scheme(cls) -> None:
        """
        Switch the current color scheme to the light color scheme.
        """
        cls._initialize_current_brightness_string_if_not_initialized()
        cls._current_brightness_string.value = MaterialBrightness.LIGHT.value

    @classmethod
    def switch_to_dark_color_scheme(cls) -> None:
        """
        Switch the current color scheme to the dark color scheme.
        """
        cls._initialize_current_brightness_string_if_not_initialized()
        cls._current_brightness_string.value = MaterialBrightness.DARK.value

    _light_color_scheme_str: String

    @classmethod
    def current_color_scheme_is_light_color_scheme(cls) -> Boolean:
        """
        Get whether the current color scheme is the light color scheme or not.

        Returns
        -------
        result : Boolean
            If the current color scheme is the light color scheme, then
            this method returns True.
        """
        cls._initialize_current_brightness_string_if_not_initialized()
        if not hasattr(cls, "_light_color_scheme_str"):
            cls._light_color_scheme_str = String(value=MaterialBrightness.LIGHT.value)
        return cls._current_brightness_string == cls._light_color_scheme_str

    _dark_color_scheme_str: String

    @classmethod
    def current_color_scheme_is_dark_color_scheme(cls) -> Boolean:
        """
        Get whether the current color scheme is the dark color scheme or not.

        Returns
        -------
        result : Boolean
            If the current color scheme is the dark color scheme, then
            this method returns True.
        """
        cls._initialize_current_brightness_string_if_not_initialized()
        if not hasattr(cls, "_dark_color_scheme_str"):
            cls._dark_color_scheme_str = String(value=MaterialBrightness.DARK.value)
        return cls._current_brightness_string == cls._dark_color_scheme_str
