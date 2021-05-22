"""Implementations of Polygon class.
"""

from typing import Any
from typing import Union

from apysc import Array
from apysc import Int
from apysc.display.line_base import LineBase
from apysc.display.points_2d_interface import Points2DInterface
from apysc.geom.point2d import Point2D

_Graphics = Any


class Polygon(LineBase, Points2DInterface):

    _points_var_name: str

    def __init__(self, parent: _Graphics, points: Array[Point2D]) -> None:
        """
        Create a polygon vector graphic. This is similar to Polyline
        class, but unlike that, end point and start point will be
        connected.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        points : Array of Point2D
            List of polygon vertex points.
        """
        from apysc.display.graphics import Graphics
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        parent_graphics: Graphics = parent
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.POLYGON)
        super(Polygon, self).__init__(
            parent=parent, x=0, y=0, variable_name=variable_name)
        self.points = points
        self._set_initial_basic_values(parent=parent)
        self._set_line_setting_if_not_none_value_exists(
            parent_graphics=parent_graphics)

    def __repr__(self) -> str:
        pass
