"""The top y geometry mix-in implementation for the `RectangleGeom`.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class RectangleGeomTopYMixIn:
    _top_y: Number

    @property
    @add_debug_info_setting(module_name=__name__)
    def top_y(self) -> Number:
        """
        Get the rectangle top y coordinate.

        Returns
        -------
        top_y : Number
            The rectangle top y coordinate.
        """
        return self._top_y
