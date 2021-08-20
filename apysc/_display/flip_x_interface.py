"""Class implementation for the flip_x interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class FlipXInterface(VariableNameInterface, RevertInterface):

    _flip_x: ap.Boolean

    def _initialize_flip_x_if_not_initialized(self) -> None:
        """
        Initialize the _flip_x attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_flip_x'):
            return
        self._flip_x = ap.Boolean(False)

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
