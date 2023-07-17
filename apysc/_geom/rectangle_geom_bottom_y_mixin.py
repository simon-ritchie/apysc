"""The bottom y geometry mix-in implementation for the `RectangleGeom`.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class RectangleGeomBottomYMixIn:
    _bottom_y: Number

    @property
    @add_debug_info_setting(module_name=__name__)
    def bottom_y(self) -> Number:
        """
        Get the rectangle bottom y coordinate.

        Returns
        -------
        bottom_y : Number
            The rectangle bottom y coordinate.
        """
        return self._bottom_y
