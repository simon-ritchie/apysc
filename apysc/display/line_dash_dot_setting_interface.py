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

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass
