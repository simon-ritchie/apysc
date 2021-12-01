"""Base class implementation for the path data.
"""

from apysc._geom.path_label import PathLabel


class PathDataBase:
    """
    Base class for the path data.
    """

    _path_label: PathLabel
    _relative: bool

    def __init__(self, path_label: PathLabel, relative: bool) -> None:
        """
        Base class for the path data.

        Parameters
        ----------
        path_label : PathLabel
            Target (svg's) path label.
        relative : bool
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).
        """
        self._path_label = path_label
        self._relative = relative
