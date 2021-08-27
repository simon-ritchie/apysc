"""Class implementation for the skew x interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class SkewXInterface(VariableNameInterface, RevertInterface):

    _skew_x: ap.Int

    def _initialize_skew_x_if_not_initialized(self) -> None:
        """
        Initialize the _skew_x attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_skew_x'):
            return
        self._skew_x = ap.Int(0)

    @property
    def skew_x(self) -> ap.Int:
        """
        Get a current skew x value of the instance.

        Returns
        -------
        skew_x : Int
            Current skew x value of this instance.
        """
        with ap.DebugInfo(
                callable_='skew_x', locals_=locals(),
                module_name=__name__, class_=SkewXInterface):
            from apysc._type import value_util
            self._initialize_skew_x_if_not_initialized()
            return value_util.get_copy(value=self._skew_x)

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
