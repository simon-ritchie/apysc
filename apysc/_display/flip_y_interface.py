"""Class implementation for the flip_y interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class FlipYInterface(VariableNameInterface, RevertInterface):

    _flip_y: ap.Boolean

    def _initialize_flip_y_if_not_initialized(self) -> None:
        """
        Initialize the _flip_y attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_flip_y'):
            return
        self._flip_y = ap.Boolean(False)

    @property
    def flip_y(self) -> ap.Boolean:
        """
        Get a boolean value whether the y-axis is flipped or not.

        Returns
        -------
        flip_y : Boolean
            A boolean value whether the y-axis is flipped or not.
        """
        with ap.DebugInfo(
                callable_='flip_y', locals_=locals(),
                module_name=__name__, class_=FlipYInterface):
            from apysc._type import value_util
            self._initialize_flip_y_if_not_initialized()
            return value_util.get_copy(value=self._flip_y)

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
