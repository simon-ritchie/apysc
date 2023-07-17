"""The center x geometry mix-in implementation for the `RectangleGeom`.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class RectangleGeomCenterXMixIn:
    _center_x: Number

    @property
    @add_debug_info_setting(module_name=__name__)
    def center_x(self) -> Number:
        """
        Get the rectangle center x coordinate.

        Returns
        -------
        center_x : Number
            The rectangle center x coordinate.
        """
        return self._center_x
