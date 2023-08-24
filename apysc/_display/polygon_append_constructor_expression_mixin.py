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
        from apysc._display.append_fill_alpha_attr_expression_mixin import (
            AppendFillAlphaAttrExpressionMixIn,
        )
        from apysc._display.append_fill_color_expression_mixin import (
            AppendFillColorAttrExpressionMixIn,
        )
        from apysc._display.append_line_alpha_attr_expression_mixin import (
            AppendLineAlphaAttrExpressionMixIn,
        )
        from apysc._display.append_line_cap_attr_expression_mixin import (
            AppendLineCapAttrExpressionMixIn,
        )
        from apysc._display.append_line_color_attr_expression_mixin import (
            AppendLineColorAttrExpressionMixIn,
        )
        from apysc._display.append_line_joints_attr_expression_mixin import (
            AppendLineJointsAttrExpressionMixIn,
        )
        from apysc._display.append_line_thickness_attr_expression_mixin import (
            AppendLineThicknessAttrExpressionMixIn,
        )
        from apysc._display.append_x_attr_expression_mixin import (
            AppendXAttrExpressionMixIn,
        )
        from apysc._display.append_y_attr_expression_mixin import (
            AppendYAttrExpressionMixIn,
        )
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._expression import expression_data_util

        INDENT_NUM: int = 2
        stage: Stage = get_stage()
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
        if isinstance(self, AppendLineJointsAttrExpressionMixIn):
            expression = self._append_line_joints_attr_expression(
                expression=expression, indent_num=INDENT_NUM
            )
        if isinstance(self, AppendXAttrExpressionMixIn):
            expression = self._append_x_attr_expression(
                expression=expression, indent_num=INDENT_NUM
            )
        if isinstance(self, AppendYAttrExpressionMixIn):
            expression = self._append_y_attr_expression(
                expression=expression, indent_num=INDENT_NUM
            )
        expression += "\n  });"
        expression_data_util.append_js_expression(expression=expression)
        self._points_var_name = points_var_name
