"""Class implementation for the `Polygon`-related classes'
`_append_constructor_expression` mix-in.
"""

from typing_extensions import final

from apysc._display.points_2d_mixin import Points2DMixIn
from apysc._display.points_var_name_mixin import PointsVarNameMixIn
from apysc._html.debug_mode import add_debug_info_setting


class PolygonAppendConstructorExpressionMixIn(Points2DMixIn, PointsVarNameMixIn):
    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a polygon's constructor expression.
        """
        import apysc as ap
        from apysc._display.graphics_base import GraphicsBase

        stage: ap.Stage = ap.get_stage()
        points_var_name: str
        points_expression: str
        points_var_name, points_expression = self._make_2dim_points_expression()
        expression: str = (
            f"{points_expression}"
            f"\nvar {self.variable_name} = {stage.variable_name}"
            f"\n  .polygon({points_var_name})"
            "\n  .attr({"
        )
        if isinstance(self, GraphicsBase):
            expression = self._append_basic_vals_expression(
                expression=expression, indent_num=2
            )
        expression += "\n  });"
        ap.append_js_expression(expression=expression)
        self._points_var_name = points_var_name
