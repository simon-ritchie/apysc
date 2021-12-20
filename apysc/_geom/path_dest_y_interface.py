"""Interface class implementation for the destination y path data.
"""

from typing import Dict

from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class PathDestYInterface(RevertInterface):

    _dest_y: Int

    def _initialize_dest_y_if_not_initialized(self) -> None:
        """
        Initialize the _dest_y attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_dest_y'):
            return
        self._dest_y = Int(0)

    @property
    def dest_y(self) -> Int:
        """
        Get a y-coordinate of the destination point.

        Returns
        -------
        dest_y : Int
            Y-coordinate of the destination point
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='dest_y', locals_=locals(),
                module_name=__name__, class_=PathDestYInterface):
            self._initialize_dest_y_if_not_initialized()
            return self._dest_y._copy()

    @dest_y.setter
    def dest_y(self, value: Int) -> None:
        """
        Set a y-coordinate of the destination point.

        Parameters
        ----------
        value : Int
            Y-coordinate of the destination point
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='dest_y', locals_=locals(),
                module_name=__name__, class_=PathDestYInterface):
            self._initialize_dest_y_if_not_initialized()
            self._dest_y.value = value

    _dest_y_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_dest_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_dest_y_snapshots',
            value=int(self._dest_y._value), snapshot_name=snapshot_name)

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
        self._initialize_dest_y_if_not_initialized()
        self._dest_y._value = self._dest_y_snapshots[snapshot_name]
