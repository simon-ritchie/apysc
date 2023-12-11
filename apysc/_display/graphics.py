# pyright: reportIncompatibleVariableOverride=false

"""Implementations for Graphics class.
"""

from typing import List
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._display import circle as _circle
from apysc._display import ellipse as _ellipse
from apysc._display import line as _line
from apysc._display import path as _path
from apysc._display import polygon as _polyg
from apysc._display import polyline as _polyline
from apysc._display import sprite
from apysc._display import triangle as _triangle
from apysc._display.begin_fill_mixin import BeginFillMixIn
from apysc._display.child_mixin import ChildMixIn
from apysc._display.css_mixin import CssMixIn
from apysc._display.display_object import DisplayObject
from apysc._display.graphics_clear_mixin import GraphicsClearMixIn
from apysc._display.line_style_mixin import LineStyleMixIn
from apysc._display.rectangle import Rectangle
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._geom.path_data_base import PathDataBase
from apysc._geom.point2d import Point2D
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.array import Array
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class Graphics(
    XMixIn,
    YMixIn,
    SetOverflowVisibleSettingMixIn,
    CssMixIn,
    DisplayObject,
    BeginFillMixIn,
    LineStyleMixIn,
    GraphicsClearMixIn,
    ChildMixIn,
    InitializeWithBaseValueInterface,
):
    """
    Create an object that has each vector graphics interface.

    References
    ----------
    - Graphics
        - https://simon-ritchie.github.io/apysc/en/graphics.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50
    ... )
    >>> rectangle.x
    Number(50.0)

    >>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
    >>> circle.x
    Number(100.0)
    """

    _current_line: Optional["_polyline.Polyline"] = None

    @final
    @arg_validation_decos.is_display_object_container(
        arg_position_index=1, optional=False
    )
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=True)
    @arg_validation_decos.is_builtin_string(arg_position_index=3, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        parent: "sprite.Sprite",
        variable_name: Optional[str] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Create an object that has each vector graphics interface.

        Parameters
        ----------
        parent : Sprite
            A parent instance.
        variable_name : str or None, default None
            Variable name to set. Specified only when
            a subclass instantiation.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - Graphics
            - https://simon-ritchie.github.io/apysc/en/graphics.html
        """
        from apysc._color.colorless import COLORLESS
        from apysc._display.sprite import Sprite
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._validation import display_validation

        self._variable_name_suffix = variable_name_suffix
        display_validation.validate_sprite(sprite=parent)
        self.parent_sprite: Sprite = parent
        if variable_name is None:
            variable_name = expression_variables_util.get_next_variable_name(
                type_name=var_names.GRAPHICS
            )
        super(Graphics, self).__init__(variable_name=variable_name)

        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="fill_color"
        )
        self._fill_color = COLORLESS

        suffix = self._get_attr_or_variable_name_suffix(value_identifier="fill_alpha")
        self._fill_alpha = Number(1.0, variable_name_suffix=suffix)

        suffix = self._get_attr_or_variable_name_suffix(value_identifier="line_color")
        self._line_color = COLORLESS

        suffix = self._get_attr_or_variable_name_suffix(value_identifier="line_alpha")
        self._line_alpha = Number(1.0, variable_name_suffix=suffix)

        suffix = self._get_attr_or_variable_name_suffix(
            value_identifier="line_thickness"
        )
        self._line_thickness = Int(1.0, variable_name_suffix=suffix)

        self._initialize_line_cap_if_not_initialized()
        self._initialize_line_joints_if_not_initialized()
        self._initialize_line_dot_setting_if_not_initialized()
        self._initialize_line_dash_setting_if_not_initialized()
        self._initialize_line_round_dot_setting_if_not_initialized()
        self._initialize_line_dash_dot_setting_if_not_initialized()

        suffix = self._get_attr_or_variable_name_suffix(value_identifier="children")
        self._children = Array([], variable_name_suffix=suffix)

        self._append_constructor_expression()
        self.parent_sprite.add_child(child=self)
        self._set_overflow_visible_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._expression import expression_data_util

        stage: Stage = get_stage()
        expression: str = f"var {self.variable_name} = {stage.variable_name}.nested();"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=3, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=3, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=4, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=4, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=5, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_rect(
        self,
        *,
        x: Union[float, Number],
        y: Union[float, Number],
        width: Union[int, Int],
        height: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> Rectangle:
        """
        Draw a rectangle vector graphics.

        Parameters
        ----------
        x : float or Number
            X position to start drawing.
        y : float or Number
            Y position to start drawing.
        width : Int or int
            Rectangle width.
        height : Int or int
            Rectangle height.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        rectangle : Rectangle
            Created rectangle.

        References
        ----------
        - Graphics draw_rect interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_rect.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.x
        Number(50.0)

        >>> rectangle.width
        Int(50)

        >>> rectangle.fill_color
        Color("#00aaff")
        """
        rectangle: Rectangle = Rectangle._create_with_graphics(
            graphics=self,
            x=x,
            y=y,
            width=width,
            height=height,
            variable_name_suffix=variable_name_suffix,
        )
        return rectangle

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=3, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=3, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=4, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=4, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=5, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=5, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=6, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=6, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=7, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_round_rect(
        self,
        *,
        x: Union[float, Number],
        y: Union[float, Number],
        width: Union[int, Int],
        height: Union[int, Int],
        ellipse_width: Union[int, Int],
        ellipse_height: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> Rectangle:
        """
        Draw a rounded rectangle vector graphics.

        Parameters
        ----------
        x : float or Number
            X-coordinate to start drawing.
        y : float or Number
            Y-coordinate to start drawing.
        width : Int or int
            Rectangle width.
        height : Int or int
            Rectangle height.
        ellipse_width : Int or int
            Ellipse width of the rectangle corner.
        ellipse_height : Int or int
            Ellipse height of the rectangle corner.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        rectangle : Rectangle
            Created rectangle.

        References
        ----------
        - Graphics draw_round_rect interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_round_rect.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> round_rect: ap.Rectangle = sprite.graphics.draw_round_rect(
        ...     x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=15
        ... )
        >>> round_rect.ellipse_width
        Int(10)

        >>> round_rect.ellipse_height
        Int(15)
        """
        rectangle: Rectangle = Rectangle._create_with_graphics(
            graphics=self,
            x=x,
            y=y,
            width=width,
            height=height,
            variable_name_suffix=variable_name_suffix,
        )
        if isinstance(ellipse_width, int):
            ellipse_width = Int(
                ellipse_width, variable_name_suffix=variable_name_suffix
            )
        if isinstance(ellipse_height, int):
            ellipse_height = Int(
                ellipse_height, variable_name_suffix=variable_name_suffix
            )
        rectangle.ellipse_width = ellipse_width
        rectangle.ellipse_height = ellipse_height
        return rectangle

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=3, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=3, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=4, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_circle(
        self,
        *,
        x: Union[float, Number],
        y: Union[float, Number],
        radius: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> "_circle.Circle":
        """
        Draw a circle vector graphics.

        Parameters
        ----------
        x : float or Number
            X-coordinate of the circle center.
        y : float or Number
            Y-coordinate of the circle center.
        radius : Int or int
            Circle radius.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        circle : Circle
            Created circle graphics instance.

        References
        ----------
        - Graphics draw_circle interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_circle.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
        >>> circle.x
        Number(100.0)

        >>> circle.y
        Number(100.0)

        >>> circle.radius
        Int(50)

        >>> circle.fill_color
        Color("#00aaff")
        """
        circle: _circle.Circle = _circle.Circle._create_with_graphics(
            graphics=self,
            x=x,
            y=y,
            radius=radius,
            variable_name_suffix=variable_name_suffix,
        )
        return circle

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=3, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=3, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=4, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=4, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=5, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_ellipse(
        self,
        *,
        x: Union[float, Number],
        y: Union[float, Number],
        width: Union[int, Int],
        height: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> "_ellipse.Ellipse":
        """
        Draw an ellipse vector graphic.

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
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        ellipse : Ellipse
            Created ellipse graphics instance.

        References
        ----------
        - Graphics draw_ellipse interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_ellipse.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        ...     x=100, y=100, width=100, height=50
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
        ellipse: _ellipse.Ellipse = _ellipse.Ellipse._create_with_graphics(
            graphics=self,
            x=x,
            y=y,
            width=width,
            height=height,
            variable_name_suffix=variable_name_suffix,
        )
        return ellipse

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=3, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def line_to(
        self,
        *,
        x: Union[float, Number],
        y: Union[float, Number],
        variable_name_suffix: str = "",
    ) -> "_polyline.Polyline":
        """
        Draw a line from previous point to specified point (initial
        point is x = 0, y = 0).

        Parameters
        ----------
        x : float or Number
            X destination point to draw a line.
        y : float or Number
            Y destination point to draw a line.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        line : Polyline
            Line graphics instance.

        References
        ----------
        - Graphics move_to and line_to interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_move_to_and_line_to.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
        >>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
        >>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
        >>> line_3: ap.Polyline = sprite.graphics.line_to(x=50, y=150)
        >>> line_1 == line_2 == line_3
        True

        >>> line_1.line_color
        Color("#ffffff")

        >>> line_1.line_thickness
        Int(5)
        """
        if self._current_line is None:
            first_point: Point2D = Point2D(
                x=0, y=0, variable_name_suffix=variable_name_suffix
            )
            second_point: Point2D = Point2D(
                x=x, y=y, variable_name_suffix=variable_name_suffix
            )
            self._current_line = _polyline.Polyline._create_with_graphics(
                graphics=self,
                points=[first_point, second_point],
                variable_name_suffix=variable_name_suffix,
            )
        else:
            self._current_line.append_line_point(x=x, y=y)
            if variable_name_suffix != "":
                self._current_line._variable_name_suffix = variable_name_suffix
        return self._current_line

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=3, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def move_to(
        self,
        *,
        x: Union[float, Number],
        y: Union[float, Number],
        variable_name_suffix: str = "",
    ) -> "_polyline.Polyline":
        """
        Move a line position to a specified point.

        Parameters
        ----------
        x : float or Number
            X destination point to move.
        y : float or Number
            Y destination point to move.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        line : Polyline
            Line graphics instance.

        References
        ----------
        - Graphics move_to and line_to interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_move_to_and_line_to.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
        >>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
        >>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
        >>> line_1 == line_2
        True

        >>> line_1.line_color
        Color("#ffffff")

        >>> line_1.line_thickness
        Int(5)
        """
        point: Point2D = Point2D(x=x, y=y, variable_name_suffix=variable_name_suffix)
        polyline: _polyline.Polyline = _polyline.Polyline._create_with_graphics(
            graphics=self, points=[point], variable_name_suffix=variable_name_suffix
        )
        self._current_line = polyline
        return polyline

    @final
    def _reset_each_line_settings(self) -> None:
        """
        Reset each line settings (e.g., LineDotSetting, LineDashSetting,
        and so on).

        Notes
        -----
        This interface does not append an expression.
        """
        self._line_dot_setting = None
        self._line_dash_setting = None
        self._line_round_dot_setting = None
        self._line_dash_dot_setting = None

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=5, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_line(
        self,
        *,
        x_start: Union[float, Number],
        y_start: Union[float, Number],
        x_end: Union[float, Number],
        y_end: Union[float, Number],
        variable_name_suffix: str = "",
    ) -> "_line.Line":
        """
        Draw a normal line vector graphic.

        Notes
        -----
        - This interface ignores line settings, like
            the `LineDotSetting`, `LineDashSetting`.

        Parameters
        ----------
        x_start : float or Number
            Line start x-coordinate.
        y_start : float or Number
            Line start y-coordinate.
        x_end : float or Number
            Line end x-coordinate.
        y_end : float or Number
            Line end y-coordinate.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        line : Line
            Created line graphics instance.

        References
        ----------
        - Graphics draw_line interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_line.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50
        ... )
        >>> line.line_color
        Color("#ffffff")

        >>> line.line_thickness
        Int(5)
        """
        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        line: _line.Line = _line.Line._create_with_graphics(
            graphics=self,
            start_point=Point2D(
                x=x_start, y=y_start, variable_name_suffix=variable_name_suffix
            ),
            end_point=Point2D(
                x=x_end, y=y_end, variable_name_suffix=variable_name_suffix
            ),
            variable_name_suffix=variable_name_suffix,
        )
        self._run_all_revert_methods(snapshot_name=snapshot_name)
        return line

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=5, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=5, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=6, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_dotted_line(
        self,
        *,
        x_start: Union[float, Number],
        y_start: Union[float, Number],
        x_end: Union[float, Number],
        y_end: Union[float, Number],
        dot_size: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> "_line.Line":
        """
        Draw a dotted line vector graphics.

        Notes
        -----
        - This interface ignores line settings, like the
            `LineDashSetting`, except `LineDotSetting`.

        Parameters
        ----------
        x_start : float or Number
            Line start x-coordinate.
        y_start : float or Number
            Line start y-coordinate.
        x_end : float or Number
            Line end x-coordinate.
        y_end : float or Number
            Line end y-coordinate.
        dot_size : Int or int
            Dot size.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        line : Line
            Created line graphics instance.

        References
        ----------
        - Graphics draw_dotted_line interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_dotted_line.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_dotted_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50, dot_size=5
        ... )
        >>> line.line_color
        Color("#ffffff")

        >>> line.line_thickness
        Int(5)

        >>> line.line_dot_setting.dot_size
        Int(5)
        """
        from apysc._display.line_dot_setting import LineDotSetting

        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_dot_setting = LineDotSetting(
            dot_size=dot_size, variable_name_suffix=variable_name_suffix
        )
        line: _line.Line = _line.Line._create_with_graphics(
            graphics=self,
            start_point=Point2D(
                x=x_start, y=y_start, variable_name_suffix=variable_name_suffix
            ),
            end_point=Point2D(
                x=x_end, y=y_end, variable_name_suffix=variable_name_suffix
            ),
            variable_name_suffix=variable_name_suffix,
        )
        self._run_all_revert_methods(snapshot_name=snapshot_name)
        return line

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=5, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=5, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=6, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=6, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=7, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_dashed_line(
        self,
        *,
        x_start: Union[float, Number],
        y_start: Union[float, Number],
        x_end: Union[float, Number],
        y_end: Union[float, Number],
        dash_size: Union[int, Int],
        space_size: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> "_line.Line":
        """
        Draw a dashed line vector graphics.

        Notes
        -----
        - This interface ignores line settings, like
        the `LineDotSetting`, except `LineDashSetting`.

        Parameters
        ----------
        x_start : float or Number
            Line start x-coordinate.
        y_start : float or Number
            Line start y-coordinate.
        x_end : float or Number
            Line end x-coordinate.
        y_end : float or Number
            Line end y-coordinate.
        dash_size : Int or int
            Dash size.
        space_size : Int or int
            Blank space size between dashes.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        line : Line
            Created line graphics instance.

        References
        ----------
        - Graphics draw_dashed_line interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_dashed_line.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_dashed_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50, dash_size=5, space_size=2
        ... )
        >>> line.line_color
        Color("#ffffff")

        >>> line.line_dash_setting.dash_size
        Int(5)

        >>> line.line_dash_setting.space_size
        Int(2)
        """
        from apysc._display.line_dash_setting import LineDashSetting

        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_dash_setting = LineDashSetting(
            dash_size=dash_size,
            space_size=space_size,
            variable_name_suffix=variable_name_suffix,
        )
        line: _line.Line = _line.Line._create_with_graphics(
            graphics=self,
            start_point=Point2D(
                x=x_start, y=y_start, variable_name_suffix=variable_name_suffix
            ),
            end_point=Point2D(
                x=x_end, y=y_end, variable_name_suffix=variable_name_suffix
            ),
            variable_name_suffix=variable_name_suffix,
        )
        self._run_all_revert_methods(snapshot_name=snapshot_name)
        return line

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=5, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=5, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=6, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=6, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=7, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_round_dotted_line(
        self,
        *,
        x_start: Union[float, Number],
        y_start: Union[float, Number],
        x_end: Union[float, Number],
        y_end: Union[float, Number],
        round_size: Union[int, Int],
        space_size: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> "_line.Line":
        """
        Draw a round-dotted line vector graphics.

        Notes
        -----
        This interface ignores line settings, like the
        `LineDotSetting`, except `LineRoundDotSetting`.

        Parameters
        ----------
        x_start : float or Number
            Line start x-coordinate.
        y_start : float or Number
            Line start y-coordinate.
        x_end : float or Number
            Line end x-coordinate.
        y_end : float or Number
            Line end y-coordinate.
        round_size : Int or int
            Dot round size.
        space_size : Int or int
            Blank space size between dots.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        line : Line
            Created line graphics instance.

        References
        ----------
        - Graphics draw_round_dotted_line interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_round_dotted_line.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_round_dotted_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50, round_size=6, space_size=3
        ... )
        >>> line.line_color
        Color("#ffffff")

        >>> line.line_round_dot_setting.round_size
        Int(6)

        >>> line.line_round_dot_setting.space_size
        Int(3)
        """
        from apysc._display.line_round_dot_setting import LineRoundDotSetting

        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_round_dot_setting = LineRoundDotSetting(
            round_size=round_size,
            space_size=space_size,
            variable_name_suffix=variable_name_suffix,
        )
        line: _line.Line = _line.Line._create_with_graphics(
            graphics=self,
            start_point=Point2D(
                x=x_start, y=y_start, variable_name_suffix=variable_name_suffix
            ),
            end_point=Point2D(
                x=x_end, y=y_end, variable_name_suffix=variable_name_suffix
            ),
            variable_name_suffix=variable_name_suffix,
        )
        self._run_all_revert_methods(snapshot_name=snapshot_name)
        return line

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=5, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=5, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=6, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=6, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=7, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=7, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=8, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_dash_dotted_line(
        self,
        *,
        x_start: Union[float, Number],
        y_start: Union[float, Number],
        x_end: Union[float, Number],
        y_end: Union[float, Number],
        dot_size: Union[int, Int],
        dash_size: Union[int, Int],
        space_size: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> "_line.Line":
        """
        Draw a dash-dotted (1-dot chain) line vector graphics.

        Parameters
        ----------
        x_start : float or Number
            Line start x-coordinate.
        y_start : float or Number
            Line start y-coordinate.
        x_end : float or Number
            Line end x-coordinate.
        y_end : float or Number
            Line end y-coordinate.
        dot_size : Int or int
            Dot size.
        dash_size : Int or int
            Dash size.
        space_size : Int or int
            Blank space size between dots and dashes.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        line : Line
            Created line graphics instance.

        References
        ----------
        - Graphics draw_dash_dotted_line interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_dash_dotted_line.html # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_dash_dotted_line(
        ...     x_start=50,
        ...     y_start=50,
        ...     x_end=150,
        ...     y_end=50,
        ...     dot_size=2,
        ...     dash_size=5,
        ...     space_size=3,
        ... )
        >>> line.line_color
        Color("#ffffff")

        >>> line.line_dash_dot_setting.dot_size
        Int(2)

        >>> line.line_dash_dot_setting.dash_size
        Int(5)

        >>> line.line_dash_dot_setting.space_size
        Int(3)
        """
        from apysc._display.line_dash_dot_setting import LineDashDotSetting

        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_dash_dot_setting = LineDashDotSetting(
            dot_size=dot_size,
            dash_size=dash_size,
            space_size=space_size,
            variable_name_suffix=variable_name_suffix,
        )
        line: _line.Line = _line.Line._create_with_graphics(
            graphics=self,
            start_point=Point2D(
                x=x_start, y=y_start, variable_name_suffix=variable_name_suffix
            ),
            end_point=Point2D(
                x=x_end, y=y_end, variable_name_suffix=variable_name_suffix
            ),
            variable_name_suffix=variable_name_suffix,
        )
        self._run_all_revert_methods(snapshot_name=snapshot_name)
        return line

    @final
    @arg_validation_decos.are_point_2ds(arg_position_index=1)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_polygon(
        self,
        *,
        points: Union[List[Point2D], Array[Point2D]],
        variable_name_suffix: str = "",
    ) -> "_polyg.Polygon":
        """
        Draw a polygon vector graphic. This interface is similar
        to the Polyline class (created by `move_to` or `line_to`).
        But unlike that, this interface connects the last point
        and the start point.

        Parameters
        ----------
        points : list of Point2D or Array.
            Polygon vertex points.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        polygon : Polygon
            Created polygon graphics instance.

        References
        ----------
        - Graphics draw_polygon interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_polygon.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=25, y=0),
        ...         ap.Point2D(x=0, y=50),
        ...         ap.Point2D(x=50, y=50),
        ...     ]
        ... )
        >>> polygon.fill_color
        Color("#00aaff")
        """
        polygon: _polyg.Polygon = _polyg.Polygon._create_with_graphics(
            graphics=self, points=points, variable_name_suffix=variable_name_suffix
        )
        return polygon

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    @arg_validation_decos.is_num(arg_position_index=5, optional=False)
    @arg_validation_decos.is_num(arg_position_index=6, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=7, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_triangle(
        self,
        *,
        x1: Union[float, Number],
        y1: Union[float, Number],
        x2: Union[float, Number],
        y2: Union[float, Number],
        x3: Union[float, Number],
        y3: Union[float, Number],
        variable_name_suffix: str = "",
    ) -> _triangle.Triangle:
        """
        Draw a triangle vector graphic.

        Parameters
        ----------
        x1 : Union[float, Number]
            First vertex's x coordinate.
        y1 : Union[float, Number]
            First vertex's y coordinate.
        x2 : Union[float, Number]
            Second vertex's x coordinate.
        y2 : Union[float, Number]
            Second vertex's y coordinate.
        x3 : Union[float, Number]
            Third vertex's x coordinate.
        y3 : Union[float, Number]
            Third vertex's y coordinate.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        triangle : Triangle
            Created triangle graphics instance.

        References
        ----------
        - Triangle class
            - https://simon-ritchie.github.io/apysc/en/triangle.html
        - Graphics draw_triangle interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_triangle.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.7)
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5, alpha=0.5)
        >>> triangle: ap.Triangle = sprite.graphics.draw_triangle(
        ...     x1=75,
        ...     y1=50,
        ...     x2=25,
        ...     y2=100,
        ...     x3=100,
        ...     y3=100,
        ... )
        >>> triangle.x1
        Number(75.0)
        >>> triangle.y1 = ap.Number(30)
        >>> triangle.y1
        Number(30.0)
        >>> triangle.fill_color
        Color("#00aaff")
        """
        triangle: _triangle.Triangle = _triangle.Triangle._create_with_graphics(
            graphics=self,
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            x3=x3,
            y3=y3,
            variable_name_suffix=variable_name_suffix,
        )
        return triangle

    @final
    @arg_validation_decos.is_valid_path_data_list(arg_position_index=1)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def draw_path(
        self, *, path_data_list: List[PathDataBase], variable_name_suffix: str = ""
    ) -> "_path.Path":
        """
        Draw a path vector graphics.

        Parameters
        ----------
        path_data_list : list of PathDataBase
            Target path data settings, such as the ap.PathData.MoveTo.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        path : Path
            Created path graphics instance.

        References
        ----------
        - Path class
            - https://simon-ritchie.github.io/apysc/en/path.html
        - Graphics draw_path interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html
        - PathMoveTo class
            - https://simon-ritchie.github.io/apysc/en/path_move_to.html
        - PathLineTo class
            - https://simon-ritchie.github.io/apysc/en/path_line_to.html
        - PathHorizontal class
            - https://simon-ritchie.github.io/apysc/en/path_horizontal.html
        - PathVertical class
            - https://simon-ritchie.github.io/apysc/en/path_vertical.html
        - PathClose class
            - https://simon-ritchie.github.io/apysc/en/path_close.html
        - PathBezier2D class
            - https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html
        - PathBezier2DContinual class
            - https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html
        - PathBezier3D class
            - https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html
        - PathBezier3DContinual class
            - https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)
        >>> path: ap.Path = sprite.graphics.draw_path(
        ...     path_data_list=[
        ...         ap.PathMoveTo(x=0, y=50),
        ...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),
        ...     ]
        ... )
        """
        path: _path.Path = _path.Path._create_with_graphics(
            graphics=self,
            path_data_list=path_data_list,
            variable_name_suffix=variable_name_suffix,
        )
        return path

    @final
    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Graphics("<variable_name>")`).
        """
        repr_str: str = f'{Graphics.__name__}("{self.variable_name}")'
        return repr_str

    @classmethod
    @final
    def _initialize_with_base_value(cls) -> "Graphics":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        graphics : Graphics
            An initialized graphics instance.
        """
        from apysc._type.boolean import Boolean

        sprite_: sprite.Sprite = sprite.Sprite()
        graphics: Graphics = Graphics(parent=sprite_)
        graphics.visible = Boolean(False)
        return graphics
