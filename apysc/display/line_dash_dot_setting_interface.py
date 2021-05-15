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
                'Not supported line_dash_dot_setting type specified:'
                f'{type(value)}'
                '\nAcceptable ones are: LineDashDotSetting or None.')
        self._line_dash_dot_setting = value

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass
