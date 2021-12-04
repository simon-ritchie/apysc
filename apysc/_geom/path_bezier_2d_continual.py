"""Path data class implementation for the svg's
`continual 2D bezier curve` (T).
"""

from typing import Union

from apysc._geom.path_data_base import PathDataBase
from apysc._type.int import Int
from apysc._converter.to_apysc_val_from_builtin import \
    get_copied_int_from_builtin_val


class PathBezier2DContinual(PathDataBase):
    """
    Path data class for the svg's `continual 2D bezier curve` (T).
    """

    _x: Int
    _y: Int

    def __init__(
            self, x: Union[int, Int], y: Union[int, Int],
            relative: bool = False) -> None:
        """
        Path data class for the svg's `continual 2D bezier curve` (T).

        Parameters
        ----------
        x : int or Int
            X-coordinate of the destination point.
        y : int or Int
            Y-coordinate of the destination point.
        relative : bool, default False
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).
        """
        from apysc._geom.path_label import PathLabel
        super(PathBezier2DContinual, self).__init__(
            path_label=PathLabel.BEZIER_2D_CONTINUAL,
            relative=relative)
        self._x = get_copied_int_from_builtin_val(integer=x)
        self._y = get_copied_int_from_builtin_val(integer=y)
