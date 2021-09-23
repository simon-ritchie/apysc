"""Class implementation for the y-coordinate interface.
"""

from typing import Dict

import apysc as ap
from apysc._animation.animation_move_interface import AnimationMoveInterface
from apysc._animation.animation_y_interface import AnimationYInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface


class YInterface(
        AnimationYInterface, AnimationMoveInterface, RevertInterface,
        AttrLinkingInterface):

    _y: ap.Int

    def _initialize_y_if_not_initialized(self) -> None:
        """
        Initialize the _y attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_y'):
            return
        self._y = ap.Int(0)

        self._append_y_attr_linking_setting()

    def _append_y_attr_linking_setting(self) -> None:
        """
        Append a y attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self._append_y_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=YInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._y, attr_name='y')
            self._append_attr_to_linking_stack(
                attr=self._y, attr_name='y')

    @property
    def y(self) -> ap.Int:
        """
        Get a y-coordinate.

        Returns
        -------
        y : Int
            Y-coordinate.

        References
        ----------
        - Display object x and y interfaces document
            - https://bit.ly/2ToA5ba
        """
        with ap.DebugInfo(
                callable_='y', locals_=locals(),
                module_name=__name__, class_=YInterface):
            from apysc._type import value_util
            self._initialize_y_if_not_initialized()
            y: ap.Int = value_util.get_copy(value=self._y)
            return y

    @y.setter
    def y(self, value: ap.Int) -> None:
        """
        Update y-coordinate.

        Parameters
        ----------
        value : int or Int
            Y-coordinate value.

        References
        ----------
        - Display object x and y interfaces document
            - https://bit.ly/2ToA5ba
        """
        with ap.DebugInfo(
                callable_='y', locals_=locals(),
                module_name=__name__, class_=YInterface):
            from apysc._type.number_value_interface import NumberValueInterface
            from apysc._validation import number_validation
            if not isinstance(value, NumberValueInterface):
                number_validation.validate_integer(integer=value)
                value = ap.Int(value=value)
            self._y = value
            self._y._append_incremental_calc_substitution_expression()
            self._append_y_update_expression()

            self._append_y_attr_linking_setting()

    def _append_y_update_expression(self) -> None:
        """
        Append y position updating expression.
        """
        with ap.DebugInfo(
                callable_=self._append_y_update_expression, locals_=locals(),
                module_name=__name__, class_=YInterface):
            from apysc._type import value_util
            self._initialize_y_if_not_initialized()
            value_str: str = value_util.get_value_str_for_expression(
                value=self._y)
            expression: str = (
                f'{self.variable_name}.y({value_str});'
            )
            ap.append_js_expression(expression=expression)

    _y_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_y_snapshots'):
            self._y_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_y_if_not_initialized()
        self._y_snapshots[snapshot_name] = int(self._y._value)

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
        self._y._value = self._y_snapshots[snapshot_name]
