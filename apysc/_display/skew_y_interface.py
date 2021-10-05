"""Class implementation for the skew y interface.
"""

from typing import Dict

import apysc as ap
from apysc._animation.animation_skew_y_interface import AnimationSkewYInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface


class SkewYInterface(
        AnimationSkewYInterface, RevertInterface, AttrLinkingInterface):

    _skew_y: ap.Int

    def _initialize_skew_y_if_not_initialized(self) -> None:
        """
        Initialize the _skew_y attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_skew_y'):
            return
        self._skew_y = ap.Int(0)

        self._append_skew_y_attr_linking_setting()

    def _append_skew_y_attr_linking_setting(self) -> None:
        """
        Append a skew-y attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self._append_skew_y_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=SkewYInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._skew_y, attr_name='skew_y')
            self._append_attr_to_linking_stack(
                attr=self._skew_y, attr_name='skew_y')

    @property
    def skew_y(self) -> ap.Int:
        """
        Get a current skew y value of the instance.

        Returns
        -------
        skew_y : Int
            Current skew y value of the instance.

        References
        ----------
        - GraphicsBase skew_x and skew_y interfaces document
            - https://simon-ritchie.github.io/apysc/graphics_base_skew.html
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

        References
        ----------
        - GraphicsBase skew_x and skew_y interfaces document
            - https://simon-ritchie.github.io/apysc/graphics_base_skew.html
        """
        with ap.DebugInfo(
                callable_='skew_y', locals_=locals(),
                module_name=__name__, class_=SkewYInterface):
            from apysc._validation import number_validation
            self._initialize_skew_y_if_not_initialized()
            number_validation.validate_integer(integer=value)
            before_value: ap.Int = self._skew_y
            self._skew_y = value
            self._append_skew_y_update_expression(before_value=before_value)

            self._append_skew_y_attr_linking_setting()

    def _append_skew_y_update_expression(self, before_value: ap.Int) -> None:
        """
        Append the skew y updating expression.

        Parameters
        ----------
        before_value : ap.Int
            Before updating value.
        """
        with ap.DebugInfo(
                callable_=self._append_skew_y_update_expression,
                locals_=locals(),
                module_name=__name__, class_=SkewYInterface):
            from apysc._type import value_util
            before_value_str: str = value_util.get_value_str_for_expression(
                value=before_value)
            after_value_str: str = value_util.get_value_str_for_expression(
                value=self._skew_y)
            expression: str = (
                f'{self.variable_name}.skew(0, -{before_value_str});'
                f'\n{self.variable_name}.skew(0, {after_value_str});'
                f'\n{before_value_str} = {after_value_str};'
            )
            ap.append_js_expression(expression=expression)

    _skew_y_snapshot: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_skew_y_snapshot'):
            self._skew_y_snapshot = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_skew_y_if_not_initialized()
        self._skew_y_snapshot[snapshot_name] = int(self._skew_y._value)

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
        self._skew_y._value = self._skew_y_snapshot[snapshot_name]
