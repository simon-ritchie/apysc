"""Class implementation for the polygon-related classes' y2 mix-in.
"""

from apysc._display.polygon_apply_current_points_mixin import (
    PolygonApplyCurrentPointsMixIn,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class PolygonY2MixIn(PolygonApplyCurrentPointsMixIn):
    _y2: Number

    @property
    @add_debug_info_setting(module_name=__name__)
    def y2(self) -> Number:
        """
        Get a second y-coordinate.

        Returns
        -------
        y2 : Number
            A second y-coordinate.
        """
        y2: Number = self._points[1].y
        return y2

    @y2.setter
    @add_debug_info_setting(module_name=__name__)
    def y2(self, value: Number) -> None:
        """
        Set a second y-coordinate.

        Parameters
        ----------
        value : Number
            Y-coordinate to set.
        """
        from apysc._geom.point2d import Point2D

        self._y2._value = value._value
        new_point: Point2D = self._points[1]
        new_point.y = value
        self._points[1] = new_point
        self._apply_current_points()
