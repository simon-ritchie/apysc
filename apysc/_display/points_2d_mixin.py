"""Class implementation for 2-dimensional points mix-in.
"""

from typing import Dict
from typing import Tuple

from typing_extensions import final

from apysc._geom.point2d import Point2D
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class Points2DMixIn(VariableNameSuffixAttrOrVarMixIn, VariableNameMixIn, RevertMixIn):

    _points: Array[Point2D]

    @final
    def _initialize_points_if_not_initialized(self) -> None:
        """
        Initialize _points attribute ifa this interface does not
        initialize it yet.
        """
        if hasattr(self, "_points"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="points")
        self._points = Array(
            [],
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def points(self) -> Array[Point2D]:
        """
        Get current points.

        Returns
        -------
        points : Array of Point2D
            Current points.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color="#fff")
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=0, y=0),
        ...         ap.Point2D(x=50, y=0),
        ...     ]
        ... )
        >>> polygon.points
        Array([Point2D(Number(0.0), Number(0.0)), Point2D(Number(50.0), Number(0.0))])
        """
        self._initialize_points_if_not_initialized()
        return self._points

    @points.setter
    @arg_validation_decos.is_point_2ds(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def points(self, value: Array[Point2D]) -> None:
        """
        Update points value.

        Parameters
        ----------
        value : Array of Point2D
            Points value to set.

        Raises
        ------
        ValueError
            If array contains not Point2D value.
        """
        self._initialize_points_if_not_initialized()
        self._append_points_update_expression(value=value)
        self._points = value

    @final
    def _make_2dim_points_expression(self) -> Tuple[str, str]:
        """
        Make JavaScript expression string.

        Returns
        -------
        variable_name: str
            Created JavaScript points variable (2-dimensional array) name.
        expression : str
            JavaScript expression string. This expression make
            2-dimensional JavaScript array variable, like
            '[[x_1, y_1], [x_2, y_2], ...]'.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._initialize_points_if_not_initialized()
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.ARRAY
        )
        i_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.INDEX
        )
        points_name: str = self._points.variable_name
        point_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.POINT2D
        )
        expression: str = (
            f"var {variable_name} = [];"
            f"\nfor (var {i_name} = 0; {i_name} < {points_name}.length; "
            f"{i_name}++) {{"
            f"\n  var {point_name} = {points_name}[{i_name}];"
            f"\n  {variable_name}.push("
            f'[{point_name}["x"], {point_name}["y"]]);'
            "}"
        )
        return variable_name, expression

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_points_update_expression(self, *, value: Array) -> None:
        """
        Append points updating expression.

        Parameters
        ----------
        value : Array
            Points value to set.
        """
        import apysc as ap

        expression: str = f"{self._points.variable_name} = {value.variable_name};"
        ap.append_js_expression(expression=expression)

    _points_snapshots: Dict[str, Array]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make values' snapshots.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_points_if_not_initialized()
        self._points._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name="_points_snapshots",
            value=self._points,
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert values if snapshots exist.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._points = self._points_snapshots[snapshot_name]
        self._points._run_all_revert_methods(snapshot_name=snapshot_name)
