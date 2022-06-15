"""This module is for the class implementation of
the `DeletedObjectInterface`.
"""

from typing import Dict
from apysc._type.revert_interface import RevertInterface


class DeletedObjectInterface(RevertInterface):

    _is_deleted_object: bool = False

    @property
    def is_deleted_object(self) -> bool:
        """
        Get a boolean indicating whether this object is
        deleted object or not.

        Returns
        -------
        is_deleted_object : bool
            A boolean indicating whether this object is
            deleted object or not.
        """
        return self._is_deleted_object

    @is_deleted_object.setter
    def is_deleted_object(self, value: bool) -> None:
        """
        Set a boolean indicating whether this object is
        deleted object or not.

        Parameters
        ----------
        value : bool
            A target value to set.
        """
        self._is_deleted_object = value

    _is_deleted_object_snapshot: Dict[str, bool]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name='_is_deleted_object_snapshot',
            value=self._is_deleted_object, snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._is_deleted_object = self._is_deleted_object_snapshot[
            snapshot_name]
