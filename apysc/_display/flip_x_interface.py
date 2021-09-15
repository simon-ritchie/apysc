"""Class implementation for the flip_x interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class FlipXInterface(
        VariableNameInterface, RevertInterface, AttrLinkingInterface):

    _flip_x: ap.Boolean

    def _initialize_flip_x_if_not_initialized(self) -> None:
        """
        Initialize the _flip_x attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_flip_x'):
            return
        self._flip_x = ap.Boolean(False)

        self._append_flip_x_attr_linking_setting()

    def _append_flip_x_attr_linking_setting(self) -> None:
        """
        Append a flip-x attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self._append_flip_x_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=FlipXInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._flip_x, attr_name='flip_x')
            self._append_attr_to_linking_stack(
                attr=self._flip_x, attr_name='flip_x')

    @property
    def flip_x(self) -> ap.Boolean:
        """
        Get a boolean value whether the x-axis is flipped or not.

        Returns
        -------
        flip_x : Boolean
            A boolean value whether the x-axis is flipped or not.
        """
        with ap.DebugInfo(
                callable_='flip_x', locals_=locals(),
                module_name=__name__, class_=FlipXInterface):
            from apysc._type import value_util
            self._initialize_flip_x_if_not_initialized()
            return value_util.get_copy(value=self._flip_x)

    @flip_x.setter
    def flip_x(self, value: ap.Boolean) -> None:
        """
        Update a x-axis flipping value.

        Parameters
        ----------
        value : Boolean
            Flipping value. If True, a x-axis will be flipped,
            otherwise it will be reset.
        """
        with ap.DebugInfo(
                callable_='flip_x', locals_=locals(),
                module_name=__name__, class_=FlipXInterface):
            self._initialize_flip_x_if_not_initialized()
            before_value: ap.Boolean = self._flip_x
            self._flip_x = value
            self._append_flip_x_update_expression(before_value=before_value)

            self._append_flip_x_attr_linking_setting()

    def _append_flip_x_update_expression(
            self, before_value: ap.Boolean) -> None:
        """
        Append a x-axis flipping value updating expression.

        Parameters
        ----------
        before_value : Boolean
            Before updating flipping value.
        """
        with ap.DebugInfo(
                callable_=self._append_flip_x_update_expression,
                locals_=locals(),
                module_name=__name__, class_=FlipXInterface):
            from apysc._display import flip_interface_helper
            self._initialize_flip_x_if_not_initialized()
            expression: str = flip_interface_helper.\
                make_flip_update_expression(
                    before_value=before_value, after_value=self._flip_x,
                    axis=flip_interface_helper.Axis.X,
                    interface_variable_name=self.variable_name)
            ap.append_js_expression(expression=expression)

    _flip_x_snapshots: Dict[str, bool]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_flip_x_snapshots'):
            self._flip_x_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_flip_x_if_not_initialized()
        self._flip_x_snapshots[snapshot_name] = self._flip_x._value

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
        self._flip_x._value = self._flip_x_snapshots[snapshot_name]
