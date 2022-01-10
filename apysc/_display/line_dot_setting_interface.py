"""Class implementation for line dot setting interface.
"""

from typing import Dict
from typing import Optional

from apysc._display.line_dot_setting import LineDotSetting
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class LineDotSettingInterface(VariableNameInterface, RevertInterface):

    _line_dot_setting: Optional[LineDotSetting]

    def _initialize_line_dot_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_dot_setting attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_dot_setting'):
            return
        self._line_dot_setting = None

    @property
    def line_dot_setting(self) -> Optional[LineDotSetting]:
        """
        Get this instance's line dot setting.

        Returns
        -------
        line_dot_setting : LineDotSetting or None
            Lien dot setting.

        References
        ----------
        - Graphics line_dot_setting interface document
            - https://bit.ly/3ni8rIS

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dot_setting = ap.LineDotSetting(dot_size=5)
        >>> line.line_dot_setting.dot_size
        Int(5)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_dot_setting', locals_=locals(),
                module_name=__name__, class_=LineDotSettingInterface):
            self._initialize_line_dot_setting_if_not_initialized()
            return self._line_dot_setting

    @line_dot_setting.setter
    def line_dot_setting(self, value: Optional[LineDotSetting]) -> None:
        """
        Set line dot setting.

        Parameters
        ----------
        value : LineDotSetting or None
            Line dot setting to set.

        References
        ----------
        - Graphics line_dot_setting interface document
            - https://bit.ly/3ni8rIS
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=LineDotSettingInterface, locals_=locals(),
                module_name=__name__, class_=LineDotSettingInterface):
            from apysc._validation import display_validation
            self._update_line_dot_setting_and_skip_appending_exp(value=value)
            self._append_line_dot_setting_update_expression()
            display_validation.validate_multiple_line_settings_isnt_set(
                any_instance=self)

    def _update_line_dot_setting_and_skip_appending_exp(
            self, *, value: Optional[LineDotSetting]) -> None:
        """
        Update line dot setting and skip appending expression.

        Parameters
        ----------
        value : LineDotSetting or None
            Line dot setting to set.
        """
        if value is not None and not isinstance(value, LineDotSetting):
            raise TypeError(
                'Not supported line_dot_setting type specified: '
                f'{type(value)}'
                '\nAcceptable ones are: LineDotSetting or None.')
        self._line_dot_setting = value

    def _append_line_dot_setting_update_expression(self) -> None:
        """
        Append line dot setting updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_line_dot_setting_update_expression,
                locals_=locals(),
                module_name=__name__, class_=LineDotSettingInterface):
            if self._line_dot_setting is None:
                setting_str: str = '""'
            else:
                setting_str = self._line_dot_setting.dot_size.variable_name
            expression: str = (
                f'{self.variable_name}.css("stroke-dasharray", {setting_str});'
            )
            ap.append_js_expression(expression=expression)

    _line_dot_setting_snapshots: Dict[str, Optional[LineDotSetting]]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_dot_setting_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_dot_setting_snapshots',
            value=self._line_dot_setting, snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._line_dot_setting = self._line_dot_setting_snapshots[
            snapshot_name]
