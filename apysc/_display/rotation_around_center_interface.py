"""Class implementation for the rotation_around_center_interface
interface.
"""

from typing import Dict

import apysc as ap
from apysc._animation.animation_rotation_around_center_interface import \
    AnimationRotationAroundCenterInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface


class RotationAroundCenterInterface(
        AnimationRotationAroundCenterInterface, RevertInterface,
        AttrLinkingInterface):

    _rotation_around_center: ap.Int

    def _initialize_rotation_around_center_if_not_initialized(self) -> None:
        """
        Initialize the `_rotation_around_center` attribute if if hasn't
        been initialized yet.
        """
        if hasattr(self, '_rotation_around_center'):
            return
        self._rotation_around_center = ap.Int(0)

        self._append_rotation_around_center_attr_linking_setting()

    def _append_rotation_around_center_attr_linking_setting(self) -> None:
        """
        Append a rotation around center attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self.
                _append_rotation_around_center_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=RotationAroundCenterInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._rotation_around_center,
                attr_name='rotation_around_center')
            self._append_attr_to_linking_stack(
                attr=self._rotation_around_center,
                attr_name='rotation_around_center')

    @property
    def rotation_around_center(self) -> ap.Int:
        """
        Get a rotation value around the center of this instance.

        Returns
        -------
        rotation_around_center : Int
            Rotation value around the center of this instance.

        References
        ----------
        - GraphicsBase rotation_around_center interface document
            - https://bit.ly/3AjeSPr
        """
        with ap.DebugInfo(
                callable_='rotation_around_center', locals_=locals(),
                module_name=__name__, class_=RotationAroundCenterInterface):
            from apysc._type import value_util
            self._initialize_rotation_around_center_if_not_initialized()
            return value_util.get_copy(value=self._rotation_around_center)

    @rotation_around_center.setter
    def rotation_around_center(self, value: ap.Int) -> None:
        """
        Update a rotation value around the center of this instance.

        Parameters
        ----------
        value : int or Int
            Rotation value around the center of this instance.

        References
        ----------
        - GraphicsBase rotation_around_center interface
            - https://bit.ly/3AjeSPr
        """
        with ap.DebugInfo(
                callable_='rotation_around_center', locals_=locals(),
                module_name=__name__, class_=RotationAroundCenterInterface):
            from apysc._validation import number_validation
            self._initialize_rotation_around_center_if_not_initialized()
            number_validation.validate_integer(integer=value)
            if not isinstance(value, ap.Int):
                value = ap.Int(value)
            before_value: ap.Int = self._rotation_around_center
            self._rotation_around_center = value
            self._append_rotation_around_center_update_expression(
                before_value=before_value)

            self._append_rotation_around_center_attr_linking_setting()

    def _append_rotation_around_center_update_expression(
            self, before_value: ap.Int) -> None:
        """
        Append the rotation around the center of this instance
        updating expression.

        Parameters
        ----------
        before_value : ap.Int
            Before updating value.
        """
        with ap.DebugInfo(
                callable_=self._append_rotation_around_center_update_expression,  # noqa
                locals_=locals(),
                module_name=__name__, class_=RotationAroundCenterInterface):
            from apysc._type import value_util
            before_value_str: str = value_util.get_value_str_for_expression(
                value=before_value)
            after_value_str: str = value_util.get_value_str_for_expression(
                value=self._rotation_around_center)
            expression: str = (
                f'{self.variable_name}.rotate(-{before_value_str});'
                f'\n{self.variable_name}.rotate({after_value_str});'
                f'\n{before_value_str} = {after_value_str};'
            )
            ap.append_js_expression(expression=expression)

    _rotation_around_center_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_rotation_around_center_snapshots'):
            self._rotation_around_center_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_rotation_around_center_if_not_initialized()
        self._rotation_around_center_snapshots[snapshot_name] = int(
            self._rotation_around_center._value)

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
        self._rotation_around_center._value = \
            self._rotation_around_center_snapshots[snapshot_name]
