"""Class implementation for 2-dimensional points interface.
"""

from typing import List
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface
from apysc import Point2D, Array


class Points2DInterface(VariableNameInterface):

    _points: Array

    def _initialize_points_if_not_initialized(self) -> None:
        """
        Initialize _points attribute if it is not initialized yet.
        """
        if hasattr(self, '_points'):
            return
        self._points = Array([])

    @property
    def points(self) -> Array:
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
    def points(self, value: Array) -> None:
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

    def _append_points_update_expression(self, value: Array) -> None:
        """
        Append points updating expression to file.

        Parameters
        ----------
        value : Array
            Points value to set.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'{self._points.variable_name} = {value.variable_name};'
        )
        expression_file_util.append_js_expression(expression=expression)

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass
