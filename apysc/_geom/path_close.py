"""Path data class implementation for the svg's `close path` (Z).
"""

from apysc._geom.path_data_base import PathDataBase
from apysc._geom.path_label import PathLabel


class PathClose(PathDataBase):
    """
    Path data class for the svg's `close path` (Z).
    """

    def __init__(self) -> None:
        """
        Path data class for the svg's `close path` (Z).
        """
        super(PathClose, self).__init__(
            path_label=PathLabel.Close,
            relative=False)
