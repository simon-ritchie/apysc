"""The height geometry mix-in implementation for the `RectangleGeom`.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class RectangleGeomHeightMixIn:
    _height: Int

    @property
    @add_debug_info_setting(module_name=__name__)
    def height(self) -> Int:
        """
        Get the rectangle geometry height.

        Returns
        -------
        height : Int
            The rectangle geometry height.
        """
        return self._height
