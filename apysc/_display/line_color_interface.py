"""Class implementation for line color interface.
"""

from typing import Dict
from typing import Union

from apysc import String
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class LineColorInterface(VariableNameInterface, RevertInterface):

    _line_color: String

    @property
    def line_color(self) -> String:
        """
        Get this instance's line color.

        Returns
        -------
        line_color : String
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, blank string will be returned.
        """
        from apysc._type import value_util
        self._initialize_line_color_if_not_initialized()
        line_color: String = value_util.get_copy(value=self._line_color)
        return line_color

    @line_color.setter
    def line_color(self, value: String) -> None:
        """
        Update this instance's line color.

        Parameters
        ----------
        value : str
            Line color to set.
        """
        self._update_line_color_and_skip_appending_exp(value=value)
        self._append_line_color_update_expression()

    def _append_line_color_update_expression(self) -> None:
        """
        Append line color updating expression.
        """
        from apysc import append_js_expression
        expression: str = (
            f'{self.variable_name}.stroke("{self.line_color}");'
        )
        append_js_expression(expression=expression)

    def _set_initial_line_color_if_not_blank(
            self, line_color: Union[str, String]) -> None:
        """
        Set initial line color value if specified value is not
        blank string.

        Parameters
        ----------
        line_color : str or String
            Line color (hexadecimal string, e.g., '#00aaff').
        """
        if line_color == '':
            return
        if isinstance(line_color, str):
            line_color = String(line_color)
        self._update_line_color_and_skip_appending_exp(value=line_color)

    def _update_line_color_and_skip_appending_exp(
            self, value: String) -> None:
        """
        Update line color and skip appending expression to file.

        Parameters
        ----------
        value : String
            Line color to set.
        """
        from apysc._color import color_util
        value = color_util.complement_hex_color(
            hex_color_code=value)
        self._initialize_line_color_if_not_initialized()
        self._line_color = value

    def _initialize_line_color_if_not_initialized(self) -> None:
        """
        Initialize line_color attribute if that value is not
        initialized yet.
        """
        if hasattr(self, '_line_color'):
            return
        self._line_color = String('')

    _line_color_snapshots: Dict[str, str]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_line_color_snapshots'):
            self._line_color_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_line_color_if_not_initialized()
        self._line_color_snapshots[snapshot_name] = self._line_color._value

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
        self._line_color._value = self._line_color_snapshots[snapshot_name]
