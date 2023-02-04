"""Class implementation for line style-related mix-in.
"""

from typing import Dict
from typing import Optional
from typing import TypeVar
from typing import Union

from typing_extensions import final

from apysc._display.line_caps import LineCaps
from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_dot_setting import LineDotSetting
from apysc._display.line_joints import LineJoints
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.string import String
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos

StrOrString = TypeVar("StrOrString", str, String)


class LineStyleMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameMixIn,
    RevertMixIn,
    VariableNameSuffixMixIn,
):

    _line_color: String
    _line_thickness: Int
    _line_alpha: Number
    _line_cap: String
    _line_joints: String
    _line_dot_setting: Optional[LineDotSetting]
    _line_dash_setting: Optional[LineDashSetting]
    _line_round_dot_setting: Optional[LineRoundDotSetting]
    _line_dash_dot_setting: Optional[LineDashDotSetting]

    @final
    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @arg_validation_decos.is_num(arg_position_index=3)
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=3)
    @arg_validation_decos.is_line_cap(arg_position_index=4, optional=True)
    @arg_validation_decos.is_line_joints(arg_position_index=5, optional=True)
    @arg_validation_decos.is_line_dot_setting(arg_position_index=6)
    @arg_validation_decos.is_line_dash_setting(arg_position_index=7)
    @arg_validation_decos.is_line_round_dot_setting(arg_position_index=8)
    @arg_validation_decos.is_line_dash_dot_setting(arg_position_index=9)
    @add_debug_info_setting(module_name=__name__)
    def line_style(
        self,
        *,
        color: StrOrString,
        thickness: Union[int, Int] = 1,
        alpha: Union[float, Number] = 1.0,
        cap: Optional[LineCaps] = None,
        joints: Optional[LineJoints] = None,
        dot_setting: Optional[LineDotSetting] = None,
        dash_setting: Optional[LineDashSetting] = None,
        round_dot_setting: Optional[LineRoundDotSetting] = None,
        dash_dot_setting: Optional[LineDashDotSetting] = None
    ) -> None:
        """
        Set line style values.

        Parameters
        ----------
        color : String or str
            Hexadecimal color string. e.g., '#00aaff'
        thickness : Int or int, default 1
            Line thickness (minimum value is 1).
        alpha : float or Number, default 1.0
            Line color opacity (0.0 to 1.0).
        cap : LineCaps or None, default None
            Line cap (edge style) setting. The not line-related
            graphics (e.g., Rectangle ignores this, conversely
            used by Polyline) ignore this setting.
        joints : LineJoints or None, default None
            Line vertices (joints) style setting. The not
            polyline-related graphics (e.g., Rectangle ignores
            this, conversely used by Polyline) ignore this setting.
        dot_setting : LineDotSetting or None, default None
            Dot setting. If this is specified, it makes a line dotted.
        dash_setting : LineDashSetting or None, default None
            Dash setting. If this is specified, it makes a line dashed.
        round_dot_setting : LineRoundDotSetting or None, default None
            Round dot setting. If this is specified, it makes a line
            round dotted. Notes: since this style uses a cap setting,
            it overrides cap and line thickness settings. And it
            increases the amount of line size.
            If you want to adjust to the same width of a normal line
            when using move_to and line_to interfaces,
            add half-round size to start x-coordinate and subtract
            from end e-coordinate.
            e.g.,
            `this.move_to(x + round_size / 2, y)`,
            `this.line_to(x - round_size / 2, y)`
        dash_dot_setting : LineDashDotSetting or None, default None
            Dash-dot (1-dot chain) setting. If this is specified,
            it makes a line 1-dot chained.

        References
        ----------
        - Graphics line_style interface
            - https://simon-ritchie.github.io/apysc/en/graphics_line_style.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color="#fff", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
        ... )
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50
        ... )
        >>> line.line_color
        String('#ffffff')

        >>> line.line_thickness
        Int(5)

        >>> line.line_alpha
        Number(0.5)

        >>> line.line_cap
        String('round')
        """
        from apysc._color import color_util

        self._initialize_line_color_if_not_initialized()
        self._initialize_line_thickness_if_not_initialized()
        self._initialize_line_alpha_if_not_initialized()
        suffix: str

        if color != "":
            color = color_util.complement_hex_color(hex_color_code=color)
        self._line_color.value = color
        self._line_thickness = self._convert_line_thickness_to_apysc_int(
            thickness=thickness
        )
        self._line_alpha = self._convert_line_alpha_to_number(alpha=alpha)
        self._set_line_cap(cap=cap)
        self._set_line_joints(joints=joints)
        self._line_dot_setting = dot_setting
        self._line_dash_setting = dash_setting
        self._line_round_dot_setting = round_dot_setting
        self._line_dash_dot_setting = dash_dot_setting

    @final
    def _convert_line_thickness_to_apysc_int(
        self, *, thickness: Union[int, Int]
    ) -> Int:
        """
        Convert a line thickness value to an Int value.

        Parameters
        ----------
        thickness : Union[int, Int]
            A line thickness value.

        Returns
        -------
        thickness_ : Int
            Converted line thickness value.
        """
        import apysc as ap

        if isinstance(thickness, ap.Int):
            thickness_: ap.Int = thickness._copy()
        else:
            suffix: str = self._get_attr_or_variable_name_suffix(
                value_identifier="line_thickness"
            )
            thickness_ = ap.Int(thickness, variable_name_suffix=suffix)
        return thickness_

    @final
    @add_debug_info_setting(module_name=__name__)
    def _convert_line_alpha_to_number(self, *, alpha: Union[float, Number]) -> Number:
        """
        Convert a line alpha value to a Number value.

        Parameters
        ----------
        alpha : Union[float, Number]
            A specified line alpha value.

        Returns
        -------
        alpha_ : Number
            Converted line alpha value.
        """
        import apysc as ap

        if isinstance(alpha, ap.Number):
            alpha_: ap.Number = alpha._copy()
        else:
            suffix = self._get_attr_or_variable_name_suffix(
                value_identifier="line_alpha"
            )
            alpha_ = ap.Number(alpha, variable_name_suffix=suffix)
        return alpha_

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_line_joints(self, *, joints: Optional[LineJoints]) -> None:
        """
        Set line joints setting to attribute.

        Parameters
        ----------
        joints : LineJoints or None, default None
            Line vertices (joints) style setting.
        """
        import apysc as ap

        if joints is None:
            joints = LineJoints.MITER
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="line_joints"
        )
        self._line_joints = ap.String(joints.value, variable_name_suffix=suffix)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_line_cap(self, *, cap: Optional[LineCaps]) -> None:
        """
        Set line cap setting to attribute.

        Parameters
        ----------
        cap : LineCaps or None, default None
            Line cap (edge style) setting.
        """
        import apysc as ap

        if cap is None:
            cap = LineCaps.BUTT
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="line_cap"
        )
        self._line_cap = ap.String(cap.value, variable_name_suffix=suffix)

    @final
    def _initialize_line_color_if_not_initialized(self) -> None:
        """
        Initialize _line_color attribute if this interface does
        not initialize it yet.
        """
        if hasattr(self, "_line_color"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="line_color"
        )
        self._line_color = String(
            "",
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @final
    def _initialize_line_thickness_if_not_initialized(self) -> None:
        """
        Initialize _line_thickness attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, "_line_thickness"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="line_thickness"
        )
        self._line_thickness = Int(
            1,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @final
    def _initialize_line_alpha_if_not_initialized(self) -> None:
        """
        Initialize _line_alpha attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_line_alpha"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="line_alpha"
        )
        self._line_alpha = Number(
            1.0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @final
    def _initialize_line_cap_if_not_initialized(self) -> None:
        """
        Initialize _line_cap attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_line_cap"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="line_cap"
        )
        self._line_cap = String(
            LineCaps.BUTT.value,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @final
    def _initialize_line_joints_if_not_initialized(self) -> None:
        """
        Initialize _line_joints attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_line_joints"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="line_joints"
        )
        self._line_joints = String(
            LineJoints.MITER.value,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @final
    def _initialize_line_dot_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_dot_setting attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_line_dot_setting"):
            return
        self._line_dot_setting = None

    @final
    def _initialize_line_dash_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_dash_setting attribute if this
        interface does not initialize it yet.
        """
        if hasattr(self, "_line_dash_setting"):
            return
        self._line_dash_setting = None

    @final
    def _initialize_line_round_dot_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_round_dot_setting attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, "_line_round_dot_setting"):
            return
        self._line_round_dot_setting = None

    @final
    def _initialize_line_dash_dot_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_dash_dot_setting attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, "_line_dash_dot_setting"):
            return
        self._line_dash_dot_setting = None

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_color(self) -> String:
        """
        Get current line color.

        Returns
        -------
        line_color : String
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, this interface returns a blank string.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color="#fff", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
        ... )
        >>> sprite.graphics.line_color
        String('#ffffff')
        """
        from apysc._type import value_util

        self._initialize_line_color_if_not_initialized()
        return value_util.get_copy(value=self._line_color)

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_thickness(self) -> Int:
        """
        Get current line thickness.

        Returns
        -------
        line_thickness : Int
            Current line thickness.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color="#fff", thickness=5, alpha=0.5)
        >>> sprite.graphics.line_thickness
        Int(5)
        """
        from apysc._type import value_util

        self._initialize_line_thickness_if_not_initialized()
        return value_util.get_copy(value=self._line_thickness)

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_alpha(self) -> Number:
        """
        Get current line color opacity.

        Returns
        -------
        line_alpha : Number
            Current line opacity (0.0 to 1.0).

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color="#fff", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
        ... )
        >>> sprite.graphics.line_alpha
        Number(0.5)
        """
        from apysc._type import value_util

        self._initialize_line_alpha_if_not_initialized()
        return value_util.get_copy(value=self._line_alpha)

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_cap(self) -> String:
        """
        Get current line cap (edge) style setting.

        Returns
        -------
        line_cap : String
            Current line cap (edge) style setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color="#fff", thickness=5, alpha=0.5, cap=ap.LineCaps.ROUND
        ... )
        >>> sprite.graphics.line_cap
        String('round')
        """
        self._initialize_line_cap_if_not_initialized()
        return self._line_cap

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_joints(self) -> String:
        """
        Get current line joints (vertices) style setting.

        Returns
        -------
        line_joints : String
            Current line joints (vertices) style setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color="#fff", thickness=5, joints=ap.LineJoints.ROUND
        ... )
        >>> sprite.graphics.line_joints
        String('round')
        """
        self._initialize_line_joints_if_not_initialized()
        return self._line_joints

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_dot_setting(self) -> Optional[LineDotSetting]:
        """
        Get current line dot setting.

        Returns
        -------
        line_dot_setting : LineDotSetting or None
            Current line dot setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color="#fff", thickness=5, dot_setting=ap.LineDotSetting(dot_size=5)
        ... )
        >>> sprite.graphics.line_dot_setting.dot_size
        Int(5)
        """
        self._initialize_line_dot_setting_if_not_initialized()
        return self._line_dot_setting

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_dash_setting(self) -> Optional[LineDashSetting]:
        """
        Get a current line dash setting.

        Returns
        -------
        line_dash_setting : LineDashSetting or None
            Current line dash setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color="#fff",
        ...     thickness=5,
        ...     dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),
        ... )
        >>> sprite.graphics.line_dash_setting.dash_size
        Int(10)

        >>> sprite.graphics.line_dash_setting.space_size
        Int(5)
        """
        self._initialize_line_dash_setting_if_not_initialized()
        return self._line_dash_setting

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_round_dot_setting(self) -> Optional[LineRoundDotSetting]:
        """
        Get current line-round dot setting.

        Returns
        -------
        line_round_dot_setting : LineRoundDotSetting or None
            Current line round dot setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color="#fff",
        ...     thickness=5,
        ...     round_dot_setting=ap.LineRoundDotSetting(round_size=6, space_size=3),
        ... )
        >>> sprite.graphics.line_round_dot_setting.round_size
        Int(6)

        >>> sprite.graphics.line_round_dot_setting.space_size
        Int(3)
        """
        self._initialize_line_round_dot_setting_if_not_initialized()
        return self._line_round_dot_setting

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_dash_dot_setting(self) -> Optional[LineDashDotSetting]:
        """
        Get current line dash-dot setting.

        Returns
        -------
        line_dash_dot_setting : LineDashDotSetting or None
            Current line dash-dot setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color="#fff",
        ...     thickness=5,
        ...     dash_dot_setting=ap.LineDashDotSetting(
        ...         dot_size=2, dash_size=5, space_size=3
        ...     ),
        ... )
        >>> sprite.graphics.line_dash_dot_setting.dot_size
        Int(2)

        >>> sprite.graphics.line_dash_dot_setting.dash_size
        Int(5)

        >>> sprite.graphics.line_dash_dot_setting.space_size
        Int(3)
        """
        self._initialize_line_dash_dot_setting_if_not_initialized()
        return self._line_dash_dot_setting

    _line_color_snapshots: Dict[str, str]
    _line_thickness_snapshots: Dict[str, int]
    _line_alpha_snapshots: Dict[str, float]
    _line_cap_snapshots: Dict[str, str]
    _line_joints_snapshots: Dict[str, str]
    _line_dot_setting_snapshots: Dict[str, Optional[LineDotSetting]]
    _line_dash_setting_snapshots: Dict[str, Optional[LineDashSetting]]
    _line_round_dot_setting_snapshots: Dict[str, Optional[LineRoundDotSetting]]
    _line_dash_dot_setting_snapshots: Dict[str, Optional[LineDashDotSetting]]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_color_if_not_initialized()
        self._initialize_line_thickness_if_not_initialized()
        self._initialize_line_alpha_if_not_initialized()
        self._initialize_line_cap_if_not_initialized()
        self._initialize_line_joints_if_not_initialized()
        self._initialize_line_dot_setting_if_not_initialized()
        self._initialize_line_dash_setting_if_not_initialized()
        self._initialize_line_round_dot_setting_if_not_initialized()
        self._initialize_line_dash_dot_setting_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_color_snapshots",
            value=self._line_color._value,
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_thickness_snapshots",
            value=int(self._line_thickness._value),
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_alpha_snapshots",
            value=self._line_alpha._value,
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_cap_snapshots",
            value=self._line_cap._value,
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_joints_snapshots",
            value=self._line_joints._value,
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_dot_setting_snapshots",
            value=self._line_dot_setting,
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_dash_setting_snapshots",
            value=self._line_dash_setting,
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_round_dot_setting_snapshots",
            value=self._line_round_dot_setting,
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_dash_dot_setting_snapshots",
            value=self._line_dash_dot_setting,
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert values if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._line_color._value = self._line_color_snapshots[snapshot_name]
        self._line_thickness._value = self._line_thickness_snapshots[snapshot_name]
        self._line_alpha._value = self._line_alpha_snapshots[snapshot_name]
        self._line_cap._value = self._line_cap_snapshots[snapshot_name]
        self._line_joints._value = self._line_joints_snapshots[snapshot_name]

        self._line_dot_setting = self._line_dot_setting_snapshots[snapshot_name]
        self._line_dash_setting = self._line_dash_setting_snapshots[snapshot_name]
        self._line_round_dot_setting = self._line_round_dot_setting_snapshots[
            snapshot_name
        ]
        self._line_dash_dot_setting = self._line_dash_dot_setting_snapshots[
            snapshot_name
        ]
