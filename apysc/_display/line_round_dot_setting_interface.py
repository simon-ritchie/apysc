"""Class implementation for line round dot setting interface.
"""

from typing import Dict
from typing import Optional

from apysc._display.line_cap_interface import LineCapInterface
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._display.line_thickness_interface import LineThicknessInterface


class LineRoundDotSettingInterface(LineCapInterface, LineThicknessInterface):

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

        Returns
        -------
        line_round_dot_setting : LineRoundDotSetting or None
            Line round dot setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_round_dot_setting', locals_=locals(),
                module_name=__name__, class_=LineRoundDotSettingInterface):
            self._initialize_line_round_dot_setting_if_not_initialized()
            return self._line_round_dot_setting

    @line_round_dot_setting.setter
    def line_round_dot_setting(
            self, value: Optional[LineRoundDotSetting]) -> None:
        """
        Set line round dot setting.

        Notes
        -----
        This property updating will affect line cap and
        thickness settings.

        Parameters
        ----------
        value : LineRoundDotSetting or None
            Line round setting to set.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_round_dot_setting', locals_=locals(),
                module_name=__name__, class_=LineRoundDotSettingInterface):
            from apysc._validation import display_validation
            self._update_line_round_dot_setting_and_skip_appending_exp(
                value=value)
            if value is not None:
                self.line_cap = ap.LineCaps.ROUND
                self.line_thickness = value.round_size
            else:
                self.line_cap = ap.LineCaps.BUTT
            self._append_line_round_dot_setting_update_expression()
            display_validation.validate_multiple_line_settings_isnt_set(
                any_instance=self)

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

    def _append_line_round_dot_setting_update_expression(self) -> None:
        """
        Append line round dot setting updating expression to file.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_line_round_dot_setting_update_expression,  # noqa
                locals_=locals(),
                module_name=__name__, class_=LineRoundDotSettingInterface):
            import apysc as ap
            if self._line_round_dot_setting is None:
                setting_str: str = '""'
            else:
                round_size_name: str = \
                    self._line_round_dot_setting.round_size.variable_name
                space_size_name: str = \
                    self._line_round_dot_setting.space_size.variable_name
                setting_str = (
                    f'"1 " + String({round_size_name} + {space_size_name})'
                )
            expression: str = (
                f'{self.variable_name}.css("stroke-dasharray", {setting_str});'
            )
            ap.append_js_expression(expression=expression)

    _line_round_dot_setting_snapshots: Dict[
        str, Optional[LineRoundDotSetting]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_line_round_dot_setting_snapshots'):
            self._line_round_dot_setting_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_line_round_dot_setting_if_not_initialized()
        self._line_round_dot_setting_snapshots[snapshot_name] = \
            self._line_round_dot_setting

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
        self._line_round_dot_setting = self._line_round_dot_setting_snapshots[
            snapshot_name]
