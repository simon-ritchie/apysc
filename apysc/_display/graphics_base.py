"""Class implementation for graphic's base class.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._color.color import Color
from apysc._display.display_object import DisplayObject
from apysc._display.line_caps import LineCaps
from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_dot_setting import LineDotSetting
from apysc._display.line_joints import LineJoints
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class GraphicsBase(
    DisplayObject,
):
    _variable_name: str

    @arg_validation_decos.not_empty_string(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __init__(self, *, variable_name: str) -> None:
        """
        Vector graphic base class.

        Parameters
        ----------
        variable_name : str
            Variable name of this instance. This will be used to
            js expression.
        """
        super(GraphicsBase, self).__init__(variable_name=variable_name)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_basic_values(
        self,
        *,
        fill_color: Color,
        fill_alpha: Union[float, Number],
        line_color: Color,
        line_thickness: Union[int, Int],
        line_alpha: Union[float, Number],
        line_cap: Optional[Union[String, LineCaps]],
        line_joints: Optional[Union[String, LineJoints]]
    ) -> None:
        """
        Set initial fundamental values (such as the fill color or
        line thickness).

        Parameters
        ----------
        fill_color : Color
            A fill-color value to set.
        fill_alpha : float or Number
            A fill-alpha value to set.
        line_color : Color
            A line-color value to set.
        line_thickness : int or Int
            A line-thickness value to set.
        line_alpha : float or Number
            A line-alpha value to set.
        line_cap : String or LineCaps or None
            A line-cap value to set.
        line_joints : String or LineJoints or None
            A line-joints value to set.
        """
        from apysc._display.fill_alpha_mixin import FillAlphaMixIn
        from apysc._display.fill_color_mixin import FillColorMixIn
        from apysc._display.line_alpha_mixin import LineAlphaMixIn
        from apysc._display.line_cap_mixin import LineCapMixIn
        from apysc._display.line_color_mixin import LineColorMixIn
        from apysc._display.line_joints_mixin import LineJointsMixIn
        from apysc._display.line_thickness_mixin import LineThicknessMixIn

        if isinstance(self, FillColorMixIn):
            self._set_initial_fill_color_if_not_colorless(fill_color=fill_color)
        if isinstance(self, FillAlphaMixIn):
            self._update_fill_alpha_and_skip_appending_exp(value=fill_alpha)
        if isinstance(self, LineColorMixIn):
            self._set_initial_line_color_if_not_colorless(line_color=line_color)
        if isinstance(self, LineThicknessMixIn):
            self._update_line_thickness_and_skip_appending_exp(value=line_thickness)
        if isinstance(self, LineAlphaMixIn):
            self._update_line_alpha_and_skip_appending_exp(value=line_alpha)
        if isinstance(self, LineCapMixIn) and line_cap is not None:
            self._update_line_cap_and_skip_appending_exp(value=line_cap)
        if isinstance(self, LineJointsMixIn) and line_joints is not None:
            self._update_line_joints_and_skip_appending_exp(value=line_joints)

        if isinstance(self, FillAlphaMixIn):
            self._append_applying_new_attr_val_exp(
                new_attr=self._fill_alpha, attr_name="fill_alpha"
            )
            self._append_attr_to_linking_stack(
                attr=self._fill_alpha, attr_name="fill_alpha"
            )

        if isinstance(self, FillColorMixIn):
            self._append_applying_new_attr_val_exp(
                new_attr=self._fill_color, attr_name="fill_color"
            )
            self._append_attr_to_linking_stack(
                attr=self._fill_color, attr_name="fill_color"
            )

        if isinstance(self, LineColorMixIn):
            self._append_applying_new_attr_val_exp(
                new_attr=self._line_color, attr_name="line_color"
            )
            self._append_attr_to_linking_stack(
                attr=self._line_color, attr_name="line_color"
            )

        if isinstance(self, LineAlphaMixIn):
            self._append_applying_new_attr_val_exp(
                new_attr=self._line_alpha, attr_name="line_alpha"
            )
            self._append_attr_to_linking_stack(
                attr=self._line_alpha, attr_name="line_alpha"
            )

        if isinstance(self, LineThicknessMixIn):
            self._append_applying_new_attr_val_exp(
                new_attr=self._line_thickness, attr_name="line_thickness"
            )
            self._append_attr_to_linking_stack(
                attr=self._line_thickness, attr_name="line_thickness"
            )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_line_setting_if_not_none_value_exists(
        self,
        line_dot_setting: Optional[LineDotSetting],
        line_dash_setting: Optional[LineDashSetting],
        line_round_dot_setting: Optional[LineRoundDotSetting],
        line_dash_dot_setting: Optional[LineDashDotSetting],
    ) -> None:
        """
        If a line setting (dot, dash, or something else) with a value
        other than None exists, set that value to the attribute.

        Parameters
        ----------
        line_dot_setting : Optional[LineDotSetting]
            A dot setting to set.
        line_dash_setting : Optional[LineDashSetting]
            A dash setting to set.
        line_round_dot_setting : Optional[LineRoundDotSetting]
            A round-dot setting to set.
        line_dash_dot_setting : Optional[LineDashDotSetting]
            A dash-dot (1-dot chain) setting to set.
        """
        if line_dot_setting is not None:
            self.line_dot_setting = line_dot_setting
            return
        if line_dash_setting is not None:
            self.line_dash_setting = line_dash_setting
            return
        if line_round_dot_setting is not None:
            self.line_round_dot_setting = line_round_dot_setting
            return
        if line_dash_dot_setting is not None:
            self.line_dash_dot_setting = line_dash_dot_setting
            return
