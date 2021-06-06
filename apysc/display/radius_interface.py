"""Class implementation for radius value interface.
"""

from typing import Dict

from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class RadiusInterface(VariableNameInterface, RevertInterface):

    _radius: Int

    def _initialize_radius_if_not_initialized(self) -> None:
        """
        Initialize _radius attribute if it is not initialized yet.
        """
        if hasattr(self, '_radius'):
            return
        self._radius = Int(0)

    @property
    def radius(self) -> Int:
        """
        Get radius value.

        Returns
        -------
        radius : Int
            Radius value.
        """
        from apysc.type import value_util
        self._initialize_radius_if_not_initialized()
        return value_util.get_copy(value=self._radius)

    @radius.setter
    def radius(self, value: Int) -> None:
        """
        Update radius value.

        Parameters
        ----------
        value : int or Int
            Radius value.
        """
        from apysc.validation import number_validation
        number_validation.validate_integer(integer=value)
        if not isinstance(value, Int):
            value = Int(value)
        self._radius = value

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
