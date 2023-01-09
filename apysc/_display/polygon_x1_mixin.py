"""Class implementation for polygon-related classes' x1 mix-in.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._display.points_2d_mixin import Points2DMixIn


class PolygonX1MixIn(Points2DMixIn):

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
