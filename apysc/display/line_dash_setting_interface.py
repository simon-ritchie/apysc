"""Class implementation for line dash setting interface.
"""

from typing import Dict
from typing import Optional

from apysc.display.line_dash_setting import LineDashSetting
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class LineDashSettingInterface(VariableNameInterface, RevertInterface):

    _line_dash_setting: Optional[LineDashSetting]

    def _initialize_line_dash_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_dash_setting if it is not
        initialized yet.
        """
        if hasattr(self, '_line_dash_setting'):
            return
        self._line_dash_setting = None

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass
