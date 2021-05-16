"""Implementations of Line class.
"""

from typing import Any

from apysc.display.line_base import LineBase

_Graphics = Any
_Point2D = Any


class Line(LineBase):

    _start_point: _Point2D
    _end_point: _Point2D

    def __init__(
            self, parent: _Graphics,
            start_point: _Point2D,
            end_point: _Point2D) -> None:
        """
        Create a line vector graphics.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        start_point : Points2D
            Line start point.
        end_point : Points2D
            Line end point.
        """
        from apysc.display.graphics import Graphics
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        parent_graphics: Graphics = parent
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.LINE)
        super(Line, self).__init__(
            parent=parent, x=0, y=0, variable_name=variable_name)
        self._start_point = start_point
        self._end_point = end_point
        self._set_initial_basic_values(parent=parent)
        self._set_line_setting_if_not_none_value_exists(
            parent_graphics=parent_graphics)

    def __repr__(self) -> str:
        pass
