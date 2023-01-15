"""Class implementation for the polygon-related classes' x3 mix-in.
"""

from apysc._display.polygon_apply_current_points_mixin import (
    PolygonApplyCurrentPointsMixIn,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class PolygonX3MixIn(PolygonApplyCurrentPointsMixIn):

    _x3: Int

    @property
    @add_debug_info_setting(module_name=__name__)
    def x3(self) -> Int:
        """
        Get a third x-coordinate.

        Returns
        -------
        x3 : Int
            A third x-coordinate.
        """
        x3: Int = self._points[2].x
        return x3

    @x3.setter
    @add_debug_info_setting(module_name=__name__)
    def x3(self, value: Int) -> None:
        """
        Set a third x-coordinate.

        Parameters
        ----------
        value : Int
            Y-coordinate to set.
        """
        import apysc as ap

        self._x3._value = value._value
        new_point: ap.Point2D = self._points[2]
        new_point.x = value
        self._points[2] = new_point
        self._apply_current_points()
