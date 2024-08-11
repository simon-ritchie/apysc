"""Class implementation for the `apply_current_points` mix-in.
"""

from apysc._display.points_2d_mixin import Points2DMixIn


class PolygonApplyCurrentPointsMixIn(Points2DMixIn):
    def _apply_current_points(self) -> None:
        """
        Apply current points settings and re-draw a polygon graphic.
        """
        from apysc._expression import expression_data_util
        from apysc._type.variable_name_mixin import VariableNameMixIn
        from apysc._validation.variable_name_validation import (
            validate_variable_name_mixin_type,
        )

        points_var_name: str
        points_expression: str
        self_instance: VariableNameMixIn = validate_variable_name_mixin_type(
            instance=self,
        )
        points_var_name, points_expression = self._make_2dim_points_expression()
        expression_data_util.append_js_expression(expression=points_expression)
        expression: str = f"{self_instance.variable_name}.plot({points_var_name});"
        expression_data_util.append_js_expression(expression=expression)
