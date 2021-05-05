"""Implementations of Polyline class.
"""

from typing import Any
from typing import Union

from apysc import Array
from apysc import Int
from apysc import Number
from apysc import String
from apysc.display.fill_alpha_interface import FillAlphaInterface
from apysc.display.fill_color_interface import FillColorInterface
from apysc.display.graphic_base import GraphicBase
from apysc.display.line_alpha_interface import LineAlphaInterface
from apysc.display.line_color_interface import LineColorInterface
from apysc.display.line_thickness_interface import LineThicknessInterface
from apysc.display.points_2d_interface import Points2DInterface
from apysc.display.x_interface import XInterface
from apysc.display.y_interface import YInterface

_Graphics = Any


class Polyline(
        GraphicBase, FillColorInterface, FillAlphaInterface,
        LineColorInterface, LineAlphaInterface, LineThicknessInterface,
        Points2DInterface, XInterface, YInterface):

    def __init__(
            self, parent: _Graphics,
            points: Array,
            fill_color: Union[str, String] = '',
            fill_alpha: Union[float, Number] = 1.0,
            line_color: Union[str, String] = '',
            line_thickness: Union[int, Int] = 1,
            line_alpha: Union[float, Number] = 1.0) -> None:
        """
        Create a polyline vector graphic.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        points : Array of Point2D
            List of line points.
        fill_color : str or String, default ''
            Fill color (hexadecimal string, e.g., '#00aaff').
        fill_alpha : float or Number, default 1.0
            Fill opacity (0.0 to 1.0).
        line_color : str or String, default ''
            Line color (hexadecimal string, e.g., '#00aaff').
        line_thickness : int or Int, default 1
            Line thickness (width).
        line_alpha : float or Number, default 1.0
            Line opacity (0.0 to 1.0).
        """
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.POLYLINE)
        super(Polyline, self).__init__(
            parent=parent, x=0, y=0,
            variable_name=variable_name)
        self.points = points
        self._set_initial_fill_color_if_not_blank(fill_color=fill_color)
        self._update_fill_alpha_and_skip_appending_exp(value=fill_alpha)
        self._set_initial_line_color_if_not_blank(line_color=line_color)
        self._update_line_thickness_and_skip_appending_exp(
            value=line_thickness)
        self._update_line_alpha_and_skip_appending_exp(value=line_alpha)
        self._initialize_x_if_not_initialized()
        self._initialize_y_if_not_initialized()

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Polyline('<variable_name>')`).
        """
        repr_str: str = f"Polyline('{self.variable_name}')"
        return repr_str
