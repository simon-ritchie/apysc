"""Path data class implementation for the svg's `close path` (Z).
"""

from apysc._geom.path_data_base import PathDataBase


class PathClose(PathDataBase):
    """
    Path data class for the svg's `close path` (Z).
    """

    def __init__(self) -> None:
        """
        Path data class for the svg's `close path` (Z).
        """
        from apysc._geom.path_label import PathLabel
        super(PathClose, self).__init__(
            path_label=PathLabel.CLOSE,
            relative=False)
