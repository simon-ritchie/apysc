"""The right x geometry mix-in implementation for the `RectangleGeom`.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class RectangleGeomRightXMixIn:
    _right_x: Number

    @property
    @add_debug_info_setting(module_name=__name__)
    def right_x(self) -> Number:
        """
        Get the rectangle right x coordinate.

        Returns
        -------
        right_x : Number
            The rectangle right x coordinate.
        """
        return self._right_x
