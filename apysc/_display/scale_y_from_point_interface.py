"""Class implementation for the scale_y_from_point interfaces.
"""

from typing import Any
from typing import Dict

import apysc as ap
from apysc._type.expression_string import ExpressionString
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class ScaleYFromPointInterface(VariableNameInterface, RevertInterface):

    _scale_y_from_point: ap.Dictionary[str, ap.Number]

    def _initialize_scale_y_from_point_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_y_from_point` attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_scale_y_from_point'):
            return
        self._scale_y_from_point = ap.Dictionary({})

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert a value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
