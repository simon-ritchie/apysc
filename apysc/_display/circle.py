"""Implementations of Circle class.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._display import graphics
from apysc._display.child_mixin import ChildMixIn
from apysc._display.cx_mixin import CxMixIn
from apysc._display.cy_mixin import CyMixIn
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._display.line_caps import LineCaps
from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_dot_setting import LineDotSetting
from apysc._display.line_joints import LineJoints
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._display.radius_mixin import RadiusMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_to_apysc_val_from_builtin_mixin import (
    AttrToApyscValFromBuiltinMixIn,
)
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class Circle(
    CxMixIn,
    CyMixIn,
    GraphicsBase,
    RadiusMixIn,
    FillColorMixIn,
    FillAlphaMixIn,
    VariableNameSuffixMixIn,
    AttrToApyscValFromBuiltinMixIn,
):
    """
    The circle vector graphics class.

    References
    ----------
    - Circle class
        - https://simon-ritchie.github.io/apysc/en/circle.html
    - Graphics draw_circle interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_circle.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color="#0af")
    >>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
    >>> circle.x
    Int(100)

    >>> circle.y
    Int(100)

    >>> circle.radius
    Int(50)

    >>> circle.fill_color
    String('#00aaff')
    """

    # self
    @arg_validation_decos.multiple_line_settings_are_not_set(arg_position_index=0)
    # x
    @arg_validation_decos.is_integer(arg_position_index=1)
    # y
    @arg_validation_decos.is_integer(arg_position_index=2)
    # radius
    @arg_validation_decos.is_integer(arg_position_index=3)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=3)
    # fill_color
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=4)
    # fill_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=5)
    # line_color
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=6)
    # line_alpha
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=7)
    # line_thickness
    @arg_validation_decos.is_integer(arg_position_index=8)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=8)
    # line_cap
    @arg_validation_decos.is_line_cap(arg_position_index=9, optional=True)
    # line_joints
    @arg_validation_decos.is_line_joints(arg_position_index=10, optional=True)
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
        x: Union[int, Int],
        y: Union[int, Int],
        radius: Union[int, Int],
        fill_color: Union[str, String] = "",
        fill_alpha: Union[float, Number] = 1.0,
        line_color: Union[str, String] = "",
        line_alpha: Union[float, Number] = 1.0,
        line_thickness: Union[int, Int] = 1,
        line_cap: Optional[Union[String, LineCaps]] = None,
        line_joints: Optional[Union[String, LineJoints]] = None,
        line_dot_setting: Optional[LineDotSetting] = None,
        line_dash_setting: Optional[LineDashSetting] = None,
        line_round_dot_setting: Optional[LineRoundDotSetting] = None,
        line_dash_dot_setting: Optional[LineDashDotSetting] = None,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Create a circle vector graphic.

        Parameters
        ----------
        x : Int or int
            X-coordinate of the circle center.
        y : Int or int
            Y-coordinate of the circle center.
        radius : Int or int
            Circle radius.
        fill_color : str or String, default ''
            A fill-color to set.
        fill_alpha : float or Number, default 1.0
            A fill-alpha to set.
        line_color : str or String, default ''
            A line-color to set.
        line_alpha : float or Number, default 1.0
            A line-alpha to set.
        line_thickness : int or Int, default 1
            A line-thickness (line-width) to set.
        line_cap : String or LineCaps or None, default None
            A line-cap setting to set.
        line_joints : String or LineJoints or None, default None
            A line-joints setting to set.
        line_dot_setting : LineDotSetting or None, default None
            A dot setting to set.
        line_dash_setting : LineDashSetting or None, default None
            A dash setting to set.
        line_round_dot_setting : LineRoundDotSetting or None, default None
            A round-dot setting to set.
        line_dash_dot_setting : LineDashDotSetting or None, default None
            A dash dot (1-dot chain) setting to set.
        parent : ChildMixIn or None, default None
            A parent instance to add this instance.
            If a specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript's debugging.

        References
        ----------
        - Circle class
            - https://simon-ritchie.github.io/apysc/en/circle.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> circle: ap.Circle = ap.Circle(x=100, y=100, radius=50, fill_color="#00aaff")
        >>> circle.x
        Int(100)
        >>> circle.y
        Int(100)
        >>> circle.radius
        Int(50)
        >>> circle.fill_color
        String('#00aaff')

        >>> circle = ap.Circle(
        ...     x=100,
        ...     y=100,
        ...     radius=50,
        ...     line_color="#ffffff",
        ...     line_thickness=3,
        ...     line_dot_setting=ap.LineDotSetting(dot_size=10),
        ... )
        >>> circle.line_color
        String('#ffffff')
        >>> circle.line_thickness
        Int(3)
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.CIRCLE
        )
        self.variable_name = variable_name
        self._radius = self._get_converted_radius_int(radius=radius)
        self._set_initial_basic_values(
            fill_color=fill_color,
            fill_alpha=fill_alpha,
            line_color=line_color,
            line_thickness=line_thickness,
            line_alpha=line_alpha,
            line_cap=line_cap,
            line_joints=line_joints,
        )
        self._append_constructor_expression()
        self._set_center_coordinates(x=x, y=y)
        self._set_line_setting_if_not_none_value_exists(
            line_dot_setting=line_dot_setting,
            line_dash_setting=line_dash_setting,
            line_round_dot_setting=line_round_dot_setting,
            line_dash_dot_setting=line_dash_dot_setting,
        )
        super(Circle, self).__init__(parent=parent, variable_name=variable_name)

        self._append_applying_new_attr_val_exp(
            new_attr=self._radius, attr_name="radius"
        )
        self._append_attr_to_linking_stack(attr=self._radius, attr_name="radius")

    @classmethod
    @final
    def _create_with_graphics(
        cls,
        *,
        graphics: "graphics.Graphics",
        x: Union[int, Int],
        y: Union[int, Int],
        radius: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> "Circle":
        """
        Create a rectangle instance with the instance of
        specified graphics.

        Parameters
        ----------
        graphics : graphics.Graphics
            Graphics instance to link this instance.
        x : Int or int
            X-coordinate of the circle center.
        y : Int or int
            Y-coordinate of the circle center.
        radius : Int or int
            Circle radius.
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript's debugging.

        Returns
        -------
        circle : Circle
            A created circle instance.
        """
        circle: Circle = Circle(
            x=x,
            y=y,
            radius=radius,
            fill_color=graphics._fill_color,
            fill_alpha=graphics._fill_alpha,
            line_color=graphics._line_color,
            line_alpha=graphics._line_alpha,
            line_thickness=graphics._line_thickness,
            line_cap=graphics._line_cap,
            line_joints=graphics._line_joints,
            line_dot_setting=graphics._line_dot_setting,
            line_dash_setting=graphics._line_dash_setting,
            line_round_dot_setting=graphics._line_round_dot_setting,
            line_dash_dot_setting=graphics._line_dash_dot_setting,
            parent=graphics,
            variable_name_suffix=variable_name_suffix,
        )
        return circle

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_center_coordinates(
        self, *, x: Union[int, Int], y: Union[int, Int]
    ) -> None:
        """
        Set a center x-coordinate and a center y-coordinate.

        Parameters
        ----------
        x : Int or int
            X-coordinate of the circle center.
        y : Int or int
            Y-coordinate of the circle center.
        """
        self.x = self._get_copied_int_from_builtin_val(integer=x, attr_identifier="x")
        self.y = self._get_copied_int_from_builtin_val(integer=y, attr_identifier="y")

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        import apysc as ap
        from apysc._type import value_util

        stage: ap.Stage = ap.get_stage()
        radius_str: str = value_util.get_value_str_for_expression(value=self._radius)
        expression: str = (
            f"var {self.variable_name} = {stage.variable_name}"
            f"\n  .circle({radius_str} * 2)"
            "\n  .attr({"
        )
        expression = self._append_basic_vals_expression(
            expression=expression, indent_num=2
        )
        expression += "\n  });"
        ap.append_js_expression(expression=expression)

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Circle('<variable_name>')`).
        """
        repr_str: str = f"Circle('{self.variable_name}')"
        return repr_str
