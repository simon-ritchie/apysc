"""Class implementation for line color interface.
"""

from typing import Dict
from typing import Union

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class LineColorInterface(VariableNameInterface, RevertInterface):

    _line_color: ap.String

    @property
    def line_color(self) -> ap.String:
        """
        Get this instance's line color.

        Returns
        -------
        line_color : String
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, blank string will be returned.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_color', locals_=locals(),
                module_name=__name__, class_=LineColorInterface):
            from apysc._type import value_util
            self._initialize_line_color_if_not_initialized()
            line_color: ap.String = value_util.get_copy(
                value=self._line_color)
            return line_color

    @line_color.setter
    def line_color(self, value: ap.String) -> None:
        """
        Update this instance's line color.

        Parameters
        ----------
        value : str
            Line color to set.
        """
        with ap.DebugInfo(
                callable_='line_color', locals_=locals(),
                module_name=__name__, class_=LineColorInterface):
            self._update_line_color_and_skip_appending_exp(value=value)
            self._append_line_color_update_expression()

    def _append_line_color_update_expression(self) -> None:
        """
        Append line color updating expression.
        """
        with ap.DebugInfo(
                callable_=self._append_line_color_update_expression,
                locals_=locals(),
                module_name=__name__, class_=LineColorInterface):
            expression: str = (
                f'{self.variable_name}.stroke("{self.line_color}");'
            )
            ap.append_js_expression(expression=expression)

    def _set_initial_line_color_if_not_blank(
            self, line_color: Union[str, ap.String]) -> None:
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
            line_color = ap.String(line_color)
        self._update_line_color_and_skip_appending_exp(value=line_color)

    def _update_line_color_and_skip_appending_exp(
            self, value: ap.String) -> None:
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
        self._line_color = ap.String('')

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
