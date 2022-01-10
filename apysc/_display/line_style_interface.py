"""Class implementation for line style related interface.

See Also
--------
- graphics_clear_interface
"""

from typing import Dict
from typing import Optional
from typing import TypeVar
from typing import Union

from apysc._display.line_caps import LineCaps
from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_dot_setting import LineDotSetting
from apysc._display.line_joints import LineJoints
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.revert_interface import RevertInterface
from apysc._type.string import String

StrOrString = TypeVar('StrOrString', str, String)


class LineStyleInterface(RevertInterface):

    _line_color: String
    _line_thickness: Int
    _line_alpha: Number
    _line_cap: String
    _line_joints: String
    _line_dot_setting: Optional[LineDotSetting]
    _line_dash_setting: Optional[LineDashSetting]
    _line_round_dot_setting: Optional[LineRoundDotSetting]
    _line_dash_dot_setting: Optional[LineDashDotSetting]

    def line_style(
            self, color: StrOrString,
            *,
            thickness: Union[int, Int] = 1,
            alpha: Union[float, Number] = 1.0,
            cap: Optional[LineCaps] = None,
            joints: Optional[LineJoints] = None,
            dot_setting: Optional[LineDotSetting] = None,
            dash_setting: Optional[LineDashSetting] = None,
            round_dot_setting: Optional[LineRoundDotSetting] = None,
            dash_dot_setting: Optional[LineDashDotSetting] = None) -> None:
        """
        Set line style values.

        Parameters
        ----------
        color : str or String
            Hexadecimal color string. e.g., '#00aaff'
        thickness : int or Int, default 1
            Line thickness (minimum value is 1).
        alpha : float or Number, default 1.0
            Line color opacity (0.0 to 1.0).
        cap : LineCaps or None, default None
            Line cap (edge style) setting. This will be ignored by not
            line-related graphics (e.g., Rectangle will ignore this,
            conversely used by Polyline).
        joints : LineJoints or None, default None
            Line vertices (joints) style setting. This will be ignored
            by not polyline-related graphics (e.g., Rectangle will ignore
            this, conversely used by Polyline).
        dot_setting : LineDotSetting or None, default None
            Dot setting. If this is specified, line will be dotted.
        dash_setting : LineDashSetting or None, default None
            Dash setting. If this is specified, line will be dashed.
        round_dot_setting : LineRoundDotSetting or None, default None
            Round dot setting. If this is specified, line will be
            round dotted.
            Notes: since this style is using cap setting, so cap setting
            and line thickness setting will be overridden, and line size
            will be increased by the amount of cap.
            If you want to adjust to the same width of normal line when using
            move_to and line_to interfaces, then add half-round size to
            start x-coordinate and subtract from end e-coordinate.
            e.g.,
            `this.move_to(x + round_size / 2, y)`
            `this.line_to(x - round_size / 2, y)`
        dash_dot_setting : LineDashDotSetting or None, default None
            Dash dot (1-dot chain) setting. If this is specified, line
            will be 1-dot chained.

        References
        ----------
        - Graphics line_style interface document
            - https://bit.ly/3zauILT

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color='#fff', thickness=5, alpha=0.5,
        ...     cap=ap.LineCaps.ROUND)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_color
        String('#ffffff')

        >>> line.line_thickness
        Int(5)

        >>> line.line_alpha
        Number(0.5)

        >>> line.line_cap
        String('round')
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_style', locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            from apysc._color import color_util
            from apysc._converter import cast
            from apysc._type.number_value_interface import NumberValueInterface
            from apysc._validation import color_validation
            from apysc._validation import display_validation
            from apysc._validation import number_validation

            self._initialize_line_color_if_not_initialized()
            self._initialize_line_thickness_if_not_initialized()
            self._initialize_line_alpha_if_not_initialized()

            if color != '':
                color = color_util.complement_hex_color(
                    hex_color_code=color)
            self._line_color.value = color
            number_validation.validate_integer(integer=thickness)
            number_validation.validate_num_is_gt_zero(num=thickness)
            self._line_thickness = ap.Int(thickness)
            number_validation.validate_num(num=alpha)
            if not isinstance(alpha, NumberValueInterface):
                alpha = cast.to_float_from_int(int_or_float=alpha)
                alpha = ap.Number(alpha)
            color_validation.validate_alpha_range(alpha=alpha)
            self._line_alpha = alpha
            self._set_line_cap(cap=cap)
            self._set_line_joints(joints=joints)
            self._line_dot_setting = dot_setting
            self._line_dash_setting = dash_setting
            self._line_round_dot_setting = round_dot_setting
            self._line_dash_dot_setting = dash_dot_setting
            display_validation.validate_multiple_line_settings_isnt_set(
                any_instance=self)

    def _set_line_joints(self, *, joints: Optional[LineJoints]) -> None:
        """
        Set line joints setting to attribute.

        Parameters
        ----------
        joints : LineJoints or None, default None
            Line vertices (joints) style setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._set_line_joints, locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            from apysc._validation.display_validation import \
                validate_line_joints
            if joints is None:
                joints = LineJoints.MITER
            validate_line_joints(joints=joints)
            self._line_joints = ap.String(joints.value)

    def _set_line_cap(self, *, cap: Optional[LineCaps]) -> None:
        """
        Set line cap setting to attribute.

        Parameters
        ----------
        cap : LineCaps or None, default None
            Line cap (edge style) setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._set_line_cap, locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            from apysc._validation.display_validation import validate_line_cap
            if cap is None:
                cap = LineCaps.BUTT
            validate_line_cap(cap=cap)
            self._line_cap = ap.String(cap.value)

    def _initialize_line_color_if_not_initialized(self) -> None:
        """
        Initialize _line_color attribute it it is not
        initialized yet.
        """
        if hasattr(self, '_line_color'):
            return
        self._line_color = String('')

    def _initialize_line_thickness_if_not_initialized(self) -> None:
        """
        Initialize _line_thickness attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_thickness'):
            return
        self._line_thickness = Int(1)

    def _initialize_line_alpha_if_not_initialized(self) -> None:
        """
        Initialize _line_alpha attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_alpha'):
            return
        self._line_alpha = Number(1.0)

    def _initialize_line_cap_if_not_initialized(self) -> None:
        """
        Initialize _line_cap attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_line_cap'):
            return
        self._line_cap = String(LineCaps.BUTT.value)

    def _initialize_line_joints_if_not_initialized(self) -> None:
        """
        Initialize _line_joints attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_line_joints'):
            return
        self._line_joints = String(LineJoints.MITER.value)

    def _initialize_line_dot_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_dot_setting attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_dot_setting'):
            return
        self._line_dot_setting = None

    def _initialize_line_dash_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_dash_setting attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_dash_setting'):
            return
        self._line_dash_setting = None

    def _initialize_line_round_dot_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_round_dot_setting attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_round_dot_setting'):
            return
        self._line_round_dot_setting = None

    def _initialize_line_dash_dot_setting_if_not_initialized(self) -> None:
        """
        Initialize _line_dash_dot_setting attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_dash_dot_setting'):
            return
        self._line_dash_dot_setting = None

    @property
    def line_color(self) -> String:
        """
        Get current line color.

        Returns
        -------
        line_color : String
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, blank string will be returned.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color='#fff', thickness=5, alpha=0.5,
        ...     cap=ap.LineCaps.ROUND)
        >>> sprite.graphics.line_color
        String('#ffffff')
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_color', locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            from apysc._type import value_util
            self._initialize_line_color_if_not_initialized()
            return value_util.get_copy(value=self._line_color)

    @property
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
        >>> sprite.graphics.line_style(
        ...     color='#fff', thickness=5, alpha=0.5)
        >>> sprite.graphics.line_thickness
        Int(5)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_thickness', locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            from apysc._type import value_util
            self._initialize_line_thickness_if_not_initialized()
            return value_util.get_copy(value=self._line_thickness)

    @property
    def line_alpha(self) -> Number:
        """
        Get current line color opacity.

        Returns
        -------
        line_alpha : Number
            Current line opacity (0.0 to 1.0).
            If not be set, None will be returned.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color='#fff', thickness=5, alpha=0.5,
        ...     cap=ap.LineCaps.ROUND)
        >>> sprite.graphics.line_alpha
        Number(0.5)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_alpha', locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            from apysc._type import value_util
            self._initialize_line_alpha_if_not_initialized()
            return value_util.get_copy(value=self._line_alpha)

    @property
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
        ...     color='#fff', thickness=5, alpha=0.5,
        ...     cap=ap.LineCaps.ROUND)
        >>> sprite.graphics.line_cap
        String('round')
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_cap', locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            self._initialize_line_cap_if_not_initialized()
            return self._line_cap

    @property
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
        ...     color='#fff', thickness=5,
        ...     joints=ap.LineJoints.ROUND)
        >>> sprite.graphics.line_joints
        String('round')
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_joints', locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            self._initialize_line_joints_if_not_initialized()
            return self._line_joints

    @property
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
        ...     color='#fff', thickness=5,
        ...     dot_setting=ap.LineDotSetting(dot_size=5))
        >>> sprite.graphics.line_dot_setting.dot_size
        Int(5)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_dot_setting', locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            self._initialize_line_dot_setting_if_not_initialized()
            return self._line_dot_setting

    @property
    def line_dash_setting(self) -> Optional[LineDashSetting]:
        """
        Get current line dash setting.

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
        ...     color='#fff', thickness=5,
        ...     dash_setting=ap.LineDashSetting(
        ...         dash_size=10, space_size=5))
        >>> sprite.graphics.line_dash_setting.dash_size
        Int(10)

        >>> sprite.graphics.line_dash_setting.space_size
        Int(5)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_dash_setting', locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            self._initialize_line_dash_setting_if_not_initialized()
            return self._line_dash_setting

    @property
    def line_round_dot_setting(self) -> Optional[LineRoundDotSetting]:
        """
        Get current line round dot setting.

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
        ...     color='#fff', thickness=5,
        ...     round_dot_setting=ap.LineRoundDotSetting(
        ...         round_size=6, space_size=3))
        >>> sprite.graphics.line_round_dot_setting.round_size
        Int(6)

        >>> sprite.graphics.line_round_dot_setting.space_size
        Int(3)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_round_dot_setting', locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            self._initialize_line_round_dot_setting_if_not_initialized()
            return self._line_round_dot_setting

    @property
    def line_dash_dot_setting(self) -> Optional[LineDashDotSetting]:
        """
        Get current line dash dot setting.

        Returns
        -------
        line_dash_dot_setting : LineDashDotSetting or None
            Current line dash dot setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(
        ...     color='#fff', thickness=5,
        ...     dash_dot_setting=ap.LineDashDotSetting(
        ...         dot_size=2, dash_size=5, space_size=3))
        >>> sprite.graphics.line_dash_dot_setting.dot_size
        Int(2)

        >>> sprite.graphics.line_dash_dot_setting.dash_size
        Int(5)

        >>> sprite.graphics.line_dash_dot_setting.space_size
        Int(3)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_dash_dot_setting', locals_=locals(),
                module_name=__name__, class_=LineStyleInterface):
            self._initialize_line_dash_dot_setting_if_not_initialized()
            return self._line_dash_dot_setting

    _line_color_snapshots: Dict[str, str]
    _line_thickness_snapshots: Dict[str, int]
    _line_alpha_snapshots: Dict[str, float]
    _line_cap_snapshots: Dict[str, str]
    _line_joints_snapshots: Dict[str, str]
    _line_dot_setting_snapshots: Dict[str, Optional[LineDotSetting]]
    _line_dash_setting_snapshots: Dict[str, Optional[LineDashSetting]]
    _line_round_dot_setting_snapshots: Dict[
        str, Optional[LineRoundDotSetting]]
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
            dict_name='_line_color_snapshots',
            value=self._line_color._value, snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_thickness_snapshots',
            value=int(self._line_thickness._value),
            snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_alpha_snapshots',
            value=self._line_alpha._value, snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_cap_snapshots',
            value=self._line_cap._value, snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_joints_snapshots',
            value=self._line_joints._value, snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_dot_setting_snapshots',
            value=self._line_dot_setting, snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_dash_setting_snapshots',
            value=self._line_dash_setting, snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_round_dot_setting_snapshots',
            value=self._line_round_dot_setting, snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_dash_dot_setting_snapshots',
            value=self._line_dash_dot_setting, snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._line_color._value = self._line_color_snapshots[snapshot_name]
        self._line_thickness._value = self._line_thickness_snapshots[
            snapshot_name]
        self._line_alpha._value = self._line_alpha_snapshots[snapshot_name]
        self._line_cap._value = self._line_cap_snapshots[snapshot_name]
        self._line_joints._value = self._line_joints_snapshots[snapshot_name]

        self._line_dot_setting = self._line_dot_setting_snapshots[
            snapshot_name]
        self._line_dash_setting = self._line_dash_setting_snapshots[
            snapshot_name]
        self._line_round_dot_setting = self._line_round_dot_setting_snapshots[
            snapshot_name]
        self._line_dash_dot_setting = self._line_dash_dot_setting_snapshots[
            snapshot_name]
