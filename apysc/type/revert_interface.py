"""Class implementation for revert interface.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional


class RevertInterface(ABC):

    _snapshot_exists: Dict[str, bool]

    def _initialize_ss_exists_val_if_not_initialized(self) -> None:
        """
        Initialize _snapshot_exists value if it is not initialized yet.
        """
        if hasattr(self, '_snapshot_exists'):
            return
        self._snapshot_exists = {}

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
        self._initialize_ss_exists_val_if_not_initialized()
        return snapshot_name in self._snapshot_exists

    def _set_snapshot_exists_val(self, snapshot_name: str) -> None:
        """
        Set boolean value whether snapshot value exists or not.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_ss_exists_val_if_not_initialized()
        self._snapshot_exists[snapshot_name] = True

    def _delete_snapshot_exists_val(self, snapshot_name: str) -> None:
        """
        Delete boolean value whether snapshot value exists or not.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_ss_exists_val_if_not_initialized()
        if snapshot_name in self._snapshot_exists:
            del self._snapshot_exists[snapshot_name]

    def _get_next_snapshot_name(self) -> str:
        """
        Get a next snapshot name.

        Returns
        -------
        snapshot_name : str
            Next snapshot name.
        """
        from apysc.expression.var_names import SNAPSHOT
        from apysc.expression import expression_variables_util
        snapshot_name: str = expression_variables_util.get_next_variable_name(
            type_name=SNAPSHOT)
        return snapshot_name
