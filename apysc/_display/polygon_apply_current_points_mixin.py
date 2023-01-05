"""Class implementation for the `apply_current_points` mix-in.
"""

from apysc._type.variable_name_mixin import VariableNameMixIn


class PolygonApplyCurrentPointsMixIn(VariableNameMixIn):

    _points_var_name: str

    def _apply_current_points(self) -> None:
        """
        Apply current points settings and re-draw a polygon graphic.
        """
        import apysc as ap

        ap.append_js_expression(
            expression=f"{self.variable_name}.plot({self._points_var_name});"
        )
