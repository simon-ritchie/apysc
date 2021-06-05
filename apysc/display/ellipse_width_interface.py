"""Class implementation for ellipse width interface.
"""

from typing import Dict
from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class EllipseWidthInterface(VariableNameInterface, RevertInterface):

    _ellipse_width: Int

    def _initialize_ellipse_width_if_not_initialized(self) -> None:
        """
        Initialize _ellipse_width attribute if it is not initialized yet.
        """
        if hasattr(self, '_ellipse_width'):
            return
        self._ellipse_width = Int(0)

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        pass

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        pass
