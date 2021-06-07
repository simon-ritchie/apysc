"""Class implementation for the center y-coordinate interface.
"""

from typing import Dict

from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class CyInterface(VariableNameInterface, RevertInterface):

    _cy: Int

    def _initialize_cy_if_not_initialized(self) -> None:
        """
        Initialize _cy attribute if it is not initialized yet.
        """
        if hasattr(self, '_cy'):
            return
        self._cy = Int(0)

    @property
    def y(self) -> Int:
        """
        Get a center y-coordinate.

        Returns
        -------
        y : Int
            Center y-coordinate.
        """
        from apysc.type import value_util
        self._initialize_cy_if_not_initialized()
        return value_util.get_copy(value=self._cy)

    @y.setter
    def y(self, value: Int) -> None:
        """
        Update a center y-coordinate.

        Parameters
        ----------
        value : int or Int
            Center y-coordinate value.
        """
        from apysc.validation import number_validation
        number_validation.validate_integer(integer=value)
        if not isinstance(value, Int):
            value = Int(value)
        self._cy = value

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert a value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
