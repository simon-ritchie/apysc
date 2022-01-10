"""Class implementation for 2-dimensional points interface.
"""

from typing import Dict
from typing import Tuple

from apysc._geom.point2d import Point2D
from apysc._type.array import Array
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class Points2DInterface(VariableNameInterface, RevertInterface):

    _points: Array[Point2D]

    def _initialize_points_if_not_initialized(self) -> None:
        """
        Initialize _points attribute if it hasn't been initialized yet.
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

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff')
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=0, y=0),
        ...         ap.Point2D(x=50, y=0),
        ...     ])
        >>> polygon.points
        Array([Point2D(Int(0), Int(0)), Point2D(Int(50), Int(0))])
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='points', locals_=locals(),
                module_name=__name__, class_=Points2DInterface):
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
        import apysc as ap
        with ap.DebugInfo(
                callable_='points', locals_=locals(),
                module_name=__name__, class_=Points2DInterface):
            for point in value.value:  # type: ignore
                if isinstance(point, Point2D):
                    continue
                raise ValueError(
                    'Specified array contains not Point2D value: '
                    f'{type(point)}')
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

    def _append_points_update_expression(self, *, value: Array) -> None:
        """
        Append points updating expression.

        Parameters
        ----------
        value : Array
            Points value to set.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_points_update_expression,
                locals_=locals(),
                module_name=__name__, class_=Points2DInterface):
            expression: str = (
                f'{self._points.variable_name} = {value.variable_name};'
            )
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
        self._points._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name='_points_snapshots',
            value=self._points, snapshot_name=snapshot_name)

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
