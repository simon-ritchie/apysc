"""Class implementation for visible interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class VisibleInterface(
        VariableNameInterface, RevertInterface, AttrLinkingInterface):

    _visible: ap.Boolean

    def _initialize_visible_if_not_initialized(self) -> None:
        """
        Initialize _visible attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_visible'):
            return
        self._visible = ap.Boolean(True)

        self._append_visible_attr_linking_setting()

    def _append_visible_attr_linking_setting(self) -> None:
        """
        Append a visible attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self._append_visible_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=VisibleInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._visible, attr_name='visible')
            self._append_attr_to_linking_stack(
                attr=self._visible, attr_name='visible')

    @property
    def visible(self) -> ap.Boolean:
        """
        Get a visibility of this instance.

        Returns
        -------
        result : Boolean
            If this instance is visible, True will be returned.
        """
        with ap.DebugInfo(
                callable_='visible', locals_=locals(),
                module_name=__name__, class_=VisibleInterface):
            from apysc._type import value_util
            self._initialize_visible_if_not_initialized()
            return value_util.get_copy(value=self._visible)

    @visible.setter
    def visible(self, value: ap.Boolean) -> None:
        """
        Update visibility of this instance.

        Parameters
        ----------
        value : Boolean
            Boolean value to set.
        """
        with ap.DebugInfo(
                callable_='visible', locals_=locals(),
                module_name=__name__, class_=VisibleInterface):
            from apysc._validation import bool_validation
            bool_validation.validate_bool(value=value)
            if isinstance(value, bool):
                value = ap.Boolean(value)
            self._visible = value
            self._append_visible_update_expression()

            self._append_visible_attr_linking_setting()

    def _append_visible_update_expression(self) -> None:
        """
        Append visible property updating expression.
        """
        with ap.DebugInfo(
                callable_=self._append_visible_update_expression,
                locals_=locals(),
                module_name=__name__, class_=VisibleInterface):
            expression: str = (
                f'if ({self._visible.variable_name}) {{'
                f'\n  {self.variable_name}.show();'
                '\n}else {'
                f'\n  {self.variable_name}.hide();'
                '\n}'
            )
            ap.append_js_expression(expression=expression)

    _visible_snapshots: Dict[str, bool]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_visible_snapshots'):
            self._visible_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_visible_if_not_initialized()
        self._visible_snapshots[snapshot_name] = self._visible._value

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert value is snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._visible._value = self._visible_snapshots[snapshot_name]
