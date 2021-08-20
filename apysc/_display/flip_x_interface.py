"""Class implementation for the flip_x interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class FlipXInterface(VariableNameInterface, RevertInterface):

    _flip_x: ap.Boolean

    def _initialize_flip_x_if_not_initialized(self) -> None:
        """
        Initialize the _flip_x attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_flip_x'):
            return
        self._flip_x = ap.Boolean(False)

    @property
    def flip_x(self) -> ap.Boolean:
        """
        Get a boolean value whether the x-axis is flipped or not.

        Returns
        -------
        flip_x : Boolean
            A boolean value whether the x-axis is flipped or not.
        """
        with ap.DebugInfo(
                callable_='flip_x', locals_=locals(),
                module_name=__name__, class_=FlipXInterface):
            from apysc._type import value_util
            self._initialize_flip_x_if_not_initialized()
            return value_util.get_copy(value=self._flip_x)

    @flip_x.setter
    def flip_x(self, value: ap.Boolean) -> None:
        """
        Update the x-axis flipping value.

        Parameters
        ----------
        value : Boolean
            Flipping value. If True, the x-axis will be flipped,
            otherwise if will be reset.
        """
        with ap.DebugInfo(
                callable_='flip_x', locals_=locals(),
                module_name=__name__, class_=FlipXInterface):
            self._flip_x = value

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
