"""Class implementation for polygon-related classes' x1 mix-in.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._display.points_2d_mixin import Points2DMixIn
from apysc._display.polygon_apply_current_points_mixin import PolygonApplyCurrentPointsMixIn


class PolygonX1MixIn(Points2DMixIn, PolygonApplyCurrentPointsMixIn):

    _x1: Int

    @property
    @add_debug_info_setting(module_name=__name__)
    def x1(self) -> Int:
        """
        Get a first x-coordinate.

        Returns
        -------
        x1 : Int
            A first x-coordinate.
        """
        x1: Int = self._points[0].x
        return x1

    @x1.setter
    @add_debug_info_setting(module_name=__name__)
    def x1(self, value: Int) -> None:
        """
        Set a first x-coordinate.

        Parameters
        ----------
        value : Int
            X-coordinate to set.
        """
        self._x1._value = value._value
        self._points[0].x.value = value._copy()
        self._apply_current_points()
