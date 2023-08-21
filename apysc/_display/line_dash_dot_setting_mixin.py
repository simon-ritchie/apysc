"""Class implementation for line dash-dot setting mix-in.
"""

from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


class LineDashDotSettingMixIn(VariableNameMixIn, RevertMixIn):
    _line_dash_dot_setting: Optional[LineDashDotSetting]

    @final
    def _initialize_line_dash_dot_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_dash_dot_setting attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_line_dash_dot_setting"):
            return
        self._line_dash_dot_setting = None

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_dash_dot_setting(self) -> Optional[LineDashDotSetting]:
        """
        Get a current dash-dot (1-dot chain) setting.

        Returns
        -------
        line_dash_dot_setting : LineDashDotSetting or None
            Dash-dot (1-dot chain) setting.

        References
        ----------
        - GraphicsBase line_dash_dot_setting interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_dash_dot_setting.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50
        ... )
        >>> line.line_dash_dot_setting = ap.LineDashDotSetting(
        ...     dot_size=2, dash_size=5, space_size=3
        ... )
        >>> line.line_dash_dot_setting.dot_size
        Int(2)

        >>> line.line_dash_dot_setting.dash_size
        Int(5)

        >>> line.line_dash_dot_setting.space_size
        Int(3)
        """
        self._initialize_line_dash_dot_setting_if_not_initialized()
        return self._line_dash_dot_setting

    @line_dash_dot_setting.setter
    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    @arg_validation_decos.is_line_dash_dot_setting(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def line_dash_dot_setting(self, value: Optional[LineDashDotSetting]) -> None:
        """
        Set line dash-dot (1-dot chain) setting.

        Parameters
        ----------
        value : LineDashDotSetting or None
            Line dash-dot (1-dot chain) setting to set.

        References
        ----------
        - GraphicsBase line_dash_dot_setting interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_dash_dot_setting.html  # noqa
        """
        self._update_line_dash_dot_setting_and_skip_appending_exp(value=value)
        self._append_line_dash_dot_setting_update_expression()

    @final
    def _update_line_dash_dot_setting_and_skip_appending_exp(
        self, *, value: Optional[LineDashDotSetting]
    ) -> None:
        """
        Update line dash-dot (1-dot chain) setting and skip
        appending expression.

        Parameters
        ----------
        value : LineDashDotSetting or None
            Line dash-dot (1-dot chain) setting to set.
        """
        if value is not None and not isinstance(value, LineDashDotSetting):
            raise TypeError(
                "Not supported line_dash_dot_setting type specified: "
                f"{type(value)}"
                "\nAcceptable ones are: LineDashDotSetting or None."
            )
        self._line_dash_dot_setting = value

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_dash_dot_setting_update_expression(self) -> None:
        """
        Append line dash-dot setting updating expression.
        """
        from apysc._expression import expression_data_util

        if self._line_dash_dot_setting is None:
            setting_str: str = '""'
        else:
            dot_size_name: str = self._line_dash_dot_setting.dot_size.variable_name
            dash_size_name: str = self._line_dash_dot_setting.dash_size.variable_name
            space_size_name: str = self._line_dash_dot_setting.space_size.variable_name
            setting_str = (
                f'String({dot_size_name}) + " " + '
                f'String({space_size_name}) + " " + '
                f'String({dash_size_name}) + " " + '
                f"String({space_size_name})"
            )
        expression: str = (
            f'{self.variable_name}.css("stroke-dasharray", {setting_str});'
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def delete_line_dash_dot_setting(self) -> None:
        """
        Delete a current line dash-dot (1-dot chain) setting.

        References
        ----------
        - GraphicsBase line_dash_dot_setting interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_dash_dot_setting.html  # noqa
        """
        self._update_line_dash_dot_setting_and_skip_appending_exp(value=None)
        self._append_line_dash_dot_setting_update_expression()

    _line_dash_dot_setting_snapshots: Optional[
        Dict[str, Optional[LineDashDotSetting]]
    ] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_dash_dot_setting_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_dash_dot_setting_snapshots",
            value=self._line_dash_dot_setting,
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
        self._initialize_line_dash_dot_setting_if_not_initialized()
        self._line_dash_dot_setting = self._get_snapshot_val_if_exists(
            current_value=self._line_dash_dot_setting,
            snapshot_dict=self._line_dash_dot_setting_snapshots,
            snapshot_name=snapshot_name,
        )
