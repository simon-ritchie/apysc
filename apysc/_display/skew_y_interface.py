"""Class implementation for the skew y interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class SkewYInterface(VariableNameInterface, RevertInterface):

    _skew_y: ap.Int

    def _initialize_skew_y_if_not_initialized(self) -> None:
        """
        Initialize the _skew_y attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_skew_y'):
            return
        self._skew_y = ap.Int(0)


    @property
    def skew_y(self) -> ap.Int:
        """
        Get a current skew y value of the instance.

        Returns
        -------
        skew_y : Int
            Current skew y value of the instance.
        """
        with ap.DebugInfo(
                callable_='skew_y', locals_=locals(),
                module_name=__name__, class_=SkewYInterface):
            from apysc._type import value_util
            self._initialize_skew_y_if_not_initialized()
            return value_util.get_copy(value=self._skew_y)

    @skew_y.setter
    def skew_y(self, value: ap.Int) -> None:
        """
        Update a skew y value of this instance.

        Parameters
        ----------
        value : Int
            Skew y value to set.
        """
        with ap.DebugInfo(
                callable_='skew_y', locals_=locals(),
                module_name=__name__, class_=SkewYInterface):
            from apysc._validation import number_validation
            self._initialize_skew_y_if_not_initialized()
            number_validation.validate_integer(integer=value)
            self._skew_y = value

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
