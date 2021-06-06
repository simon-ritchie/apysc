"""Class implementation for center x-coordinate interface.
"""

from typing import Dict

from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class CxInterface(VariableNameInterface, RevertInterface):

    _cx: Int

    def _initialize_cx_if_not_initialized(self) -> None:
        """
        Initialize _cx attribute if it is not initialized yet.
        """
        if hasattr(self, '_cx'):
            return
        self._cx = Int(0)

    @property
    def cx(self) -> Int:
        """
        Get a center x-coordinate.

        Parameters
        ----------
        cx : Int
            Center x-coordinate.
        """
        from apysc.type import value_util
        self._initialize_cx_if_not_initialized()
        return value_util.get_copy(value=self._cx)

    @cx.setter
    def cx(self, value: Int) -> None:
        """
        Update center x-coordinate.

        Parameters
        ----------
        value : int or Int
            Center x-coordinate value.
        """
        from apysc.validation import number_validation
        number_validation.validate_integer(integer=value)
        if not isinstance(value, Int):
            value = Int(value)
        self._cx = value

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
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
