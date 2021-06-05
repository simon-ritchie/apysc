"""Class implementation for radius value interface.
"""

from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class RadiusInterface(VariableNameInterface, RevertInterface):

    _radius: Int

    def _initialize_radius_if_not_initialized(self) -> None:
        """
        Initialize _radius attribute if it is not initialized yet.
        """
        if hasattr(self, '_radius'):
            return
        self._radius = Int(0)

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
