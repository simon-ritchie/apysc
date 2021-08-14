"""Class implementation for the JavaScript expression string.
"""

from typing import Dict
from apysc._type.revert_interface import RevertInterface


class ExpressionString(RevertInterface):
    """
    The class for the JavaScript expression string.
    """

    _value: str

    def __init__(self, value: str) -> None:
        """
        The class for the JavaScript expression string.

        Parameters
        ----------
        value : str
            String to set.
        """
        self._value = value

    _value_snapshots: Dict[str, str]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
