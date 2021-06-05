"""Class implementation for ellipse height interface.
"""

from typing import Dict
from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class EllipseHeightInterface(VariableNameInterface, RevertInterface):

    _ellipse_height: Int

    def _initialize_ellipse_height_if_not_initialized(self) -> None:
        """
        Initialize _ellipse_height attribute if it is not initialized yet.
        """
        if hasattr(self, '_ellipse_height'):
            return
        self._ellipse_height = Int(0)

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