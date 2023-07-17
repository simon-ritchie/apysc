"""The left x geometry mix-in implementation for the `RectangleGeom`.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class RectangleGeomLeftXMixIn:
    _left_x: Number

    @property
    @add_debug_info_setting(module_name=__name__)
    def left_x(self) -> Number:
        """
        Get the rectangle left x coordinate.

        Returns
        -------
        left_x : Number
            The rectangle left x coordinate.
        """
        return self._left_x
