"""Class implementation for the polygon-related classes' x2 mix-in.
"""

from apysc._display.polygon_apply_current_points_mixin import (
    PolygonApplyCurrentPointsMixIn,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class PolygonX2MixIn(PolygonApplyCurrentPointsMixIn):

    _x2: Number

    @property
    @add_debug_info_setting(module_name=__name__)
    def x2(self) -> Number:
        """
        Get a second x-coordinate.

        Returns
        -------
        x2 : Number
            A second x-coordinate.
        """
        x2: Number = self._points[1].x
        return x2

    @x2.setter
    @add_debug_info_setting(module_name=__name__)
    def x2(self, value: Number) -> None:
        """
        Set a second x-coordinate.

        Parameters
        ----------
        value : Number
            X-coordinate to set.
        """
        import apysc as ap

        self._x2._value = value._value
        new_point: ap.Point2D = self._points[1]
        new_point.x = value
        self._points[1] = new_point
        self._apply_current_points()
