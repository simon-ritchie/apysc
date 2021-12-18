"""Interface class implementation for the control x path data.
"""

from typing import Dict

from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class PathControlXInterface(RevertInterface):

    _control_x: Int

    def _initialize_control_x_if_not_initialized(self) -> None:
        """
        Initialize the _control_x attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_control_x'):
            return
        self._control_x = Int(0)

    @property
    def control_x(self) -> Int:
        """
        Get a X-coordinate of the point.

        Returns
        -------
        control_x : Int
            X-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_x', locals_=locals(),
                module_name=__name__, class_=PathControlXInterface):
            self._initialize_control_x_if_not_initialized()
            return self._control_x._copy()

    @control_x.setter
    def control_x(self, value: Int) -> None:
        """
        Set a X-coordinate of the control point.

        Parameters
        ----------
        value : Int
            X-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_x', locals_=locals(),
                module_name=__name__, class_=PathControlXInterface):
            self._initialize_control_x_if_not_initialized()
            self._control_x.value = value

    _control_x_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_control_x_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_control_x_snapshots',
            value=int(self._control_x._value), snapshot_name=snapshot_name)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert a value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_control_x_if_not_initialized()
        self._control_x._value = self._control_x_snapshots[snapshot_name]
