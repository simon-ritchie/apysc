"""Path data class implementation for the svg's `vertical line` (V).
"""

from typing import Union

from apysc._geom.path_data_base import PathDataBase
from apysc._type.int import Int
from apysc._converter.to_apysc_val_from_builtin import \
    get_copied_int_from_builtin_val


class PathVertical(PathDataBase):
    """
    Path data class for the svg's `vertical line` (V).
    """

    _y: Int

    def __init__(
            self, y: Union[int, Int], relative: bool = False) -> None:
        """
        Path data class for the svg's `vertical line' (V).

        Parameters
        ----------
        y : int or Int
            Y-coordinate of the destination point.
        relative : bool, default False
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).
        """
        from apysc._geom.path_label import PathLabel
        super(PathVertical, self).__init__(
            path_label=PathLabel.VERTICAL,
            relative=relative)
        self._y = get_copied_int_from_builtin_val(integer=y)
