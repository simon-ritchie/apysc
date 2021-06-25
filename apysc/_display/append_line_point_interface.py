"""Class implementation for append line point interface.
"""

from typing import Union

from apysc import Int
from apysc._display.points_2d_interface import Points2DInterface


class AppendLinePointInterface(Points2DInterface):

    _points_var_name: str

    def append_line_point(
            self, x: Union[int, Int], y: Union[int, Int]) -> None:
        """
        Append line point at the end.

        Parameters
        ----------
        x : int or Int
            X-coordinate.
        y : int or Int
            Y-coordinate.
        """
        from apysc import Point2D
        from apysc import append_js_expression
        from apysc._type import value_util
        if not hasattr(self, '_points_var_name'):
            raise AttributeError(
                '_points_var_name attribute is not set. Please add '
                'implementation to set that value when constructor or else.')
        self.points.append(value=Point2D(x=x, y=y))
        expression: str
        x_name: str = value_util.get_value_str_for_expression(value=x)
        y_name: str = value_util.get_value_str_for_expression(value=y)
        expression = (
            f'{self._points_var_name}.push([{x_name}, {y_name}]);'
            f'\n{self.variable_name}.plot({self._points_var_name});'
        )
        append_js_expression(expression=expression)
