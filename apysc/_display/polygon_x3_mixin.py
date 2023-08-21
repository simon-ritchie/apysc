"""Class implementation for the polygon-related classes' x3 mix-in.
"""

from apysc._display.polygon_apply_current_points_mixin import (
    PolygonApplyCurrentPointsMixIn,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class PolygonX3MixIn(PolygonApplyCurrentPointsMixIn):
    _x3: Number

    @property
    @add_debug_info_setting(module_name=__name__)
    def x3(self) -> Number:
        """
        Get a third x-coordinate.

        Returns
        -------
        x3 : Number
            A third x-coordinate.
        """
        x3: Number = self._points[2].x
        return x3

    @x3.setter
    @add_debug_info_setting(module_name=__name__)
    def x3(self, value: Number) -> None:
        """
        Set a third x-coordinate.

        Parameters
        ----------
        value : Number
            Y-coordinate to set.
        """
        from apysc._geom.point2d import Point2D

        self._x3._value = value._value
        new_point: Point2D = self._points[2]
        new_point.x = value
        self._points[2] = new_point
        self._apply_current_points()
