"""Class implementation for line round dot setting interface.
"""

from typing import Dict
from typing import Optional

from apysc.display.line_round_dot_setting import LineRoundDotSetting
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class LineRoundDotSettingInterface(VariableNameInterface, RevertInterface):

    _line_round_dot_setting: Optional[LineRoundDotSetting]

    def _initialize_line_round_dot_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_round_dot_setting if it is not
        initialized yet.
        """
        if hasattr(self, '_line_round_dot_setting'):
            return
        self._line_round_dot_setting = None

    @property
    def line_round_dot_setting(self) -> Optional[LineRoundDotSetting]:
        """
        Get this instance's line round dot setting.

        Parameters
        ----------
        line_round_dot_setting : LineRoundDotSetting or None
            LKine round dot setting.
        """
        self._initialize_line_round_dot_setting_if_not_initialized()
        return self._line_round_dot_setting

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass
