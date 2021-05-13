"""Class implementation for line style related interface.

See Also
--------
- graphics_clear_interface
"""

from typing import Dict
from typing import Optional
from typing import TypeVar
from typing import Union

from apysc import Int
from apysc import Number
from apysc import String
from apysc.display.line_caps import LineCaps
from apysc.display.line_dash_setting import LineDashSetting
from apysc.display.line_dot_setting import LineDotSetting
from apysc.display.line_joints import LineJoints
from apysc.type.revert_interface import RevertInterface

StrOrString = TypeVar('StrOrString', str, String)


class LineStyleInterface(RevertInterface):

    _line_color: String
    _line_thickness: Int
    _line_alpha: Number
    _line_cap: String
    _line_joints: String
    _line_dot_setting: Optional[LineDotSetting]
    _line_dash_setting: Optional[LineDashSetting]

    def line_style(
            self, color: StrOrString,
            thickness: Union[int, Int] = 1,
            alpha: Union[float, Number] = 1.0,
            cap: Optional[LineCaps] = None,
            joints: Optional[LineJoints] = None,
            dot_setting: Optional[LineDotSetting] = None,
            dash_setting: Optional[LineDashSetting] = None) -> None:
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
        """
        from apysc.color import color_util
        from apysc.converter import cast
        from apysc.type.number_value_interface import NumberValueInterface
        from apysc.validation import color_validation
        from apysc.validation import number_validation

        self._initialize_line_color_if_not_initialized()
        self._initialize_line_thickness_if_not_initialized()
        self._initialize_line_alpha_if_not_initialized()

        color = color_util.complement_hex_color(
            hex_color_code=color)
        self._line_color.value = color
        number_validation.validate_integer(integer=thickness)
        number_validation.validate_num_is_gt_zero(num=thickness)
        self._line_thickness = Int(thickness)
        number_validation.validate_num(num=alpha)
        if not isinstance(alpha, NumberValueInterface):
            alpha = cast.to_float_from_int(int_or_float=alpha)
            alpha = Number(alpha)
        color_validation.validate_alpha_range(alpha=alpha)
        self._line_alpha = alpha
        self._set_line_cap(cap=cap)
        self._set_line_joints(joints=joints)
        self._line_dot_setting = dot_setting
        self._line_dash_setting = dash_setting

    def _set_line_joints(self, joints: Optional[LineJoints]) -> None:
        """
        Set line joints setting to attribute.

        Parameters
        ----------
        joints : LineJoints or None, default None
            Line vertices (joints) style setting.
        """
        from apysc.validation.display_validation import validate_line_joints
        if joints is None:
            joints = LineJoints.MITER
        validate_line_joints(joints=joints)
        self._line_joints = String(joints.value)

    def _set_line_cap(self, cap: Optional[LineCaps]) -> None:
        """
        Set line cap setting to attribute.

        Parameters
        ----------
        cap : LineCaps or None, default None
            Line cap (edge style) setting.
        """
        from apysc.validation.display_validation import validate_line_cap
        if cap is None:
            cap = LineCaps.BUTT
        validate_line_cap(cap=cap)
        self._line_cap = String(cap.value)

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
        Initialize _line_cap attribute if it is not initialized yet.
        """
        if hasattr(self, '_line_cap'):
            return
        self._line_cap = String(LineCaps.BUTT.value)

    def _initialize_line_joints_if_not_initialized(self) -> None:
        """
        Initialize _line_joints attribute if it is not initialized yet.
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

    @property
    def line_color(self) -> String:
        """
        Get current line color.

        Returns
        -------
        line_color : String
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, blank string will be returned.
        """
        from apysc.type import value_util
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
        """
        from apysc.type import value_util
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
        """
        from apysc.type import value_util
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
        """
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
        """
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
        """
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
        """
        self._initialize_line_dash_setting_if_not_initialized()
        return self._line_dash_setting

    _line_color_snapshots: Dict[str, str]
    _line_thickness_snapshots: Dict[str, int]
    _line_alpha_snapshots: Dict[str, float]
    _line_cap_snapshots: Dict[str, str]
    _line_joints_snapshots: Dict[str, str]
    _line_dot_setting_snapshots: Dict[str, Optional[LineDotSetting]]
    _line_dash_setting_snapshots: Dict[str, Optional[LineDashSetting]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_line_color_snapshots'):
            self._line_color_snapshots = {}
            self._line_thickness_snapshots = {}
            self._line_alpha_snapshots = {}
            self._line_cap_snapshots = {}
            self._line_joints_snapshots = {}
            self._line_dot_setting_snapshots = {}
            self._line_dash_setting_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_line_color_if_not_initialized()
        self._initialize_line_thickness_if_not_initialized()
        self._initialize_line_alpha_if_not_initialized()
        self._initialize_line_cap_if_not_initialized()
        self._initialize_line_joints_if_not_initialized()
        self._initialize_line_dot_setting_if_not_initialized()
        self._initialize_line_dash_setting_if_not_initialized()
        self._line_color_snapshots[snapshot_name] = self._line_color._value
        self._line_thickness_snapshots[snapshot_name] = \
            int(self._line_thickness._value)
        self._line_alpha_snapshots[snapshot_name] = self._line_alpha._value
        self._line_cap_snapshots[snapshot_name] = self._line_cap._value
        self._line_joints_snapshots[snapshot_name] = self._line_joints._value
        self._line_dot_setting_snapshots[snapshot_name] = \
            self._line_dot_setting
        self._line_dash_setting_snapshots[snapshot_name] = \
            self._line_dash_setting

    def _revert(self, snapshot_name: str) -> None:
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
