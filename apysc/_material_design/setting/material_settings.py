"""The static class implementation for the material design settings.
"""

from typing import Optional
from apysc._material_design.color.material_color_scheme import MaterialColorScheme
from apysc._type.boolean import Boolean


class MaterialSettings:

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
    def set_light_color_scheme(cls, *, color_scheme: Optional[MaterialColorScheme]) -> None:
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
    def set_dark_color_scheme(cls, *, color_scheme: Optional[MaterialColorScheme]) -> None:
        """
        Set a dark color scheme setting.

        Parameters
        ----------
        color_scheme : MaterialColorScheme or None
            Color scheme to set. If None is specified, the color scheme
            will be removed.
        """
        cls._dark_color_scheme = color_scheme

    _is_initialized_color_scheme_selection: Boolean

    @classmethod
    def _initialize_color_scheme_selection_bool_if_not_initialized(cls) -> None:
        """
        Initialize the color scheme selection boolean value
        if it is not initialized yet.
        """
        if hasattr(cls, "_is_initialized_color_scheme_selection"):
            return
        cls._is_initialized_color_scheme_selection = Boolean(
            False,
            variable_name_suffix="_is_initialized_color_scheme_selection",
        )

    @classmethod
    def _delete_initializing_bool_attrs(cls) -> None:
        """
        Delete the initializing boolean attributes from this class.
        """
        if hasattr(cls, "_is_initialized_color_scheme_selection"):
            del cls._is_initialized_color_scheme_selection
