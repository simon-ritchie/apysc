"""This module is for the SVG `continual 2D bezier
curve` (T) class implementation.
"""

from typing import Any
from typing import Union

from apysc._geom.path_data_base import PathDataBase
from apysc._geom.path_x_interface import PathXInterface
from apysc._geom.path_y_interface import PathYInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.string import String


class PathBezier2DContinual(PathDataBase, PathXInterface, PathYInterface):
    """
    Path data class for the SVG `continual 2D bezier curve` (T).

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color='#fff', thickness=3)
    >>> path: ap.Path = sprite.graphics.draw_path(
    ...     path_data_list=[
    ...         ap.PathMoveTo(x=0, y=50),
    ...         ap.PathBezier2D(
    ...             control_x=50, control_y=0,
    ...             dest_x=100, dest_y=50),
    ...         ap.PathBezier2DContinual(x=150, y=50),
    ...     ])
    """

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='PathBezier2DContinual')
    def __init__(
            self, x: Union[int, Int], y: Union[int, Int], *,
            relative: Union[bool, Boolean] = False) -> None:
        """
        Path data class for the SVG `continual 2D bezier curve` (T).

        Parameters
        ----------
        x : Int or int
            X-coordinate of the destination point.
        y : Int or int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            The boolean value indicates whether the path
            coordinates are relative or not (absolute).

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=3)
        >>> path: ap.Path = sprite.graphics.draw_path(
        ...     path_data_list=[
        ...         ap.PathMoveTo(x=0, y=50),
        ...         ap.PathBezier2D(
        ...             control_x=50, control_y=0,
        ...             dest_x=100, dest_y=50),
        ...         ap.PathBezier2DContinual(x=150, y=50),
        ...     ])
        """
        from apysc._converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        from apysc._geom.path_label import PathLabel
        super(PathBezier2DContinual, self).__init__(
            path_label=PathLabel.BEZIER_2D_CONTINUAL,
            relative=relative)
        self.x = get_copied_int_from_builtin_val(integer=x)
        self.y = get_copied_int_from_builtin_val(integer=y)

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='PathBezier2DContinual')
    def _get_svg_str(self) -> str:
        """
        Get an SVG path string created with the current setting.

        Returns
        -------
        svg_str : str
            An SVG path string was created with
            the current setting.
        """
        from apysc._type import value_util
        svg_char: String = self._get_svg_char()
        svg_char_str: str = value_util.get_value_str_for_expression(
            value=svg_char)
        x_str: str = value_util.get_value_str_for_expression(
            value=self._x)
        y_str: str = value_util.get_value_str_for_expression(
            value=self._y)
        svg_str: str = (
            f'{svg_char_str} + String({x_str}) + " " + String({y_str})')
        return svg_str

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='PathBezier2DContinual')
    def update_path_data(
            self, x: Union[int, Int], y: Union[int, Int],
            *,
            relative: Union[bool, Boolean] = False) -> None:
        """
        Update a path data settings.

        Parameters
        ----------
        x : Int or int
            X-coordinate of the destination point.
        y : Int or int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            A boolean value indicates whether the path
            coordinates are relative or not (absolute).

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_2d_continual = ap.PathBezier2DContinual(x=100, y=50)
        >>> bezier_2d_continual.update_path_data(x=150, y=100)
        >>> bezier_2d_continual.x
        Int(150)

        >>> bezier_2d_continual.y
        Int(100)
        """
        from apysc._converter.to_apysc_val_from_builtin import \
            get_copied_boolean_from_builtin_val
        from apysc._converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        self.x = get_copied_int_from_builtin_val(integer=x)
        self.y = get_copied_int_from_builtin_val(integer=y)
        self.relative = get_copied_boolean_from_builtin_val(
            bool_val=relative)

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='PathBezier2DContinual')
    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap
        if not isinstance(other, PathBezier2DContinual):
            result: ap.Boolean = ap.Boolean(False)
            return result
        return (
            self.x == other.x
            and self.y == other.y
            and self.relative == other.relative)

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='PathBezier2DContinual')
    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap
        result: ap.Boolean = self == other
        result = result.not_
        return result
