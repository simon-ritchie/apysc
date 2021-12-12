"""Path data class implementation for the svg's `3D besier curve` (C).
"""

from typing import Union

from apysc._converter.to_apysc_val_from_builtin import \
    get_copied_int_from_builtin_val
from apysc._geom.path_data_base import PathDataBase
from apysc._geom.path_dest_x_interface import PathDestXInterface
from apysc._geom.path_dest_y_interface import PathDestYInterface
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.string import String


class PathBezier3D(PathDataBase, PathDestXInterface, PathDestYInterface):
    """
    Path data class for the svg's `3D bezier curve` (C).
    """

    _control_x1: Int
    _control_y1: Int
    _control_x2: Int
    _control_y2: Int

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
        """
        from apysc._geom.path_label import PathLabel
        super(PathBezier3D, self).__init__(
            path_label=PathLabel.BEZIER_3D,
            relative=relative)
        self._control_x1 = get_copied_int_from_builtin_val(integer=control_x1)
        self._control_y1 = get_copied_int_from_builtin_val(integer=control_y1)
        self._control_x2 = get_copied_int_from_builtin_val(integer=control_x2)
        self._control_y2 = get_copied_int_from_builtin_val(integer=control_y2)
        self._dest_x = get_copied_int_from_builtin_val(integer=dest_x)
        self._dest_y = get_copied_int_from_builtin_val(integer=dest_y)

    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.

        Returns
        -------
        svg_str : str
            A path's SVG string created with the current setting.
        """
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
            relative: Union[bool, Boolean]) -> None:
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
        """
        self._control_x1.value = control_x1
        self._control_y1.value = control_y1
        self._control_x2.value = control_x2
        self._control_y2.value = control_y2
        self._dest_x.value = dest_x
        self._dest_y.value = dest_y
        self._relative.value = relative
