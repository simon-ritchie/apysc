"""Class implementation for the scale_y_from_center interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class ScaleYFromCenterInterface(VariableNameInterface, RevertInterface):

    _scale_y_from_center: ap.Number

    def _initialize_scale_y_from_center_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_y_from_center` attribute if it hasn't been
        initialized yet.'
        """
        if hasattr(self, '_scale_y_from_center'):
            return
        self._scale_y_from_center = ap.Number(1.0)

    @property
    def scale_y_from_center(self) -> ap.Number:
        """
        Get a scale-y value from the center of this instance.

        Returns
        -------
        scale_y_from_center : ap.Number
            Scale-y value from the center of this instance.
        """
        with ap.DebugInfo(
                callable_='scale_y_from_center', locals_=locals(),
                module_name=__name__, class_=ScaleYFromCenterInterface):
            from apysc._type import value_util
            self._initialize_scale_y_from_center_if_not_initialized()
            return value_util.get_copy(value=self._scale_y_from_center)

    @scale_y_from_center.setter
    def scale_y_from_center(self, value: ap.Number) -> None:
        """
        Update a scale-y value from the center of this instance.

        Parameters
        ----------
        value : ap.Number
            Scale-y value from the center of this instance.
        """
        with ap.DebugInfo(
                callable_='scale_y_from_center', locals_=locals(),
                module_name=__name__, class_=ScaleYFromCenterInterface):
            from apysc._validation import number_validation
            self._initialize_scale_y_from_center_if_not_initialized()
            number_validation.validate_num(num=value)
            if not isinstance(value, ap.Number):
                value = ap.Number(value)
            before_value: ap.Number = self._scale_y_from_center
            self._scale_y_from_center = value
            self._append_scale_y_from_center_update_expression(
                before_value=before_value)

    def _append_scale_y_from_center_update_expression(
            self, before_value: ap.Number) -> None:
        """
        Append the scale-y from the center of this instance
        updating expression.

        Parameters
        ----------
        before_value : ap.Number
            Before updating value.
        """
        with ap.DebugInfo(
                callable_=self._append_scale_y_from_center_update_expression,
                locals_=locals(),
                module_name=__name__, class_=ScaleYFromCenterInterface):
            from apysc._type import value_util
            before_value_str: str = value_util.get_value_str_for_expression(
                value=before_value)
            after_value_str: str = value_util.get_value_str_for_expression(
                value=self._scale_y_from_center)
            expression: str = (
                f'{self.variable_name}.scale(1, 1 / {before_value_str});'
                f'\n{self.variable_name}.scale(1, {after_value_str});'
                f'\n{before_value_str} = {after_value_str};'
            )
            ap.append_js_expression(expression=expression)

    _scale_y_from_center_snapshots: Dict[str, float]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_scale_y_from_center_snapshots'):
            self._scale_y_from_center_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_scale_y_from_center_if_not_initialized()
        self._scale_y_from_center_snapshots[snapshot_name] = \
            self._scale_y_from_center._value

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert a value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._scale_y_from_center._value = \
            self._scale_y_from_center_snapshots[snapshot_name]
