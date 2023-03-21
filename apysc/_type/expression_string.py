"""Class implementation for the JavaScript expression string.
"""

from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._type.revert_mixin import RevertMixIn


class ExpressionString(RevertMixIn):
    """
    This class is for the JavaScript expression string.
    """

    _value: str

    @final
    def __init__(self, value: str) -> None:
        """
        The class for the JavaScript expression string.

        Parameters
        ----------
        value : str
            String to set.
        """
        self._value = value

    _value_snapshots: Optional[Dict[str, str]] = None

    @property
    def value(self) -> str:
        """
        Get a expression string.

        Returns
        -------
        value : str
            A expression string.
        """
        return self._value

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_value_snapshots", value=self._value, snapshot_name=snapshot_name
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._value = self._get_snapshot_val_if_exists(
            current_value=self._value,
            snapshot_dict=self._value_snapshots,
            snapshot_name=snapshot_name,
        )
