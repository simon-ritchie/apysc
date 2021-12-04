"""Path data class implementation for the svg's `2D bezier curve` (Q).
"""

from typing import Union

from apysc._geom.path_data_base import PathDataBase
from apysc._type.int import Int
from apysc._converter.to_apysc_val_from_builtin import \
    get_copied_int_from_builtin_val


class PathBezier2D(PathDataBase):
    """
    Path data class for the svg's `2D bezier curve` (Q).
    """

    _control_x: Int
    _control_y: Int
    _dest_x: Int
    _dest_y: Int

    def __init__(
            self,
            control_x: Union[int, Int],
            control_y: Union[int, Int],
            dest_x: Union[int, Int],
            dest_y: Union[int, Int],
            relative: bool = False) -> None:
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
        relative : bool, default False
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
