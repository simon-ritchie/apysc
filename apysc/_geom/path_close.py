"""Path data class implementation for the svg's `close path` (Z).
"""

from apysc._geom.path_data_base import PathDataBase
from apysc._type.string import String


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
        svg_str: str = value_util.get_value_str_for_expression(
            value=svg_char)
        return svg_str
