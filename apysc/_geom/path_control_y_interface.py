"""Interface class implementation for the control y path data.
"""

from typing import Dict

from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class PathControlYInterface(RevertInterface):

    _control_y: Int

    def _initialize_control_y_if_not_initialized(self) -> None:
        """
        Initialize the _control_y attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_control_y'):
            return
        self._control_y = Int(0)

    @property
    def control_y(self) -> Int:
        """
        Get a Y-coordinate of the control point.

        Returns
        -------
        control_y : Int
            Y-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_y', locals_=locals(),
                module_name=__name__, class_=PathControlYInterface):
            self._initialize_control_y_if_not_initialized()
            return self._control_y._copy()

    @control_y.setter
    def control_y(self, value: Int) -> None:
        """
        Set a Y-coordinate of the control point.

        Parameters
        ----------
        value : Int
            Y-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_y', locals_=locals(),
                module_name=__name__, class_=PathControlYInterface):
            self._initialize_control_y_if_not_initialized()
            self._control_y.value = value

    _control_y_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_control_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_control_y_snapshots',
            value=int(self._control_y._value), snapshot_name=snapshot_name)

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
        self._initialize_control_y_if_not_initialized()
        self._control_y._value = self._control_y_snapshots[snapshot_name]
