"""Class implementation for append line point mix-in.
"""

from typing import Union

from typing_extensions import final

from apysc._display.points_2d_mixin import Points2DMixIn
from apysc._display.set_x_and_y_with_minimum_point_interface_base import (
    SetXAndYWithMinimumPointInterfaceBase,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class AppendLinePointMixIn(Points2DMixIn, VariableNameSuffixMixIn):

    _points_var_name: str

    @final
    @arg_validation_decos.is_integer(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def append_line_point(self, *, x: Union[int, Int], y: Union[int, Int]) -> None:
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
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=0, y=0),
        ...         ap.Point2D(x=0, y=50),
        ...         ap.Point2D(x=50, y=50),
        ...     ]
        ... )
        >>> polygon.append_line_point(x=50, y=0)
        """
        import apysc as ap
        from apysc._type import value_util

        if not hasattr(self, "_points_var_name"):
            raise AttributeError(
                "_points_var_name attribute is not set. Please add "
                "implementation to set that value when constructor "
                "or else."
            )
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="points")
        point: ap.Point2D = ap.Point2D(x=x, y=y, variable_name_suffix=suffix)
        self.points.append(value=point)
        expression: str
        x_name: str = value_util.get_value_str_for_expression(value=x)
        y_name: str = value_util.get_value_str_for_expression(value=y)
        expression = (
            f"{self._points_var_name}.push([{x_name}, {y_name}]);"
            f"\n{self.variable_name}.plot({self._points_var_name});"
        )
        ap.append_js_expression(expression=expression)

        if isinstance(self, SetXAndYWithMinimumPointInterfaceBase):
            self._set_x_and_y_with_minimum_point()
