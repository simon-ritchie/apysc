"""Class implementation for the `revert`-related interface.
"""

from abc import ABC
from abc import abstractmethod


class RevertInterface(ABC):
    @abstractmethod
    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    @abstractmethod
    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert values if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
