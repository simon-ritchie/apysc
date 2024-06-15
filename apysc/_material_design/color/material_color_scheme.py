"""The `MaterialColorScheme` class implementation.
"""


from apysc._color.color import Color
from typing import Optional


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
