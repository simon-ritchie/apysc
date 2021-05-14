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

    def _update_line_round_dot_setting_and_skip_appending_exp(
            self, value: Optional[LineRoundDotSetting]) -> None:
        """
        Update line round setting and skip appending expression to file.

        Parameters
        ----------
        value : LineRoundSetting or None
            Line round dot setting to set.
        """
        if value is not None and not isinstance(value, LineRoundDotSetting):
            raise TypeError(
                'Not supported line_round_dot_setting type specified: '
                f'{type(value)}'
                '\nAcceptable ones are: LineRoundDotSetting or None.')
        self._line_round_dot_setting = value

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass
