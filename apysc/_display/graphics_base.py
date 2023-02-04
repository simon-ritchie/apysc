"""Class implementation for graphic's base class.
"""

from abc import ABC
from abc import abstractmethod
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._display.child_mixin import ChildMixIn
from apysc._display.display_object import DisplayObject
from apysc._display.line_caps import LineCaps
from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_dot_setting import LineDotSetting
from apysc._display.line_joints import LineJoints
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._display.stage import get_stage
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class GraphicsBase(
    DisplayObject,
    ABC,
):

    _variable_name: str

    @arg_validation_decos.is_display_object_container(
        arg_position_index=1, optional=True
    )
    @arg_validation_decos.not_empty_string(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def __init__(self, *, parent: Optional[ChildMixIn], variable_name: str) -> None:
        """
        Vector graphic base class.

        Parameters
        ----------
        parent : ChildMixIn or None
            Parent instance. If a specified value is None,
            this interface uses a stage instance.
        variable_name : str
            Variable name of this instance. This will be used to
            js expression.
        """
        super(GraphicsBase, self).__init__(variable_name=variable_name)
        if parent is None:
            parent = get_stage()
        parent.add_child(child=self)
        self._set_overflow_visible_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_basic_values(
        self,
        *,
        fill_color: Union[str, String],
        fill_alpha: Union[float, Number],
        line_color: Union[str, String],
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
        fill_color : str or String
            A fill-color value to set.
        fill_alpha : float or Number
            A fill-alpha value to set.
        line_color : str or String
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
            self._set_initial_fill_color_if_not_blank(fill_color=fill_color)
        if isinstance(self, FillAlphaMixIn):
            self._update_fill_alpha_and_skip_appending_exp(value=fill_alpha)
        if isinstance(self, LineColorMixIn):
            self._set_initial_line_color_if_not_blank(line_color=line_color)
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

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_basic_vals_expression(self, *, expression: str, indent_num: int) -> str:
        """
        Append basic values expression to a specified one.

        Parameters
        ----------
        expression : str
            Target expression.
        indent_num : int
            Indentation number.

        Returns
        -------
        expression : str
            After appending expression.
        """
        from apysc._display import graphics_expression
        from apysc._display.fill_alpha_mixin import FillAlphaMixIn
        from apysc._display.fill_color_mixin import FillColorMixIn
        from apysc._display.line_alpha_mixin import LineAlphaMixIn
        from apysc._display.line_cap_mixin import LineCapMixIn
        from apysc._display.line_color_mixin import LineColorMixIn
        from apysc._display.line_joints_mixin import LineJointsMixIn
        from apysc._display.line_thickness_mixin import LineThicknessMixIn

        if isinstance(self, FillColorMixIn):
            self._initialize_fill_color_if_not_initialized()
            expression = graphics_expression.append_fill_expression(
                fill_color=self._fill_color,
                expression=expression,
                indent_num=indent_num,
            )

        if isinstance(self, FillAlphaMixIn):
            self._initialize_fill_alpha_if_not_initialized()
            expression = graphics_expression.append_fill_opacity_expression(
                fill_alpha=self._fill_alpha,
                expression=expression,
                indent_num=indent_num,
            )

        if isinstance(self, LineColorMixIn):
            self._initialize_line_color_if_not_initialized()
            expression = graphics_expression.append_stroke_expression(
                line_color=self._line_color,
                expression=expression,
                indent_num=indent_num,
            )

        if isinstance(self, LineThicknessMixIn):
            self._initialize_line_thickness_if_not_initialized()
            expression = graphics_expression.append_stroke_width_expression(
                line_thickness=self._line_thickness,
                expression=expression,
                indent_num=indent_num,
            )

        if isinstance(self, LineAlphaMixIn):
            self._initialize_line_alpha_if_not_initialized()
            expression = graphics_expression.append_stroke_opacity_expression(
                line_alpha=self._line_alpha,
                expression=expression,
                indent_num=indent_num,
            )

        if isinstance(self, LineCapMixIn):
            self._initialize_line_cap_if_not_initialized()
            expression = graphics_expression.append_stroke_linecap_expression(
                line_cap=self._line_cap, expression=expression, indent_num=indent_num
            )

        if isinstance(self, LineJointsMixIn):
            self._initialize_line_joints_if_not_initialized()
            expression = graphics_expression.append_stroke_linejoin_expression(
                line_joints=self._line_joints,
                expression=expression,
                indent_num=indent_num,
            )

        self._initialize_x_if_not_initialized()
        expression = graphics_expression.append_x_expression(
            x=self._x, expression=expression, indent_num=indent_num
        )

        self._initialize_y_if_not_initialized()
        expression = graphics_expression.append_y_expression(
            y=self._y, expression=expression, indent_num=indent_num
        )
        return expression

    @abstractmethod
    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).
        """
