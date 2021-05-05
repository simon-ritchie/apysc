"""Class implementation for fill color interface.
"""

from typing import Dict
from typing import Union

from apysc import String
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class FillColorInterface(VariableNameInterface, RevertInterface):

    _fill_color: String

    @property
    def fill_color(self) -> String:
        """
        Get this instance's fill color.

        Returns
        -------
        fill_color : String
            Current fill color (hexadecimal string, e.g., '#00aaff').
            If not be set, None will be returned.
        """
        from apysc.type import value_util
        self._initialize_fill_color_if_not_initialized()
        fill_color: String = value_util.get_copy(value=self._fill_color)
        return fill_color

    @fill_color.setter
    def fill_color(self, value: String) -> None:
        """
        Update this instance's fill color.

        Parameters
        ----------
        value : String
            Fill color to set.
        """
        self._update_fill_color_and_skip_appending_exp(value=value)
        self._append_fill_color_update_expression()

    def _append_fill_color_update_expression(self) -> None:
        """
        Append fill color updating expression.
        """
        from apysc.expression import expression_file_util
        expression: str = (
            f'{self.variable_name}.fill("{self.fill_color}");'
        )
        expression_file_util.append_js_expression(expression=expression)

    def _set_initial_fill_color_if_not_blank(
            self, fill_color: Union[str, String]) -> None:
        """
        Set initial fill color value if specified value is not
        blank string.

        Parameters
        ----------
        fill_color : str or String
            Fill color (hexadecimal string, e.g., '#00aaff').
        """
        if fill_color == '':
            return
        if isinstance(fill_color, str):
            fill_color = String(fill_color)
        self._update_fill_color_and_skip_appending_exp(value=fill_color)

    def _update_fill_color_and_skip_appending_exp(
            self, value: String) -> None:
        """
        Update fill color and skip appending expression to file.

        Parameters
        ----------
        value : String
            Fill color to set.
        """
        from apysc.color import color_util
        value = color_util.complement_hex_color(
            hex_color_code=value)
        self._initialize_fill_color_if_not_initialized()
        self._fill_color.value = value

    def _initialize_fill_color_if_not_initialized(self) -> None:
        """
        Initialize fill_color attribute if that value is not
        instantiated yet.
        """
        if hasattr(self, '_fill_color'):
            return
        self._fill_color = String('')

    _fill_color_snapshots: Dict[str, str]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_fill_color_snapshots'):
            self._fill_color_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_fill_color_if_not_initialized()
        self._fill_color_snapshots[snapshot_name] = self._fill_color._value

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
        self._fill_color._value = self._fill_color_snapshots[snapshot_name]
