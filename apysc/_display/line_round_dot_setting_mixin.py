"""Class implementation for the line round-dot setting
interface.
"""

from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._display.line_cap_mixin import LineCapMixIn
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._display.line_thickness_mixin import LineThicknessMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class LineRoundDotSettingMixIn(LineCapMixIn, LineThicknessMixIn):

    _line_round_dot_setting: Optional[LineRoundDotSetting]

    @final
    def _initialize_line_round_dot_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_round_dot_setting if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_line_round_dot_setting"):
            return
        self._line_round_dot_setting = None

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_round_dot_setting(self) -> Optional[LineRoundDotSetting]:
        """
        Get this instance's line round dot setting.

        Returns
        -------
        line_round_dot_setting : LineRoundDotSetting or None
            Line round dot setting.

        References
        ----------
        - GraphicsBase line_round_dot interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_round_dot_setting.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color="#fff", thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50
        ... )
        >>> line.line_round_dot_setting = ap.LineRoundDotSetting(
        ...     round_size=10, space_size=5
        ... )
        >>> line.line_round_dot_setting.round_size
        Int(10)

        >>> line.line_round_dot_setting.space_size
        Int(5)
        """
        self._initialize_line_round_dot_setting_if_not_initialized()
        return self._line_round_dot_setting

    @line_round_dot_setting.setter
    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    @arg_validation_decos.is_line_round_dot_setting(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def line_round_dot_setting(self, value: Optional[LineRoundDotSetting]) -> None:
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

        self._update_line_round_dot_setting_and_skip_appending_exp(value=value)
        if value is not None:
            self.line_cap = ap.LineCaps.ROUND
            self.line_thickness = value.round_size
        else:
            self.line_cap = ap.LineCaps.BUTT
        self._append_line_round_dot_setting_update_expression()

    @final
    def _update_line_round_dot_setting_and_skip_appending_exp(
        self, *, value: Optional[LineRoundDotSetting]
    ) -> None:
        """
        Update line round setting and skip appending expression.

        Parameters
        ----------
        value : LineRoundSetting or None
            Line round-dot settings to set.
        """
        if value is not None and not isinstance(value, LineRoundDotSetting):
            raise TypeError(
                "Not supported line_round_dot_setting type specified: "
                f"{type(value)}"
                "\nAcceptable ones are: LineRoundDotSetting or None."
            )
        self._line_round_dot_setting = value

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_round_dot_setting_update_expression(self) -> None:
        """
        Append line round dot setting updating expression.
        """
        import apysc as ap

        if self._line_round_dot_setting is None:
            setting_str: str = '""'
        else:
            round_size_name: str = self._line_round_dot_setting.round_size.variable_name
            space_size_name: str = self._line_round_dot_setting.space_size.variable_name
            setting_str = f'"1 " + String({round_size_name} + {space_size_name})'
        expression: str = (
            f'{self.variable_name}.css("stroke-dasharray", {setting_str});'
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def delete_line_round_dot_setting(self) -> None:
        """
        Delete a current line-round dot setting.

        References
        ----------
        - GraphicsBase line_round_dot interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_round_dot_setting.html  # noqa
        """
        import apysc as ap

        self._update_line_round_dot_setting_and_skip_appending_exp(value=None)
        self.line_cap = ap.LineCaps.BUTT
        self._append_line_round_dot_setting_update_expression()

    _line_round_dot_setting_snapshots: Dict[str, Optional[LineRoundDotSetting]]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_round_dot_setting_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_round_dot_setting_snapshots",
            value=self._line_round_dot_setting,
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
        self._line_round_dot_setting = self._line_round_dot_setting_snapshots[
            snapshot_name
        ]
