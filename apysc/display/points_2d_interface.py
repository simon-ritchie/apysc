"""Class implementation for 2-dimensional points interface.
"""

from typing import List
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface
from apysc import Point2D


class Points2DInterface(VariableNameInterface, RevertInterface):

    _points: List[Point2D]

    def _initialize_points_if_not_initialized(self) -> None:
        """
        Initialize _points attribute if it is not initialized yet.
        """
        if hasattr(self, '_points'):
            return
        self._points = []

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass
