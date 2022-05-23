"""Class implementation for append line point interface.
"""

from typing import Union

from apysc._display.points_2d_interface import Points2DInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class AppendLinePointInterface(Points2DInterface):

    _points_var_name: str

    @arg_validation_decos.is_integer(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @add_debug_info_setting(
        module_name=__name__, class_name='AppendLinePointInterface')
    def append_line_point(
            self, *, x: Union[int, Int], y: Union[int, Int]) -> None:
        """
        Append line point at the end.

        Parameters
        ----------
        x : int or Int
            X-coordinate.
        y : int or Int
            Y-coordinate.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=0, y=0),
        ...         ap.Point2D(x=0, y=50),
        ...         ap.Point2D(x=50, y=50),
        ...     ])
        >>> polygon.append_line_point(x=50, y=0)
        """
        import apysc as ap
        from apysc._type import value_util
        if not hasattr(self, '_points_var_name'):
            raise AttributeError(
                '_points_var_name attribute is not set. Please add '
                'implementation to set that value when constructor '
                'or else.')
        self.points.append(value=ap.Point2D(x=x, y=y))
        expression: str
        x_name: str = value_util.get_value_str_for_expression(value=x)
        y_name: str = value_util.get_value_str_for_expression(value=y)
        expression = (
            f'{self._points_var_name}.push([{x_name}, {y_name}]);'
            f'\n{self.variable_name}.plot({self._points_var_name});'
        )
        ap.append_js_expression(expression=expression)
