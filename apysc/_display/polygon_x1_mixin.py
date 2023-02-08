"""Class implementation for the polygon-related classes' x1 mix-in.
"""

from apysc._display.polygon_apply_current_points_mixin import (
    PolygonApplyCurrentPointsMixIn,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class PolygonX1MixIn(PolygonApplyCurrentPointsMixIn):

    _x1: Number

    @property
    @add_debug_info_setting(module_name=__name__)
    def x1(self) -> Number:
        """
        Get a first x-coordinate.

        Returns
        -------
        x1 : Number
            A first x-coordinate.
        """
        x1: Number = self._points[0].x
        return x1

    @x1.setter
    @add_debug_info_setting(module_name=__name__)
    def x1(self, value: Number) -> None:
        """
        Set a first x-coordinate.

        Parameters
        ----------
        value : Number
            X-coordinate to set.
        """
        import apysc as ap

        self._x1._value = value._value
        new_point: ap.Point2D = self._points[0]
        new_point.x = value
        self._points[0] = new_point
        self._apply_current_points()
