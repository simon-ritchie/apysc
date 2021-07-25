"""Class implementation for line cap interface.
"""

from typing import Any
from typing import Dict
from typing import Union

import apysc as ap
from apysc._display.line_caps import LineCaps
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class LineCapInterface(VariableNameInterface, RevertInterface):

    _line_cap: ap.String

    def _initialize_line_cap_if_not_initialized(self) -> None:
        """
        Inilialize _line_cap attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_cap'):
            return
        self._line_cap = ap.String(LineCaps.BUTT.value)

    @property
    def line_cap(self) -> Any:
        """
        Get this instance's line cap style setting.

        Returns
        -------
        line_cap : String
            Line cap style setting.
        """
        with ap.DebugInfo(
                callable_='line_cap', locals_=locals(),
                module_name=__name__, class_=LineCapInterface):
            self._initialize_line_cap_if_not_initialized()
            return self._line_cap._copy()

    @line_cap.setter
    def line_cap(self, value: Any) -> None:
        """
        Set line cap style setting.

        Parameters
        ----------
        value : String or LineCaps
            Line cap style setting to set.
        """
        with ap.DebugInfo(
                callable_='line_cap', locals_=locals(),
                module_name=__name__, class_=LineCapInterface):
            self._update_line_cap_and_skip_appending_exp(value=value)
            self._append_line_cap_update_expression()

    def _append_line_cap_update_expression(self) -> None:
        """
        Append line cap updating expression to file.
        """
        with ap.DebugInfo(
                callable_=self._append_line_cap_update_expression,
                locals_=locals(),
                module_name=__name__, class_=LineCapInterface):
            from apysc._type import value_util
            cap_name: str = value_util.get_value_str_for_expression(
                value=self._line_cap)
            expression: str = (
                f'{self.variable_name}.attr({{"stroke-linecap": {cap_name}}});'
            )
            ap.append_js_expression(expression=expression)

    def _update_line_cap_and_skip_appending_exp(
            self, value: Union[ap.String, LineCaps]) -> None:
        """
        Update line cap and skip appending expression to file.

        Parameters
        ----------
        value : String or LineCaps
            Line cap style setting to set.
        """
        from apysc._validation.display_validation import validate_line_cap
        if not isinstance(value, (ap.String, LineCaps)):
            raise TypeError(
                'Not supported line_cap type specified: '
                f'{type(value)}'
                '\nAcceptable ones are: String or LineCaps.')
        validate_line_cap(cap=value)
        if isinstance(value, ap.String):
            self._line_cap = value._copy()
        else:
            self._line_cap = ap.String(value.value)

    _line_cap_snapshots: Dict[str, str]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_line_cap_snapshots'):
            self._line_cap_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_line_cap_if_not_initialized()
        self._line_cap_snapshots[snapshot_name] = self._line_cap._value

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._line_cap._value = self._line_cap_snapshots[snapshot_name]
