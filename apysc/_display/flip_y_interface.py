"""Class implementation for the flip_y interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class FlipYInterface(
        VariableNameInterface, RevertInterface, AttrLinkingInterface):

    _flip_y: ap.Boolean

    def _initialize_flip_y_if_not_initialized(self) -> None:
        """
        Initialize the _flip_y attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_flip_y'):
            return
        self._flip_y = ap.Boolean(False)

        self._append_flip_y_attr_linking_setting()

    def _append_flip_y_attr_linking_setting(self) -> None:
        """
        Append a flip-y attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self._append_flip_y_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=FlipYInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._flip_y, attr_name='flip_y')
            self._append_attr_to_linking_stack(
                attr=self._flip_y, attr_name='flip_y')

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

    @flip_y.setter
    def flip_y(self, value: ap.Boolean) -> None:
        """
        Update a y-axis flipping value.

        Parameters
        ----------
        value : Boolean
            Flipping value. If true, a y-axis will be flipped,
            otherwise it will be reset.
        """
        with ap.DebugInfo(
                callable_='flip_y', locals_=locals(),
                module_name=__name__, class_=FlipYInterface):
            self._initialize_flip_y_if_not_initialized()
            before_value: ap.Boolean = self._flip_y
            self._flip_y = value
            self._append_flip_y_update_expression(before_value=before_value)

            self._append_flip_y_attr_linking_setting()

    def _append_flip_y_update_expression(
            self, before_value: ap.Boolean) -> None:
        """
        Append a y-axis flipping value updating expression.

        Parameters
        ----------
        before_value : Boolean
            Before updating flipping value.
        """
        with ap.DebugInfo(
                callable_=self._append_flip_y_update_expression,
                locals_=locals(),
                module_name=__name__, class_=FlipYInterface):
            from apysc._display import flip_interface_helper
            self._initialize_flip_y_if_not_initialized()
            expression: str = flip_interface_helper.\
                make_flip_update_expression(
                    before_value=before_value, after_value=self._flip_y,
                    axis=flip_interface_helper.Axis.Y,
                    interface_variable_name=self.variable_name)
            ap.append_js_expression(expression=expression)

    _flip_y_snapshots: Dict[str, bool]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_flip_y_snapshots'):
            self._flip_y_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_flip_y_if_not_initialized()
        self._flip_y_snapshots[snapshot_name] = self._flip_y._value

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
        self._flip_y._value = self._flip_y_snapshots[snapshot_name]
