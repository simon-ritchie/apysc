"""Interface class implementation for the x path data.
"""

from typing import Dict

from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class PathXInterface(RevertInterface):

    _x: Int

    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize the _x attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_x'):
            return
        self._x = Int(0)

    @property
    def x(self) -> Int:
        """
        Get a x-coordinate of the destination point.

        Returns
        -------
        x : Int
            A x-coordinate of the destination point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=PathXInterface):
            self._initialize_x_if_not_initialized()
            return self._x._copy()

    @x.setter
    def x(self, value: Int) -> None:
        """
        Set a x-coordinate of the destination point.

        Parameters
        ----------
        value : Int
            X-coordinate of the destination point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=PathXInterface):
            self._initialize_x_if_not_initialized()
            self._x.value = value

    _x_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_x_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_x_snapshots',
            value=int(self._x._value), snapshot_name=snapshot_name)

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
        self._initialize_x_if_not_initialized()
        self._x._value = self._x_snapshots[snapshot_name]
