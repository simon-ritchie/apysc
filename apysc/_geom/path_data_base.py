"""Base class implementation for the path data.
"""

from abc import ABC
from abc import abstractmethod

from apysc._geom.path_label import PathLabel


class PathDataBase(ABC):
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

    def _get_svg_char(self) -> str:
        """
        Get a SVG character (e.g., 'M' or 'm') from the
        current setting.

        Returns
        -------
        svg_char : str
            Target SVG character.
        """
        svg_char: str = self._path_label.value
        if self._relative:
            svg_char = svg_char.lower()
        return svg_char

    @abstractmethod
    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.
        """
