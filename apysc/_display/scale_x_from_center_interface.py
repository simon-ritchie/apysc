"""Class implementation for the scale_x_from_center interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class ScaleXFromCenterInterface(VariableNameInterface, RevertInterface):

    _scale_x_from_center: ap.Number

    def _initialize_scale_x_from_center_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_x_from_center` attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_scale_x_from_center'):
            return
        self._scale_x_from_center = ap.Number(1.0)

    @property
    def scale_x_from_center(self) -> ap.Number:
        """
        Get a scale-x value from the center of this instance.

        Returns
        -------
        scale_x_from_center : ap.Number
            Scale-x value from the center of this instance.
        """
        with ap.DebugInfo(
                callable_='scale_x_from_center', locals_=locals(),
                module_name=__name__, class_=ScaleXFromCenterInterface):
            from apysc._type import value_util
            self._initialize_scale_x_from_center_if_not_initialized()
            return value_util.get_copy(value=self._scale_x_from_center)

    @scale_x_from_center.setter
    def scale_x_from_center(self, value: ap.Number) -> None:
        """
        Update a scale-x value from the center of this instance.

        Parameters
        ----------
        value : ap.Number
            Scale-x value from the center of this instance.
        """
        with ap.DebugInfo(
                callable_='scale_x_from_center', locals_=locals(),
                module_name=__name__, class_=ScaleXFromCenterInterface):
            from apysc._validation import number_validation
            self._initialize_scale_x_from_center_if_not_initialized()
            number_validation.validate_num(num=value)
            if not isinstance(value, ap.Number):
                value = ap.Number(value)
            self._scale_x_from_center = value

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
