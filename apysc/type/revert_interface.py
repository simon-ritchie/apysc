"""Class implementation for revert interface.
"""

from abc import ABC, abstractmethod


class RevertInterface(ABC):

    _snapshot_exists: bool = False

    @abstractmethod
    def make_snapshot(self) -> None:
        """
        Make values snapshot.
        """

    @abstractmethod
    def revert(self) -> None:
        """
        Revert values if snapshot exists.
        """

    @property
    def snapshot_exists(self) -> bool:
        """
        Get a boolean value whether snapshot value exists or not.

        Returns
        -------
        snapshot_exists : bool
            Boolean value whether snapshot value exists or not.
        """
        return self._snapshot_exists

    @snapshot_exists.setter
    def snapshot_exists(self, value: bool) -> None:
        """
        Update boolean value whether snapshot value exists or not.

        Parameters
        ----------
        value : bool
            Value to set.
        """
        self._snapshot_exists = value
