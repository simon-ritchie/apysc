"""Interface class implementation for the destination x path data.
"""

from typing import Dict

from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class PathDestXInterface(RevertInterface):

    _dest_x: Int

    def _initialize_dest_x_if_not_initialized(self) -> None:
        """
        Initialize the _dest_x attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_dest_x'):
            return
        self._dest_x = Int(0)

    @property
    def dest_x(self) -> Int:
        """
        Get a x-coordinate of the destination point.

        Returns
        -------
        dest_x : Int
            X-coordinate of the destination point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='dest_x', locals_=locals(),
                module_name=__name__, class_=PathDestXInterface):
            self._initialize_dest_x_if_not_initialized()
            return self._dest_x._copy()

    @dest_x.setter
    def dest_x(self, value: Int) -> None:
        """
        Set a x-coordinate of the destination point.

        Parameters
        ----------
        value : Int
            X-coordinate of the destination point.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='dest_x', locals_=locals(),
                module_name=__name__, class_=PathDestXInterface):
            self._initialize_dest_x_if_not_initialized()
            self._dest_x.value = value

    _dest_x_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_dest_x_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_dest_x_snapshots',
            value=int(self._dest_x._value), snapshot_name=snapshot_name)

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
        self._initialize_dest_x_if_not_initialized()
        self._dest_x._value = self._dest_x_snapshots[snapshot_name]
