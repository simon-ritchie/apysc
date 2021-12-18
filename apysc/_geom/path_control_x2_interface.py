"""Interface class implementation for the second control x path data.
"""

from typing import Dict

from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class PathControlX2Interface(RevertInterface):

    _control_x2: Int

    def _initialize_control_x2_if_not_initialized(self) -> None:
        """
        Initialize the _control_x2 attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_control_x2'):
            return
        self._control_x2 = Int(0)

    @property
    def control_x2(self) -> Int:
        """
        Get a second x-coordinate of the control point.

        Returns
        -------
        control_x2 : Int
            Second x-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_x2', locals_=locals(),
                module_name=__name__, class_=PathControlX2Interface):
            self._initialize_control_x2_if_not_initialized()
            return self._control_x2._copy()

    @control_x2.setter
    def control_x2(self, value: Int) -> None:
        """
        Set a second x-coordinate of the control point.

        Parameters
        ----------
        value : Int
            Second x-coordinate of the control point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='control_x2', locals_=locals(),
                module_name=__name__, class_=PathControlX2Interface):
            self._initialize_control_x2_if_not_initialized()
            self._control_x2.value = value

    _control_x2_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_control_x2_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_control_x2_snapshots',
            value=int(self._control_x2._value), snapshot_name=snapshot_name)

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
        self._initialize_control_x2_if_not_initialized()
        self._control_x2._value = self._control_x2_snapshots[snapshot_name]
