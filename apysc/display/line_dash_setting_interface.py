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

    @property
    def line_dash_setting(self) -> Optional[LineDashSetting]:
        """
        Get this interface's line dash setting.

        Returns
        -------
        line_dash_setting : LineDashSetting or None
            Line dash setting.
        """
        self._initialize_line_dash_setting_if_not_initialized()
        return self._line_dash_setting

    def _update_line_dash_setting_and_skip_appending_exp(
            self, value: Optional[LineDashSetting]) -> None:
        """
        Update line dash setting and skip appending expression to file.

        Parameters
        ----------
        value : LineDashSetting or None
            Line dash setting to set.
        """
        if value is not None and not isinstance(value, LineDashSetting):
            raise TypeError(
                'Not supported line_dash_setting type specified: '
                f'{type(value)}'
                '\nAcceptable ones are: LineDashSetting or None.')
        self._line_dash_setting = value

    def _append_line_dash_setting_update_expression(self) -> None:
        """
        Append line dash setting updating expression to file.
        """
        from apysc.expression import expression_file_util
        if self._line_dash_setting is None:
            setting_str: str = '""'
        else:
            setting_str = (
                f'String({self._line_dash_setting.dash_size.variable_name})'
                ' + " " + '
                f'String({self._line_dash_setting.space_size.variable_name})'
            )
        expression: str = (
            f'{self.variable_name}.css("stroke-dasharray", {setting_str});'
        )
        expression_file_util.append_js_expression(expression=expression)

    def _make_snapshot(self, snapshot_name: str) -> None:
        pass

    def _revert(self, snapshot_name: str) -> None:
        pass
