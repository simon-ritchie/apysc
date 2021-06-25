"""Class implementation for 2-dimensional points interface.
"""

from typing import Dict
from typing import Tuple

from apysc import Array
from apysc._geom.point2d import Point2D
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class Points2DInterface(VariableNameInterface, RevertInterface):

    _points: Array[Point2D]

    def _initialize_points_if_not_initialized(self) -> None:
        """
        Initialize _points attribute if it is not initialized yet.
        """
        if hasattr(self, '_points'):
            return
        self._points = Array([])

    @property
    def points(self) -> Array[Point2D]:
        """
        Get current points.

        Returns
        -------
        points : Array of Point2D
            Current points.
        """
        self._initialize_points_if_not_initialized()
        return self._points

    @points.setter
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
        for point in value.value:
            if isinstance(point, Point2D):
                continue
            raise ValueError(
                f'Specified array contains not Point2D value: {type(point)}')
        self._initialize_points_if_not_initialized()
        self._append_points_update_expression(value=value)
        self._points = value

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
            type_name=var_names.ARRAY)
        i_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.INDEX)
        points_name: str = self._points.variable_name
        point_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.POINT2D)
        expression: str = (
            f'var {variable_name} = [];'
            f'\nfor (var {i_name} = 0; {i_name} < {points_name}.length; '
            f'{i_name}++) {{'
            f'\n  var {point_name} = {points_name}[{i_name}];'
            f'\n  {variable_name}.push('
            f'[{point_name}["x"], {point_name}["y"]]);'
            '}'
        )
        return variable_name, expression

    def _append_points_update_expression(self, value: Array) -> None:
        """
        Append points updating expression to file.

        Parameters
        ----------
        value : Array
            Points value to set.
        """
        from apysc import append_js_expression
        expression: str = (
            f'{self._points.variable_name} = {value.variable_name};'
        )
        append_js_expression(expression=expression)

    _points_snapshots: Dict[str, Array]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapshots.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_points_snapshots'):
            self._points_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_points_if_not_initialized()
        self._points._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        self._points_snapshots[snapshot_name] = self._points

    def _revert(self, snapshot_name: str) -> None:
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
