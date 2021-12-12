"""Path data class implementation for the svg's `2D bezier curve` (Q).
"""

from typing import Union

from apysc._converter.to_apysc_val_from_builtin import \
    get_copied_int_from_builtin_val
from apysc._geom.path_control_x_interface import PathControlXInterface
from apysc._geom.path_control_y_interface import PathControlYInterface
from apysc._geom.path_data_base import PathDataBase
from apysc._geom.path_dest_x_interface import PathDestXInterface
from apysc._geom.path_dest_y_interface import PathDestYInterface
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.string import String


class PathBezier2D(
        PathDataBase, PathControlXInterface, PathControlYInterface,
        PathDestXInterface, PathDestYInterface):
    """
    Path data class for the svg's `2D bezier curve` (Q).
    """

    def __init__(
            self,
            control_x: Union[int, Int],
            control_y: Union[int, Int],
            dest_x: Union[int, Int],
            dest_y: Union[int, Int],
            *,
            relative: Union[bool, Boolean] = False) -> None:
        """
        Path data class for the svg's `2D bezier curve` (Q).

        Parameters
        ----------
        control_x : int or Int
            X-coordinate of the bezier's control point.
        control_y : int or Int
            Y-coordinate of the bezier's control point.
        dest_x : int or Int
            X-coordinate of the destination point.
        dest_y : int or Int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).
        """
        from apysc._geom.path_label import PathLabel
        super(PathBezier2D, self).__init__(
            path_label=PathLabel.BEZIER_2D,
            relative=relative)
        self._control_x = get_copied_int_from_builtin_val(integer=control_x)
        self._control_y = get_copied_int_from_builtin_val(integer=control_y)
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
        from apysc._type import value_util
        svg_char: String = self._get_svg_char()
        svg_char_str: str = value_util.get_value_str_for_expression(
            value=svg_char)
        control_x_str: str = value_util.get_value_str_for_expression(
            value=self._control_x)
        control_y_str: str = value_util.get_value_str_for_expression(
            value=self._control_y)
        dest_x_str: str = value_util.get_value_str_for_expression(
            value=self._dest_x)
        dest_y_str: str = value_util.get_value_str_for_expression(
            value=self._dest_y)
        svg_str: str = (
            f'{svg_char_str} + String({control_x_str}) + " " '
            f'+ String({control_y_str}) + " " '
            f'+ String({dest_x_str}) + " " '
            f'+ String({dest_y_str})'
        )
        return svg_str

    def update_path_data(
            self,
            control_x: Union[int, Int],
            control_y: Union[int, Int],
            dest_x: Union[int, Int],
            dest_y: Union[int, Int],
            relative: Union[bool, Boolean]) -> None:
        """
        Update the path's data settings.

        Parameters
        ----------
        control_x : int or Int
            X-coordinate of the bezier's control point.
        control_y : int or Int
            Y-coordinate of the bezier's control point.
        dest_x : int or Int
            X-coordinate of the destination point.
        dest_y : int or Int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).
        """
        self._control_x.value = control_x
        self._control_y.value = control_y
        self._dest_x.value = dest_x
        self._dest_y.value = dest_y
        self._relative.value = relative
