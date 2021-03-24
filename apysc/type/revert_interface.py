"""Class implementation for revert interface.
"""

from abc import ABC, abstractmethod
from typing import Dict


class RevertInterface(ABC):

    _snapshot_exists: Dict[str, bool] = {}

    @abstractmethod
    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    @abstractmethod
    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    def _is_snapshot_exists(self, snapshot_name: str) -> bool:
        """
        Get a boolean value whether snapshot value exists or not.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.

        Returns
        -------
        snapshot_exists : bool
            Boolean value whether snapshot value exists or not.
        """
        return snapshot_name in self._snapshot_exists

    def _set_snapshot_exists_val(self, snapshot_name: str) -> None:
        """
        Set boolean value whether snapshot value exists or not.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._snapshot_exists[snapshot_name] = True

    def _delete_snapshot_exists_val(self, snapshot_name: str) -> None:
        """
        Delete boolean value whether snapshot value exists or not.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if snapshot_name in self._snapshot_exists:
            del self._snapshot_exists[snapshot_name]
