"""The `MaterialColorScheme` class implementation.
"""

from typing import Optional

from apysc._color.color import Color
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class MaterialColorScheme:
    """
    The color scheme class for the material design.

    Notes
    -----
    The apysc library refers to the Flutter's ColorScheme class.

    References
    ----------
    - ColorScheme class (Flutter)
        - https://api.flutter.dev/flutter/material/ColorScheme-class.html
    - Flutter license (BSD 3-Clause "New" or "Revised" License)
        - https://github.com/flutter/flutter/blob/master/LICENSE
    """

    _primary: Color
    _on_primary: Color
    _secondary: Color
    _on_secondary: Color
    _error: Color
    _on_error: Color
    _surface: Color
    _on_surface: Color
    _primary_container: Optional[Color] = None
    _on_primary_container: Optional[Color] = None
    _secondary_container: Optional[Color] = None
    _on_secondary_container: Optional[Color] = None
    _tertiary: Optional[Color] = None
    _on_tertiary: Optional[Color] = None
    _tertiary_container: Optional[Color] = None
    _on_tertiary_container: Optional[Color] = None
    _error_container: Optional[Color] = None
    _on_error_container: Optional[Color] = None
    _outline: Optional[Color] = None
    _outline_variant: Optional[Color] = None

    # primary
    @arg_validation_decos.is_color(arg_position_index=1, optional=False)
    # on_primary
    @arg_validation_decos.is_color(arg_position_index=2, optional=False)
    # secondary
    @arg_validation_decos.is_color(arg_position_index=3, optional=False)
    # on_secondary
    @arg_validation_decos.is_color(arg_position_index=4, optional=False)
    # error
    @arg_validation_decos.is_color(arg_position_index=5, optional=False)
    # on_error
    @arg_validation_decos.is_color(arg_position_index=6, optional=False)
    # surface
    @arg_validation_decos.is_color(arg_position_index=7, optional=False)
    # on_surface
    @arg_validation_decos.is_color(arg_position_index=8, optional=False)
    # primary_container
    @arg_validation_decos.is_color(arg_position_index=9, optional=True)
    # on_primary_container
    @arg_validation_decos.is_color(arg_position_index=10, optional=True)
    # secondary_container
    @arg_validation_decos.is_color(arg_position_index=11, optional=True)
    # on_secondary_container
    @arg_validation_decos.is_color(arg_position_index=12, optional=True)
    # tertiary
    @arg_validation_decos.is_color(arg_position_index=13, optional=True)
    # on_tertiary
    @arg_validation_decos.is_color(arg_position_index=14, optional=True)
    # tertiary_container
    @arg_validation_decos.is_color(arg_position_index=15, optional=True)
    # on_tertiary_container
    @arg_validation_decos.is_color(arg_position_index=16, optional=True)
    # error_container
    @arg_validation_decos.is_color(arg_position_index=17, optional=True)
    # on_error_container
    @arg_validation_decos.is_color(arg_position_index=18, optional=True)
    # outline
    @arg_validation_decos.is_color(arg_position_index=19, optional=True)
    # outline_variant
    @arg_validation_decos.is_color(arg_position_index=20, optional=True)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        primary: Color,
        on_primary: Color,
        secondary: Color,
        on_secondary: Color,
        error: Color,
        on_error: Color,
        surface: Color,
        on_surface: Color,
        primary_container: Optional[Color] = None,
        on_primary_container: Optional[Color] = None,
        secondary_container: Optional[Color] = None,
        on_secondary_container: Optional[Color] = None,
        tertiary: Optional[Color] = None,
        on_tertiary: Optional[Color] = None,
        tertiary_container: Optional[Color] = None,
        on_tertiary_container: Optional[Color] = None,
        error_container: Optional[Color] = None,
        on_error_container: Optional[Color] = None,
        outline: Optional[Color] = None,
        outline_variant: Optional[Color] = None,
    ) -> None:
        """
        The color scheme class for the material design.

        Parameters
        ----------
        primary : Color
            The main color displayed most frequently.
        on_primary : Color
            A color to use on a primary color widget.
        secondary : Color
            An accent color used for less prominent widgets than the primary color.
        on_secondary : Color
            A color to use on a secondary color widget.
        error : Color
            A color to use for input validation errors.
        on_error : Color
            A color to use on an error color widget.
        surface : Color
            The background color for widgets like the material design's card.
        on_surface : Color
            A color to use on a surface color widget.
        primary_container : Optional[Color], optional
            A color to use on a primary color container widget or
            when you want to use this in a less prominent way
            than the primary color.
        on_primary_container : Optional[Color], optional
            A color to use on a primary_container color widget.
        secondary_container : Optional[Color], optional
            A color to use on a secondary color container widget or
            when you want to use this in a less prominent way
            than the secondary color.
        on_secondary_container : Optional[Color], optional
            A color to use on a secondary_container color widget.
        tertiary : Optional[Color], optional
            An accent color following the primary and secondary colors.
        on_tertiary : Optional[Color], optional
            A color to use on a tertiary color widget.
        tertiary_container : Optional[Color], optional
            A color to use on a tertiary color container widget or
            when you want to use this in a less prominent way
            than the tertiary color.
        on_tertiary_container : Optional[Color], optional
            A color to use on a tertiary_container color widget.
        error_container : Optional[Color], optional
            A color to use on an error color container widget or
            when you want to use this in a less prominent way
            than the error color.
        on_error_container : Optional[Color], optional
            A color to use on an error_container color widget.
        outline : Optional[Color], optional
            A widget outline color.
        outline_variant : Optional[Color], optional
            A color for an widget's outline that is less prominent than
            the outline color.

        Notes
        -----
        The apysc library refers to the Flutter's ColorScheme class.

        References
        ----------
        - ColorScheme class (Flutter)
            - https://api.flutter.dev/flutter/material/ColorScheme-class.html
        - Flutter license (BSD 3-Clause "New" or "Revised" License)
            - https://github.com/flutter/flutter/blob/master/LICENSE
        """
        self._primary = primary._copy()
        self._on_primary = on_primary._copy()
        self._secondary = secondary._copy()
        self._on_secondary = on_secondary._copy()
        self._error = error._copy()
        self._on_error = on_error._copy()
        self._surface = surface._copy()
        self._on_surface = on_surface._copy()
        if primary_container is not None:
            self._primary_container = primary_container._copy()
        if on_primary_container is not None:
            self._on_primary_container = on_primary_container._copy()
        if secondary_container is not None:
            self._secondary_container = secondary_container._copy()
        if on_secondary_container is not None:
            self._on_secondary_container = on_secondary_container._copy()
        if tertiary is not None:
            self._tertiary = tertiary._copy()
        if on_tertiary is not None:
            self._on_tertiary = on_tertiary._copy()
        if tertiary_container is not None:
            self._tertiary_container = tertiary_container._copy()
        if on_tertiary_container is not None:
            self._on_tertiary_container = on_tertiary_container._copy()
        if error_container is not None:
            self._error_container = error_container._copy()
        if on_error_container is not None:
            self._on_error_container = on_error_container._copy()
        if outline is not None:
            self._outline = outline._copy()
        if outline_variant is not None:
            self._outline_variant = outline_variant._copy()

    @property
    def primary(self) -> Color:
        """
        Get the `primary` color.

        Returns
        -------
        primary : Color
            The main color displayed most frequently.
        """
        return self._primary._copy()

    @property
    def on_primary(self) -> Color:
        """
        Get the `on_primary` color.

        Returns
        -------
        on_primary : Color
            A color to use on a primary color widget.
        """
        return self._on_primary._copy()

    @property
    def secondary(self) -> Color:
        """
        Get the `secondary` color.

        Returns
        -------
        secondary : Color
            An accent color used for less prominent widgets than the primary color.
        """
        return self._secondary._copy()

    @property
    def on_secondary(self) -> Color:
        """
        Get the `on_secondary` color.

        Returns
        -------
        on_secondary : Color
            A color to use on a secondary color widget.
        """
        return self._on_secondary._copy()

    @property
    def error(self) -> Color:
        """
        Get the `error` color.

        Returns
        -------
        error : Color
            A color to use for input validation errors.
        """
        return self._error._copy()

    @property
    def on_error(self) -> Color:
        """
        Get the `on_error` color.

        Returns
        -------
        on_error : Color
            A color to use on an error color widget.
        """
        return self._on_error._copy()

    @property
    def surface(self) -> Color:
        """
        Get the `surface` color.

        Returns
        -------
        surface : Color
            The background color for widgets like the material design's card.
        """
        return self._surface._copy()

    @property
    def on_surface(self) -> Color:
        """
        Get the `on_surface` color.

        Returns
        -------
        on_surface : Color
            A color to use on a surface color widget.
        """
        return self._on_surface._copy()

    @property
    def primary_container(self) -> Optional[Color]:
        """
        Get the `primary_container` color.

        Returns
        -------
        primary_container : Optional[Color]
            A color to use on a primary color container widget or
            when you want to use this in a less prominent way
            than the primary color.
        """
        if self._primary_container is None:
            return None
        return self._primary_container._copy()

    @property
    def on_primary_container(self) -> Optional[Color]:
        """
        Get the `on_primary_container` color.

        Returns
        -------
        on_primary_container : Optional[Color]
            A color to use on a primary_container color widget.
        """
        if self._on_primary_container is None:
            return None
        return self._on_primary_container._copy()

    @property
    def secondary_container(self) -> Optional[Color]:
        """
        Get the `secondary_container` color.

        Returns
        -------
        secondary_container : Optional[Color]
            A color to use on a secondary color container widget or
            when you want to use this in a less prominent way
            than the secondary color.
        """
        if self._secondary_container is None:
            return None
        return self._secondary_container._copy()

    @property
    def on_secondary_container(self) -> Optional[Color]:
        """
        Get the `on_secondary_container` color.

        Returns
        -------
        on_secondary_container : Optional[Color]
            A color to use on a secondary_container color widget.
        """
        if self._on_secondary_container is None:
            return None
        return self._on_secondary_container._copy()

    @property
    def tertiary(self) -> Optional[Color]:
        """
        Get the `tertiary` color.

        Returns
        -------
        tertiary : Optional[Color]
            An accent color following the primary and secondary colors.
        """
        if self._tertiary is None:
            return None
        return self._tertiary._copy()

    @property
    def on_tertiary(self) -> Optional[Color]:
        """
        Get the `on_tertiary` color.

        Returns
        -------
        on_tertiary : Optional[Color]
            A color to use on a tertiary color widget.
        """
        if self._on_tertiary is None:
            return None
        return self._on_tertiary._copy()

    @property
    def tertiary_container(self) -> Optional[Color]:
        """
        Get the `tertiary_container` color.

        Returns
        -------
        tertiary_container : Optional[Color]
            A color to use on a tertiary color container widget or
            when you want to use this in a less prominent way
            than the tertiary color.
        """
        if self._tertiary_container is None:
            return None
        return self._tertiary_container._copy()

    @property
    def on_tertiary_container(self) -> Optional[Color]:
        """
        Get the `on_tertiary_container` color.

        Returns
        -------
        on_tertiary_container : Optional[Color]
            A color to use on a tertiary_container color widget.
        """
        if self._on_tertiary_container is None:
            return None
        return self._on_tertiary_container._copy()

    @property
    def error_container(self) -> Optional[Color]:
        """
        Get the `error_container` color.

        Returns
        -------
        error_container : Optional[Color]
            A color to use on an error color container widget or
            when you want to use this in a less prominent way
            than the error color.
        """
        if self._error_container is None:
            return None
        return self._error_container._copy()

    @property
    def on_error_container(self) -> Optional[Color]:
        """
        Get the `on_error_container` color.

        Returns
        -------
        on_error_container : Optional[Color]
            A color to use on an error_container color widget.
        """
        if self._on_error_container is None:
            return None
        return self._on_error_container._copy()

    @property
    def outline(self) -> Optional[Color]:
        """
        Get the `outline` color.

        Returns
        -------
        outline : Optional[Color]
            A widget outline color.
        """
        if self._outline is None:
            return None
        return self._outline._copy()

    @property
    def outline_variant(self) -> Optional[Color]:
        """
        Get the `outline_variant` color.

        Returns
        -------
        outline_variant : Optional[Color]
            A color for an widget's outline that is less prominent than
            the outline color.
        """
        if self._outline_variant is None:
            return None
        return self._outline_variant._copy()
