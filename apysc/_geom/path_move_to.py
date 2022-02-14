"""Path data class implementation for the svg's `move to` (M).
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


class PathMoveTo(PathDataBase, PathXInterface, PathYInterface):
    """
    Path data class for the svg's `move to` (M).

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color='#fff', thickness=3)
    >>> path: ap.Path = sprite.graphics.draw_path(
    ...     path_data_list=[
    ...         ap.PathMoveTo(x=0, y=50),
    ...         ap.PathLineTo(x=50, y=50),
    ...     ])
    """

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='PathMoveTo')
    def __init__(
            self, x: Union[int, Int], y: Union[int, Int], *,
            relative: Union[bool, Boolean] = False) -> None:
        """
        Path data class for the svg's `move to` (M).

        Parameters
        ----------
        x : int or Int
            X-coordinate of the destination point.
        y : int or Int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            The boolean value indicating whether the path
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
        ...         ap.PathLineTo(x=50, y=50),
        ...     ])
        """
        from apysc._converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        from apysc._geom.path_label import PathLabel
        super(PathMoveTo, self).__init__(
            path_label=PathLabel.MOVE_TO,
            relative=relative)
        self.x = get_copied_int_from_builtin_val(integer=x)
        self.y = get_copied_int_from_builtin_val(integer=y)

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='PathMoveTo')
    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.

        Returns
        -------
        svg_str : str
            A path's SVG string created with the current setting.
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
        module_name=__name__, class_name='PathMoveTo')
    def update_path_data(
            self, x: Union[int, Int], y: Union[int, Int],
            *,
            relative: Union[bool, Boolean] = False) -> None:
        """
        Update the path's data settings.

        Parameters
        ----------
        x : int or Int
            X-coordinate of the destination point.
        y : int or Int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).

        Examples
        --------
        >>> import apysc as ap
        >>> move_to: ap.PathMoveTo = ap.PathMoveTo(x=50, y=50)
        >>> move_to.update_path_data(x=100, y=150)
        >>> move_to.x
        Int(100)

        >>> move_to.y
        Int(150)
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
        module_name=__name__, class_name='PathMoveTo')
    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : Any
            Other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap
        if not isinstance(other, PathMoveTo):
            result: ap.Boolean = ap.Boolean(False)
            return result
        return (
            self.x == other.x
            and self.y == other.y
            and self.relative == other.relative)

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='PathMoveTo')
    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : Any
            Other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap
        result: ap.Boolean = self == other
        result = result.not_
        return result
