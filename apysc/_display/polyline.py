"""Implementations of Polyline class.
"""

import apysc as ap
from apysc._display.append_line_point_interface import AppendLinePointInterface
from apysc._display.line_base import LineBase
from apysc._geom.point2d import Point2D


class Polyline(LineBase, AppendLinePointInterface):
    """
    The polyline vector graphics class.

    References
    ----------
    - Graphics move_to and line_to interfaces document
        - https://bit.ly/3eybhEP
    """

    def __init__(
            self, parent: 'ap.Graphics', points: ap.Array[Point2D]) -> None:
        """
        Create a polyline vector graphic.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        points : Array of Point2D
            List of line points.

        References
        ----------
        - Graphics move_to and line_to interfaces document
            - https://bit.ly/3eybhEP
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Polyline):
            from apysc._display.graphics import Graphics
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            parent_graphics: Graphics = parent
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.POLYLINE)
            super(Polyline, self).__init__(
                parent=parent, x=0, y=0,
                variable_name=variable_name)
            self.points = points
            self._set_initial_basic_values(parent=parent)
            self._append_constructor_expression()
            self._set_line_setting_if_not_none_value_exists(
                parent_graphics=parent_graphics)
            self._set_overflow_visible_setting()

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

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=Polyline):
            from apysc._display.stage import get_stage_variable_name
            stage_variable_name: str = get_stage_variable_name()
            points_var_name: str
            points_expression: str
            points_var_name, points_expression = \
                self._make_2dim_points_expression()
            expression: str = (
                f'{points_expression}'
                f'\nvar {self.variable_name} = {stage_variable_name}'
                f'\n  .polyline({points_var_name})'
                '\n  .attr({'
            )
            expression = self._append_basic_vals_expression(
                expression=expression, indent_num=2)
            expression += '\n  });'
            ap.append_js_expression(expression=expression)
            self._points_var_name = points_var_name
