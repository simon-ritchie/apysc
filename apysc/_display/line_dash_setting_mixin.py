"""Class implementation for line dash setting mix-in.
"""

from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._display.line_dash_setting import LineDashSetting
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class LineDashSettingMixIn(VariableNameMixIn, RevertMixIn):

    _line_dash_setting: Optional[LineDashSetting]

    @final
    def _initialize_line_dash_setting_if_not_initialized(self) -> None:
        """
        Initialize the _line_dash_setting attribute if this
        interface does not initialize it yet.
        """
        if hasattr(self, "_line_dash_setting"):
            return
        self._line_dash_setting = None

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_dash_setting(self) -> Optional[LineDashSetting]:
        """
        Get a current line dash setting.

        Returns
        -------
        line_dash_setting : LineDashSetting or None
            Line dash setting.

        References
        ----------
        - GraphicsBase line_dash_setting interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_dash_setting.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color="#fff", thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50
        ... )
        >>> line.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)
        >>> line.line_dash_setting.dash_size
        Int(5)

        >>> line.line_dash_setting.space_size
        Int(2)
        """
        self._initialize_line_dash_setting_if_not_initialized()
        return self._line_dash_setting

    @line_dash_setting.setter
    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    @arg_validation_decos.is_line_dash_setting(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def line_dash_setting(self, value: Optional[LineDashSetting]) -> None:
        """
        Set line dash setting.

        Parameters
        ----------
        value : LineDashSetting or None
            Line dash setting to set.

        References
        ----------
        - GraphicsBase line_dash_setting interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_dash_setting.html  # noqa
        """
        self._update_line_dash_setting_and_skip_appending_exp(value=value)
        self._append_line_dash_setting_update_expression()

    @final
    def _update_line_dash_setting_and_skip_appending_exp(
        self, *, value: Optional[LineDashSetting]
    ) -> None:
        """
        Update line dash setting and skip appending expression.

        Parameters
        ----------
        value : LineDashSetting or None
            Line dash setting to set.
        """
        if value is not None and not isinstance(value, LineDashSetting):
            raise TypeError(
                "Not supported line_dash_setting type specified: "
                f"{type(value)}"
                "\nAcceptable ones are: LineDashSetting or None."
            )
        self._line_dash_setting = value

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_dash_setting_update_expression(self) -> None:
        """
        Append line dash setting updating expression.
        """
        import apysc as ap

        if self._line_dash_setting is None:
            setting_str: str = '""'
        else:
            setting_str = (
                "String("
                f"{self._line_dash_setting.dash_size.variable_name})"
                ' + " " + '
                "String("
                f"{self._line_dash_setting.space_size.variable_name})"
            )
        expression: str = (
            f'{self.variable_name}.css("stroke-dasharray", {setting_str});'
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def delete_line_dash_setting(self) -> None:
        """
        Delete a current line dash setting.

        References
        ----------
        - GraphicsBase line_dash_setting interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_dash_setting.html  # noqa
        """
        self._update_line_dash_setting_and_skip_appending_exp(value=None)
        self._append_line_dash_setting_update_expression()

    _line_dash_setting_snapshots: Dict[str, Optional[LineDashSetting]]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_dash_setting_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_dash_setting_snapshots",
            value=self._line_dash_setting,
            snapshot_name=snapshot_name,
        )

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
        self._line_dash_setting = self._line_dash_setting_snapshots[snapshot_name]
