"""Class implementation for the scale_x_from_center interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class ScaleXFromCenterInterface(VariableNameInterface, RevertInterface):

    _scale_x_from_center: ap.Number

    def _initialize_scale_x_from_center_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_x_from_center` attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_scale_x_from_center'):
            return
        self._scale_x_from_center = ap.Number(1.0)

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
