"""Class implementation for visible interface.
"""

from typing import Dict

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class VisibleInterface(VariableNameInterface, RevertInterface):

    _visible: ap.Boolean

    def _initialize_visible_if_not_initialized(self) -> None:
        """
        Initialize _visible attribute it hasn't been initialized yet.
        """
        if hasattr(self, '_visible'):
            return
        self._visible = ap.Boolean(True)

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

    def _append_visible_update_expression(self) -> None:
        """
        Append visible property updating expression to file.
        """
        with ap.DebugInfo(
                callable_=self._append_visible_update_expression,
                locals_=locals(),
                module_name=__name__, class_=VisibleInterface):
            expression: str = f'{self.variable_name}.'
            if self._visible:
                expression += 'show();'
            else:
                expression += 'hide();'
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
