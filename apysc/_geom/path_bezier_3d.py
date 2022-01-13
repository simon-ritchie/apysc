"""Path data class implementation for the svg's `3D besier curve` (C).
"""

from typing import Union

from apysc._geom.path_control_x1_interface import PathControlX1Interface
from apysc._geom.path_control_x2_interface import PathControlX2Interface
from apysc._geom.path_control_y1_interface import PathControlY1Interface
from apysc._geom.path_control_y2_interface import PathControlY2Interface
from apysc._geom.path_data_base import PathDataBase
from apysc._geom.path_dest_x_interface import PathDestXInterface
from apysc._geom.path_dest_y_interface import PathDestYInterface
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.string import String


class PathBezier3D(
        PathDataBase, PathDestXInterface, PathDestYInterface,
        PathControlX1Interface, PathControlY1Interface,
        PathControlX2Interface, PathControlY2Interface):
    """
    Path data class for the svg's `3D bezier curve` (C).

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color='#fff', thickness=3)
    >>> path: ap.Path = sprite.graphics.draw_path(
    ...     path_data_list=[
    ...         ap.PathMoveTo(x=0, y=50),
    ...         ap.PathBezier3D(
    ...             control_x1=0, control_y1=0,
    ...             control_x2=50, control_y2=0,
    ...             dest_x=50, dest_y=50),
    ...         ap.PathBezier3DContinual(
    ...             control_x=100, control_y=100,
    ...             dest_x=100, dest_y=50),
    ...     ])
    """

    def __init__(
            self,
            control_x1: Union[int, Int],
            control_y1: Union[int, Int],
            control_x2: Union[int, Int],
            control_y2: Union[int, Int],
            dest_x: Union[int, Int],
            dest_y: Union[int, Int],
            *,
            relative: Union[bool, Boolean] = False) -> None:
        """
        Path data class for the svg's `3D bezier curve` (C).

        Parameters
        ----------
        control_x1 : int or Int
            X-coordinate of the bezier's first control point.
        control_y1 : int or Int
            Y-coordinate of the bezier's first control point.
        control_x2 : int or Int
            X-coordinate of the bezier's second control point.
        control_y2 : int or Int
            Y-coordinate of the bezier's second control point.
        dest_x : int or Int
            X-coordinate of the destination point.
        dest_y : int or Int
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
        ...         ap.PathBezier3D(
        ...             control_x1=0, control_y1=0,
        ...             control_x2=50, control_y2=0,
        ...             dest_x=50, dest_y=50),
        ...         ap.PathBezier3DContinual(
        ...             control_x=100, control_y=100,
        ...             dest_x=100, dest_y=50),
        ...     ])
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=PathBezier3D):
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_int_from_builtin_val
            from apysc._geom.path_label import PathLabel
            super(PathBezier3D, self).__init__(
                path_label=PathLabel.BEZIER_3D,
                relative=relative)
            self.control_x1 = get_copied_int_from_builtin_val(
                integer=control_x1)
            self.control_y1 = get_copied_int_from_builtin_val(
                integer=control_y1)
            self.control_x2 = get_copied_int_from_builtin_val(
                integer=control_x2)
            self.control_y2 = get_copied_int_from_builtin_val(
                integer=control_y2)
            self.dest_x = get_copied_int_from_builtin_val(integer=dest_x)
            self.dest_y = get_copied_int_from_builtin_val(integer=dest_y)

    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.

        Returns
        -------
        svg_str : str
            A path's SVG string created with the current setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._get_svg_str, locals_=locals(),
                module_name=__name__, class_=PathBezier3D):
            from apysc._type.value_util import get_value_str_for_expression
            svg_char: String = self._get_svg_char()
            svg_char_str: str = get_value_str_for_expression(
                value=svg_char)
            control_x1_str: str = get_value_str_for_expression(
                value=self._control_x1)
            control_y1_str: str = get_value_str_for_expression(
                value=self._control_y1)
            control_x2_str: str = get_value_str_for_expression(
                value=self._control_x2)
            control_y2_str: str = get_value_str_for_expression(
                value=self._control_y2)
            dest_x_str: str = get_value_str_for_expression(value=self._dest_x)
            dest_y_str: str = get_value_str_for_expression(value=self._dest_y)
            svg_str: str = (
                f'{svg_char_str} + String({control_x1_str}) '
                f'+ " " + String({control_y1_str}) '
                f'+ " " + String({control_x2_str}) '
                f'+ " " + String({control_y2_str}) '
                f'+ " " + String({dest_x_str}) '
                f'+ " " + String({dest_y_str})'
            )
            return svg_str

    def update_path_data(
            self,
            control_x1: Union[int, Int],
            control_y1: Union[int, Int],
            control_x2: Union[int, Int],
            control_y2: Union[int, Int],
            dest_x: Union[int, Int],
            dest_y: Union[int, Int],
            *,
            relative: Union[bool, Boolean] = False) -> None:
        """
        Update the path's data settings.

        Parameters
        ----------
        control_x1 : int or Int
            X-coordinate of the bezier's first control point.
        control_y1 : int or Int
            Y-coordinate of the bezier's first control point.
        control_x2 : int or Int
            X-coordinate of the bezier's second control point.
        control_y2 : int or Int
            Y-coordinate of the bezier's second control point.
        dest_x : int or Int
            X-coordinate of the destination point.
        dest_y : int or Int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_3d_continual = ap.PathBezier3D(
        ...     control_x1=0, control_y1=0,
        ...     control_x2=50, control_y2=0,
        ...     dest_x=50, dest_y=50)
        >>> bezier_3d_continual.update_path_data(
        ...     control_x1=100, control_y1=100,
        ...     control_x2=150, control_y2=100,
        ...     dest_x=150, dest_y=150)
        >>> bezier_3d_continual.control_x1
        Int(100)

        >>> bezier_3d_continual.control_y1
        Int(100)

        >>> bezier_3d_continual.control_x2
        Int(150)

        >>> bezier_3d_continual.control_y2
        Int(100)

        >>> bezier_3d_continual.dest_x
        Int(150)

        >>> bezier_3d_continual.dest_y
        Int(150)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.update_path_data, locals_=locals(),
                module_name=__name__, class_=PathBezier3D):
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_boolean_from_builtin_val
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_int_from_builtin_val
            self.control_x1 = get_copied_int_from_builtin_val(
                integer=control_x1)
            self.control_y1 = get_copied_int_from_builtin_val(
                integer=control_y1)
            self.control_x2 = get_copied_int_from_builtin_val(
                integer=control_x2)
            self.control_y2 = get_copied_int_from_builtin_val(
                integer=control_y2)
            self.dest_x = get_copied_int_from_builtin_val(integer=dest_x)
            self.dest_y = get_copied_int_from_builtin_val(integer=dest_y)
            self.relative = get_copied_boolean_from_builtin_val(
                bool_val=relative)
