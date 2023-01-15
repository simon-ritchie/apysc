"""Class implementation for the polygon-related classes' y1 mix-in.
"""

from apysc._display.polygon_apply_current_points_mixin import (
    PolygonApplyCurrentPointsMixIn,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class PolygonY1MixIn(PolygonApplyCurrentPointsMixIn):

    _y1: Int

    @property
    @add_debug_info_setting(module_name=__name__)
    def y1(self) -> Int:
        """
        Get a first y-coordinate.

        Returns
        -------
        y1 : Int
            A first y-coordinate.
        """
        y1: Int = self._points[0].y
        return y1

    @y1.setter
    @add_debug_info_setting(module_name=__name__)
    def y1(self, value: Int) -> None:
        """
        Set a first y-coordinate.

        Parameters
        ----------
        value : Int
            Y-coordinate to set.
        """
        import apysc as ap

        self._y1._value = value._value
        new_point: ap.Point2D = self._points[0]
        new_point.y = value
        self._points[0] = new_point
        self._apply_current_points()
