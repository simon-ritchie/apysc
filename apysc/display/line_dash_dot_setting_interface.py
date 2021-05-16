"""Class implementation for line dash dot setting interface.
"""

from typing import Dict
from typing import Optional

from apysc.display.line_dash_dot_setting import LineDashDotSetting
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class LineDashDotSettingInterface(VariableNameInterface, RevertInterface):

    _line_dash_dot_setting: Optional[LineDashDotSetting]

    def _initialize_line_dash_dot_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_dash_dot_setting attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_dash_dot_setting'):
            return
        self._line_dash_dot_setting = None

    @property
    def line_dash_dot_setting(self) -> Optional[LineDashDotSetting]:
        """
        Get current dash dot (1-dot chain) setting.

        Returns
        -------
        line_dash_dot_setting : LineDashDotSetting or None
            Dash dot (1-dot chain) setting.
        """
        self._initialize_line_dash_dot_setting_if_not_initialized()
        return self._line_dash_dot_setting

    @line_dash_dot_setting.setter
    def line_dash_dot_setting(
            self, value: Optional[LineDashDotSetting]) -> None:
        """
        Set line dash dot (1-dot chain) setting.

        Parameters
        ----------
        value : LineDashDotSetting or None
            Line dash dot (1-dot chain) setting to set.
        """
        from apysc.validation import display_validation
        self._update_line_dash_dot_setting_and_skip_appending_exp(value=value)
        self._append_line_dash_dot_setting_update_expression()
        display_validation.validate_multiple_line_settings_isnt_set(
            any_instance=self)

    def _update_line_dash_dot_setting_and_skip_appending_exp(
            self, value: Optional[LineDashDotSetting]) -> None:
        """
        Update line dash dot (1-dot chain) setting and skip
        appending expression to file.

        Parameters
        ----------
        value : LineDashDotSetting or None
            Line dash dot (1-dot chain) setting to set.
        """
        if value is not None and not isinstance(value, LineDashDotSetting):
            raise TypeError(
                'Not supported line_dash_dot_setting type specified: '
                f'{type(value)}'
                '\nAcceptable ones are: LineDashDotSetting or None.')
        self._line_dash_dot_setting = value

    def _append_line_dash_dot_setting_update_expression(self) -> None:
        """
        Append line dash dot setting updating expression to file.
        """
        from apysc.expression import expression_file_util
        if self._line_dash_dot_setting is None:
            setting_str: str = '""'
        else:
            dot_size_name: str = \
                self._line_dash_dot_setting.dot_size.variable_name
            dash_size_name: str = \
                self._line_dash_dot_setting.dash_size.variable_name
            space_size_name: str = \
                self._line_dash_dot_setting.space_size.variable_name
            setting_str = (
                f'String({dot_size_name}) + " " + '
                f'String({space_size_name}) + " " + '
                f'String({dash_size_name}) + " " + '
                f'String({space_size_name})'
            )
        expression: str = (
            f'{self.variable_name}.css("stroke-dasharray", {setting_str});'
        )
        expression_file_util.append_js_expression(expression=expression)

    _line_dash_dot_setting_snapshots: Dict[str, Optional[LineDashDotSetting]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_line_dash_dot_setting_snapshots'):
            self._line_dash_dot_setting_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_line_dash_dot_setting_if_not_initialized()
        self._line_dash_dot_setting_snapshots[snapshot_name] = \
            self._line_dash_dot_setting

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
        self._line_dash_dot_setting = self._line_dash_dot_setting_snapshots[
            snapshot_name]
