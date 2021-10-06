"""Class implementation for the scale_x_from_center interface.
"""

from typing import Dict

import apysc as ap
from apysc._animation.animation_scale_x_from_center_interface import \
    AnimationScaleXFromCenterInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface


class ScaleXFromCenterInterface(
        AnimationScaleXFromCenterInterface, RevertInterface,
        AttrLinkingInterface):

    _scale_x_from_center: ap.Number

    def _initialize_scale_x_from_center_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_x_from_center` attribute if it hasn't been
        initialized yet.
        """
        with ap.DebugInfo(
                callable_=self.
                _initialize_scale_x_from_center_if_not_initialized,
                locals_=locals(),
                module_name=__name__, class_=ScaleXFromCenterInterface):
            if hasattr(self, '_scale_x_from_center'):
                return
            self._scale_x_from_center = ap.Number(1.0)

            self._append_scale_x_from_center_attr_linking_setting()

    def _append_scale_x_from_center_attr_linking_setting(self) -> None:
        """
        Append a scale-x attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self.
                _append_scale_x_from_center_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=ScaleXFromCenterInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._scale_x_from_center,
                attr_name='scale_x_from_center')
            self._append_attr_to_linking_stack(
                attr=self._scale_x_from_center,
                attr_name='scale_x_from_center')

    @property
    def scale_x_from_center(self) -> ap.Number:
        """
        Get a scale-x value from the center of this instance.

        Returns
        -------
        scale_x_from_center : ap.Number
            Scale-x value from the center of this instance.

        References
        ----------
        - GraphicsBase scale_x_from_center and scale_y_from_center interfaces
            - https://bit.ly/3ityoCX
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

        References
        ----------
        - GraphicsBase scale_x_from_center and scale_y_from_center interfaces
            - https://bit.ly/3ityoCX
        """
        with ap.DebugInfo(
                callable_='scale_x_from_center', locals_=locals(),
                module_name=__name__, class_=ScaleXFromCenterInterface):
            from apysc._validation import number_validation
            self._initialize_scale_x_from_center_if_not_initialized()
            number_validation.validate_num(num=value)
            if not isinstance(value, ap.Number):
                value = ap.Number(value)
            before_value: ap.Number = self._scale_x_from_center
            self._scale_x_from_center = value
            self._append_scale_x_from_center_update_expression(
                before_value=before_value)

            self._append_scale_x_from_center_attr_linking_setting()

    def _append_scale_x_from_center_update_expression(
            self, before_value: ap.Number) -> None:
        """
        Append the scale-x from the center of this instance
        updating expression.

        Parameters
        ----------
        before_value : ap.Number
            Before updating value.
        """
        with ap.DebugInfo(
                callable_=self._append_scale_x_from_center_update_expression,
                locals_=locals(),
                module_name=__name__, class_=ScaleXFromCenterInterface):
            from apysc._type import value_util
            before_value_str: str = value_util.get_value_str_for_expression(
                value=before_value)
            after_value_str: str = value_util.get_value_str_for_expression(
                value=self._scale_x_from_center)
            expression: str = (
                f'{self.variable_name}.scale(1 / {before_value_str}, 1);'
                f'\n{self.variable_name}.scale({after_value_str}, 1);'
                f'\n{before_value_str} = {after_value_str};'
            )
            ap.append_js_expression(expression=expression)

    _scale_x_from_center_snapshots: Dict[str, float]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_scale_x_from_center_snapshots'):
            self._scale_x_from_center_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_scale_x_from_center_if_not_initialized()
        self._scale_x_from_center_snapshots[snapshot_name] = \
            self._scale_x_from_center._value

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
        self._scale_x_from_center._value = \
            self._scale_x_from_center_snapshots[snapshot_name]
