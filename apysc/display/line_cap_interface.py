"""Class implementation for line cap interface.
"""

from typing import Any, Dict
from typing import Union

from apysc import String
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface
from apysc.display.line_caps import LineCaps


class LineCapInterface(VariableNameInterface, RevertInterface):

    _line_cap: String

    def _initialize_line_cap_if_not_initialized(self) -> None:
        """
        Inilialize _line_cap attribute if that it is not
        initialized yet.
        """
        if hasattr(self, '_line_cap'):
            return
        self._line_cap = String(LineCaps.BUTT.value)

    @property
    def line_cap(self) -> Any:
        """
        Get this instance's line cap style setting.

        Returns
        -------
        line_cap : String
            Line cap style setting.
        """
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
        from apysc.validation.display_validation import validate_line_cap
        if not isinstance(value, (String, LineCaps)):
            raise TypeError(
                'Not supported line_cap type specified: '
                f'{type(value)}'
                '\nAcceptable ones: String or LineCaps.')
        validate_line_cap(cap=value)
        if isinstance(value, String):
            self._line_cap = value._copy()
        else:
            self._line_cap = String(value.value)
        self._append_line_cap_update_expression()

    def _append_line_cap_update_expression(self) -> None:
        """
        Append line cap updating expression to file.
        """
        from apysc.type import value_util
        from apysc.expression import expression_file_util
        cap_name: str = value_util.get_value_str_for_expression(
            value=self._line_cap)
        expression: str = (
            f'{self.variable_name}.attr({{"stroke-linecap": {cap_name}}});'
        )
        expression_file_util.append_js_expression(expression=expression)

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
