"""The center y geometry mix-in implementation for the `RectangleGeom`.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class RectangleGeomCenterYMixIn:
    _center_y: Number

    @property
    @add_debug_info_setting(module_name=__name__)
    def center_y(self) -> Number:
        """
        Get the rectangle center y coordinate.

        Returns
        -------
        center_y : Number
            The rectangle center y coordinate.
        """
        return self._center_y
