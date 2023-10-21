"""Implementation of the Ellipse class.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._color.color import Color
from apysc._color.colorless import COLORLESS
from apysc._display import graphics
from apysc._display.add_to_parent_mixin import AddToParentMixIn
from apysc._display.append_fill_alpha_attr_expression_mixin import (
    AppendFillAlphaAttrExpressionMixIn,
)
from apysc._display.append_fill_color_expression_mixin import (
    AppendFillColorAttrExpressionMixIn,
)
from apysc._display.append_line_alpha_attr_expression_mixin import (
    AppendLineAlphaAttrExpressionMixIn,
)
from apysc._display.append_line_cap_attr_expression_mixin import (
    AppendLineCapAttrExpressionMixIn,
)
from apysc._display.append_line_color_attr_expression_mixin import (
    AppendLineColorAttrExpressionMixIn,
)
from apysc._display.append_line_thickness_attr_expression_mixin import (
    AppendLineThicknessAttrExpressionMixIn,
)
from apysc._display.append_x_attr_expression_mixin import AppendXAttrExpressionMixIn
from apysc._display.append_y_attr_expression_mixin import AppendYAttrExpressionMixIn
from apysc._display.child_mixin import ChildMixIn
from apysc._display.css_mixin import CssMixIn
from apysc._display.cx_mixin import CxMixIn
from apysc._display.cy_mixin import CyMixIn
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.flip_x_mixin import FlipXMixIn
from apysc._display.flip_y_mixin import FlipYMixIn
from apysc._display.get_bounds_mixin import GetBoundsMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._display.line_alpha_mixin import LineAlphaMixIn
from apysc._display.line_caps import LineCaps
from apysc._display.line_color_mixin import LineColorMixIn
from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._display.line_dash_dot_setting_mixin import LineDashDotSettingMixIn
from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_dash_setting_mixin import LineDashSettingMixIn
from apysc._display.line_dot_setting import LineDotSetting
from apysc._display.line_dot_setting_mixin import LineDotSettingMixIn
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._display.line_round_dot_setting_mixin import LineRoundDotSettingMixIn
from apysc._display.rotation_around_center_mixin import RotationAroundCenterMixIn
from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
from apysc._display.scale_x_from_center_mixin import ScaleXFromCenterMixIn
from apysc._display.scale_x_from_point_mixin import ScaleXFromPointMixIn
from apysc._display.scale_y_from_center_mixin import ScaleYFromCenterMixIn
from apysc._display.scale_y_from_point_mixin import ScaleYFromPointMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.skew_x_mixin import SkewXMixIn
from apysc._display.skew_y_mixin import SkewYMixIn
from apysc._display.width_and_height_mixin_for_ellipse import (
    WidthAndHeightMixInForEllipse,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.attr_to_apysc_val_from_builtin_mixin import (
    AttrToApyscValFromBuiltinMixIn,
)
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.repr_interface import ReprInterface
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class Ellipse(
    ReprInterface,
    CxMixIn,
    AppendXAttrExpressionMixIn,
    CyMixIn,
    AppendYAttrExpressionMixIn,
    SetOverflowVisibleSettingMixIn,
    CssMixIn,
    GraphicsBase,
    RotationAroundCenterMixIn,
    RotationAroundPointMixIn,
    ScaleXFromCenterMixIn,
    ScaleYFromCenterMixIn,
    ScaleXFromPointMixIn,
    ScaleYFromPointMixIn,
    FlipXMixIn,
    FlipYMixIn,
    SkewXMixIn,
    SkewYMixIn,
    WidthAndHeightMixInForEllipse,
    FillColorMixIn,
    AppendFillColorAttrExpressionMixIn,
    FillAlphaMixIn,
    AppendFillAlphaAttrExpressionMixIn,
    LineColorMixIn,
    AppendLineColorAttrExpressionMixIn,
    LineAlphaMixIn,
    AppendLineAlphaAttrExpressionMixIn,
    AppendLineThicknessAttrExpressionMixIn,
    AppendLineCapAttrExpressionMixIn,
    LineDotSettingMixIn,
    LineDashSettingMixIn,
    LineRoundDotSettingMixIn,
    LineDashDotSettingMixIn,
    GetBoundsMixIn,
    VariableNameSuffixMixIn,
    AttrToApyscValFromBuiltinMixIn,
    InitializeWithBaseValueInterface,
    AddToParentMixIn,
):
    """
    The ellipse vector graphics class.

    References
    ----------
    - Ellipse class
        - https://simon-ritchie.github.io/apysc/en/ellipse.html
    - Graphics draw_ellipse interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_ellipse.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
    >>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
    ...     x=100, y=100, width=80, height=50
    ... )
    >>> ellipse.x
    Number(100.0)

    >>> ellipse.y
    Number(100.0)

    >>> ellipse.width
    Int(80)

    >>> ellipse.height
    Int(50)

    >>> ellipse.fill_color
    Color("#00aaff")
    """

    # self
    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    # x
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    # y
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    # width
    @arg_validation_decos.is_integer(arg_position_index=3, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=3, optional=False)
    # height
    @arg_validation_decos.is_integer(arg_position_index=4, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=4, optional=False)
    # fill_color
    @arg_validation_decos.is_color(arg_position_index=5, optional=False)
    # fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=6, optional=False)
    # line_color
    @arg_validation_decos.is_color(arg_position_index=7, optional=False)
    # line_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=8, optional=False)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=9, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=9, optional=False)
    # line_cap
    @arg_validation_decos.is_line_cap(arg_position_index=10, optional=True)
    # line_dot_setting
    @arg_validation_decos.is_line_dot_setting(arg_position_index=11)
    # line_dash_setting
    @arg_validation_decos.is_line_dash_setting(arg_position_index=12)
    # line_round_dot_setting
    @arg_validation_decos.is_line_round_dot_setting(arg_position_index=13)
    # line_dash_dot_setting
    @arg_validation_decos.is_line_dash_dot_setting(arg_position_index=14)
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=15, optional=True
    )
    # variable_name_suffix
    @arg_validation_decos.is_builtin_string(arg_position_index=16, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        x: Union[float, Number],
        y: Union[float, Number],
        width: Union[int, Int],
        height: Union[int, Int],
        fill_color: Color = COLORLESS,
        fill_alpha: Union[float, Number] = 1.0,
        line_color: Color = COLORLESS,
        line_alpha: Union[float, Number] = 1.0,
        line_thickness: Union[int, Int] = 1,
        line_cap: Optional[Union[String, LineCaps]] = None,
        line_dot_setting: Optional[LineDotSetting] = None,
        line_dash_setting: Optional[LineDashSetting] = None,
        line_round_dot_setting: Optional[LineRoundDotSetting] = None,
        line_dash_dot_setting: Optional[LineDashDotSetting] = None,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Create an ellipse vector graphic.

        Parameters
        ----------
        x : float or Number
            X-coordinate of the ellipse center.
        y : float or Number
            Y-coordinate of the ellipse center.
        width : Int or int
            Ellipse width.
        height : Int or int
            Ellipse height.
        fill_color : Color, default COLORLESS
            A fill-color to set.
        fill_alpha : float or Number, default 1.0
            A fill-alpha to set.
        line_color : Color, default COLORLESS
            A line-color to set.
        line_alpha : float or Number, default 1.0
            A line-alpha to set.
        line_thickness : int or Int, default 1
            A line-thickness (line-width) to set.
        line_cap : String or LineCaps or None, default None
            A line-cap setting to set.
        line_dot_setting : LineDotSetting or None, default None
            A dot setting to set.
        line_dash_setting : LineDashSetting or None, default None
            A dash setting to set.
        line_round_dot_setting : LineRoundDotSetting or None, default None
            A round-dot setting to set.
        line_dash_dot_setting : LineDashDotSetting or None, default None
            A dash-dot (1-dot chain) setting to set.
        parent : ChildMixIn or None, default None
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - Ellipse class
            - https://simon-ritchie.github.io/apysc/en/ellipse.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> ellipse: ap.Ellipse = ap.Ellipse(
        ...     x=100, y=100, width=100, height=50, fill_color=ap.Color("#00aaff")
        ... )
        >>> ellipse.x
        Number(100.0)
        >>> ellipse.y
        Number(100.0)
        >>> ellipse.width
        Int(100)
        >>> ellipse.height
        Int(50)
        >>> ellipse.fill_color
        Color("#00aaff")
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.ELLIPSE
        )
        self.variable_name = variable_name
        self._width = self._get_copied_int_from_builtin_val(
            integer=width, attr_identifier="width"
        )
        self._height = self._get_copied_int_from_builtin_val(
            integer=height, attr_identifier="height"
        )
        self._append_width_attr_linking_setting()
        self._append_height_attr_linking_setting()
        self._set_initial_basic_values(
            fill_color=fill_color,
            fill_alpha=fill_alpha,
            line_color=line_color,
            line_thickness=line_thickness,
            line_alpha=line_alpha,
            line_cap=line_cap,
            line_joints=None,
        )
        self._append_constructor_expression()
        self.x = self._get_copied_number_from_builtin_val(
            float_or_num=x, attr_identifier="x"
        )
        self.y = self._get_copied_number_from_builtin_val(
            float_or_num=y, attr_identifier="y"
        )
        self._set_line_setting_if_not_none_value_exists(
            line_dot_setting=line_dot_setting,
            line_dash_setting=line_dash_setting,
            line_round_dot_setting=line_round_dot_setting,
            line_dash_dot_setting=line_dash_dot_setting,
        )
        super(Ellipse, self).__init__(variable_name=variable_name)
        self._set_overflow_visible_setting()
        self._add_to_parent(parent=parent)

    @classmethod
    @final
    def _create_with_graphics(
        cls,
        *,
        graphics: "graphics.Graphics",
        x: Union[float, Number],
        y: Union[float, Number],
        width: Union[int, Int],
        height: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> "Ellipse":
        """
        Create an ellipse instance with the instance of
        specified graphics.

        Parameters
        ----------
        graphics : Graphics
            Graphics instance to link this instance.
        x : float or Number
            X-coordinate of the ellipse center.
        y : float or Number
            Y-coordinate of the ellipse center.
        width : Int or int
            Ellipse width.
        height : Int or int
            Ellipse height.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        ellipse : Ellipse
            A created ellipse instance.
        """
        ellipse: Ellipse = Ellipse(
            x=x,
            y=y,
            width=width,
            height=height,
            fill_color=graphics._fill_color,
            fill_alpha=graphics._fill_alpha,
            line_color=graphics._line_color,
            line_alpha=graphics._line_alpha,
            line_thickness=graphics._line_thickness,
            line_cap=graphics._line_cap,
            line_dot_setting=graphics._line_dot_setting,
            line_dash_setting=graphics._line_dash_setting,
            line_round_dot_setting=graphics._line_round_dot_setting,
            line_dash_dot_setting=graphics._line_dash_dot_setting,
            parent=graphics,
            variable_name_suffix=variable_name_suffix,
        )
        return ellipse

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        INDENT_NUM: int = 2
        stage: Stage = get_stage()
        width_str: str = value_util.get_value_str_for_expression(value=self._width)
        height_str: str = value_util.get_value_str_for_expression(value=self._height)
        expression: str = (
            f"var {self.variable_name} = {stage.variable_name}"
            f"\n  .ellipse({width_str}, {height_str})"
            "\n  .attr({"
        )
        expression = self._append_fill_color_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_fill_alpha_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_line_color_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_line_thickness_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_line_alpha_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_line_cap_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_x_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression = self._append_y_attr_expression(
            expression=expression, indent_num=INDENT_NUM
        )
        expression += "\n  });"
        expression_data_util.append_js_expression(expression=expression)

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Ellipse("<variable_name>")`).
        """
        repr_str: str = f'{Ellipse.__name__}("{self.variable_name}")'
        return repr_str

    @classmethod
    @final
    def _initialize_with_base_value(cls) -> "Ellipse":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        ellipse : Ellipse
            An initialized ellipse instance.
        """
        from apysc._type.boolean import Boolean

        ellipse: Ellipse = Ellipse(
            x=-1,
            y=-1,
            width=1,
            height=1,
        )
        ellipse.visible = Boolean(False)
        return ellipse
