"""Path data class implementation for the SVG's `2D bezier curve` (Q).
"""

from typing import Any
from typing import Union

from typing_extensions import final

from apysc._geom.path_control_x_mixin import PathControlXMixIn
from apysc._geom.path_control_y_mixin import PathControlMixIn
from apysc._geom.path_data_base import PathDataBase
from apysc._geom.path_dest_x_mixin import PathDestXMixIn
from apysc._geom.path_dest_y_mixin import PathDestYMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class PathBezier2D(
    PathDataBase,
    PathControlXMixIn,
    PathControlMixIn,
    PathDestXMixIn,
    PathDestYMixIn,
):
    """
    Path data class for the SVG's `2D bezier curve` (Q).

    References
    ----------
    - Path class
        - https://simon-ritchie.github.io/apysc/en/path.html
    - Graphics draw_path interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html
    - PathBezier2D class
        - https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html
    - PathBezier2DContinual class
        - https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color="#fff", thickness=3)
    >>> path: ap.Path = sprite.graphics.draw_path(
    ...     path_data_list=[
    ...         ap.PathMoveTo(x=0, y=50),
    ...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),
    ...     ]
    ... )
    """

    @final
    @arg_validation_decos.is_integer(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @arg_validation_decos.is_integer(arg_position_index=3)
    @arg_validation_decos.is_integer(arg_position_index=4)
    @arg_validation_decos.is_boolean(arg_position_index=5)
    @arg_validation_decos.is_builtin_string(arg_position_index=6, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        control_x: Union[int, Int],
        control_y: Union[int, Int],
        dest_x: Union[int, Int],
        dest_y: Union[int, Int],
        *,
        relative: Union[bool, Boolean] = False,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Path data class for the SVG's `2D bezier curve` (Q).

        Parameters
        ----------
        control_x : Int or int
            X-coordinate of the bezier's control point.
        control_y : Int or int
            Y-coordinate of the bezier's control point.
        dest_x : Int or int
            X-coordinate of the destination point.
        dest_y : Int or int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            A boolean value indicates whether the path
            coordinates are relative or not (absolute).
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript's debugging.

        References
        ----------
        - Path class
            - https://simon-ritchie.github.io/apysc/en/path.html
        - Graphics draw_path interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html
        - PathBezier2D class
            - https://simon-ritchie.github.io/apysc/en/path_bezier_2d.html
        - PathBezier2DContinual class
            - https://simon-ritchie.github.io/apysc/en/path_bezier_2d_continual.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color="#fff", thickness=3)
        >>> path: ap.Path = sprite.graphics.draw_path(
        ...     path_data_list=[
        ...         ap.PathMoveTo(x=0, y=50),
        ...         ap.PathBezier2D(control_x=50, control_y=0, dest_x=100, dest_y=50),
        ...     ]
        ... )
        """
        from apysc._geom.path_label import PathLabel

        self._variable_name_suffix = variable_name_suffix
        super(PathBezier2D, self).__init__(
            path_label=PathLabel.BEZIER_2D, relative=relative
        )
        self.control_x = self._get_copied_int_from_builtin_val(
            integer=control_x, attr_identifier="control_x"
        )
        self.control_y = self._get_copied_int_from_builtin_val(
            integer=control_y, attr_identifier="control_y"
        )
        self.dest_x = self._get_copied_int_from_builtin_val(
            integer=dest_x, attr_identifier="dest_x"
        )
        self.dest_y = self._get_copied_int_from_builtin_val(
            integer=dest_y, attr_identifier="dest_y"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.

        Returns
        -------
        svg_str : str
            A SVG path string was created with the current setting.
        """
        from apysc._type import value_util

        svg_char: String = self._get_svg_char()
        svg_char_str: str = value_util.get_value_str_for_expression(value=svg_char)
        control_x_str: str = value_util.get_value_str_for_expression(
            value=self._control_x
        )
        control_y_str: str = value_util.get_value_str_for_expression(
            value=self._control_y
        )
        dest_x_str: str = value_util.get_value_str_for_expression(value=self._dest_x)
        dest_y_str: str = value_util.get_value_str_for_expression(value=self._dest_y)
        svg_str: str = (
            f'{svg_char_str} + String({control_x_str}) + " " '
            f'+ String({control_y_str}) + " " '
            f'+ String({dest_x_str}) + " " '
            f"+ String({dest_y_str})"
        )
        return svg_str

    @final
    @arg_validation_decos.is_integer(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @arg_validation_decos.is_integer(arg_position_index=3)
    @arg_validation_decos.is_integer(arg_position_index=4)
    @arg_validation_decos.is_boolean(arg_position_index=5)
    @add_debug_info_setting(module_name=__name__)
    def update_path_data(
        self,
        control_x: Union[int, Int],
        control_y: Union[int, Int],
        dest_x: Union[int, Int],
        dest_y: Union[int, Int],
        *,
        relative: Union[bool, Boolean] = False,
    ) -> None:
        """
        Update the path's data settings.

        Parameters
        ----------
        control_x : Int or int
            X-coordinate of the bezier's control point.
        control_y : Int or int
            Y-coordinate of the bezier's control point.
        dest_x : Int or int
            X-coordinate of the destination point.
        dest_y : Int or int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            A boolean value indicates whether the path
            coordinates are relative or not (absolute).

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
        ...     control_x=50, control_y=0, dest_x=100, dest_y=50
        ... )
        >>> bezier_2d.update_path_data(
        ...     control_x=150, control_y=100, dest_x=200, dest_y=150
        ... )
        >>> bezier_2d.control_x
        Int(150)

        >>> bezier_2d.control_y
        Int(100)

        >>> bezier_2d.dest_x
        Int(200)

        >>> bezier_2d.dest_y
        Int(150)
        """
        self.control_x = self._get_copied_int_from_builtin_val(
            integer=control_x, attr_identifier="control_x"
        )
        self.control_y = self._get_copied_int_from_builtin_val(
            integer=control_y, attr_identifier="control_y"
        )
        self.dest_x = self._get_copied_int_from_builtin_val(
            integer=dest_x, attr_identifier="dest_x"
        )
        self.dest_y = self._get_copied_int_from_builtin_val(
            integer=dest_y, attr_identifier="dest_y"
        )
        self.relative = self._get_copied_boolean_from_builtin_val(
            bool_val=relative, attr_identifier="relative"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap

        if not isinstance(other, PathBezier2D):
            result: ap.Boolean = ap.Boolean(False)
            return result
        return (
            self.control_x == other.control_x
            and self.control_y == other.control_y
            and self.dest_x == other.dest_x
            and self.dest_y == other.dest_y
            and self.relative == other.relative
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap

        result: ap.Boolean = self == other
        result = result.not_
        return result
