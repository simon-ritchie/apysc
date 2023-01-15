"""Class implementation for the polygon-related classes' y3 mix-in.
"""

from apysc._display.polygon_apply_current_points_mixin import (
    PolygonApplyCurrentPointsMixIn,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class PolygonY3MixIn(PolygonApplyCurrentPointsMixIn):

    _y3: Int

    @property
    @add_debug_info_setting(module_name=__name__)
    def y3(self) -> Int:
        """
        Get a third y-coordinate.

        Returns
        -------
        y3 : Int
            A third y-coordinate.
        """
        y3: Int = self._points[2].y
        return y3

    @y3.setter
    def y3(self, value: Int) -> None:
        """
        Set a third y-coordinate.

        Parameters
        ----------
        value : Int
            Y-coordinate to set.
        """
        import apysc as ap

        self._y3._value = value._value
        new_point: ap.Point2D = self._points[2]
        new_point.y = value
        self._points[2] = new_point
        self._apply_current_points()
