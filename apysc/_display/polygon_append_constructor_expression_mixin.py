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
        from apysc._display.append_fill_color_expression_mixin import (
            AppendFillColorAttrExpressionMixIn
        )
        from apysc._display.append_fill_alpha_attr_expression_mixin import (
            AppendFillAlphaAttrExpressionMixIn
        )
        from apysc._display.append_line_color_attr_expression_mixin import (
            AppendLineColorAttrExpressionMixIn
        )
        from apysc._display.append_line_thickness_attr_expression_mixin import (
            AppendLineThicknessAttrExpressionMixIn
        )
        from apysc._display.append_line_alpha_attr_expression_mixin import (
            AppendLineAlphaAttrExpressionMixIn
        )
        from apysc._display.append_line_cap_attr_expression_mixin import (
            AppendLineCapAttrExpressionMixIn
        )

        INDENT_NUM: int = 2
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
        if isinstance(self, AppendFillColorAttrExpressionMixIn):
            expression = self._append_fill_color_attr_expression(
                expression=expression, indent_num=INDENT_NUM
            )
        if isinstance(self, AppendFillAlphaAttrExpressionMixIn):
            expression = self._append_fill_alpha_attr_expression(
                expression=expression, indent_num=INDENT_NUM
            )
        if isinstance(self, AppendLineColorAttrExpressionMixIn):
            expression = self._append_line_color_attr_expression(
                expression=expression, indent_num=INDENT_NUM
            )
        if isinstance(self, AppendLineThicknessAttrExpressionMixIn):
            expression = self._append_line_thickness_attr_expression(
                expression=expression, indent_num=INDENT_NUM
            )
        if isinstance(self, AppendLineAlphaAttrExpressionMixIn):
            expression = self._append_line_alpha_attr_expression(
                expression=expression, indent_num=INDENT_NUM
            )
        if isinstance(self, AppendLineCapAttrExpressionMixIn):
            expression = self._append_line_cap_attr_expression(
                expression=expression, indent_num=INDENT_NUM
            )
        if isinstance(self, GraphicsBase):
            expression = self._append_basic_vals_expression(
                expression=expression, indent_num=INDENT_NUM
            )
        expression += "\n  });"
        ap.append_js_expression(expression=expression)
        self._points_var_name = points_var_name
