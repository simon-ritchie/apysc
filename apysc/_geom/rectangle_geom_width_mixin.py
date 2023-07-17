"""The width geometry mix-in implementation for the `RectangleGeom`.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class RectangleGeomWidthMixIn:
    _width: Int

    @property
    @add_debug_info_setting(module_name=__name__)
    def width(self) -> Int:
        """
        Get the rectangle geometry width.

        Returns
        -------
        width : Int
            The rectangle geometry width.
        """
        return self._width
