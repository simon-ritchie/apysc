"""Class implementation for the center y-coordinate interface.
"""

from typing import Dict

from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class CyInterface(VariableNameInterface, RevertInterface):

    _cy: Int

    def _initialize_cy_if_not_initialized(self) -> None:
        """
        Initialize _cy attribute if it is not initialized yet.
        """
        if hasattr(self, '_cy'):
            return
        self._cy = Int(0)

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
