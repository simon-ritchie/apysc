"""This module is for SVG's `continual 3D bezier curve` (S)
path data class implementations.
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
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class PathBezier3DContinual(
    PathDataBase,
    PathControlXMixIn,
    PathControlMixIn,
    PathDestXMixIn,
    PathDestYMixIn,
):
    """
    Path data class for SVG's `continual 3D bezier curve` (S).

    References
    ----------
    - Path class
        - https://simon-ritchie.github.io/apysc/en/path.html
    - Graphics draw_path interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html
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
    ...         ap.PathBezier3D(
    ...             control_x1=0,
    ...             control_y1=0,
    ...             control_x2=50,
    ...             control_y2=0,
    ...             dest_x=50,
    ...             dest_y=50,
    ...         ),
    ...         ap.PathBezier3DContinual(
    ...             control_x=100, control_y=100, dest_x=100, dest_y=50
    ...         ),
    ...     ]
    ... )
    """

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    @arg_validation_decos.is_boolean(arg_position_index=5, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=6, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        control_x: Union[float, Number],
        control_y: Union[float, Number],
        dest_x: Union[float, Number],
        dest_y: Union[float, Number],
        *,
        relative: Union[bool, Boolean] = False,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Path data class for SVG's `continual 3D bezier curve` (S).

        Parameters
        ----------
        control_x : float or Number
            X-coordinate of the bezier's control point.
        control_y : float or Number
            Y-coordinate of the bezier's control point.
        dest_x : float or Number
            X-coordinate of the destination point.
        dest_y : float or Number
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            A boolean value indicates whether the path coordinates
            are relative or not (absolute).
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - Path class
            - https://simon-ritchie.github.io/apysc/en/path.html
        - Graphics draw_path interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html
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
        ...         ap.PathBezier3D(
        ...             control_x1=0,
        ...             control_y1=0,
        ...             control_x2=50,
        ...             control_y2=0,
        ...             dest_x=50,
        ...             dest_y=50,
        ...         ),
        ...         ap.PathBezier3DContinual(
        ...             control_x=100, control_y=100, dest_x=100, dest_y=50
        ...         ),
        ...     ]
        ... )
        """
        from apysc._geom.path_label import PathLabel

        self._variable_name_suffix = variable_name_suffix
        super(PathBezier3DContinual, self).__init__(
            path_label=PathLabel.BEZIER_3D_CONTINUAL, relative=relative
        )
        self.control_x = self._get_copied_number_from_builtin_val(
            float_or_num=control_x, attr_identifier="control_x"
        )
        self.control_y = self._get_copied_number_from_builtin_val(
            float_or_num=control_y, attr_identifier="control_y"
        )
        self.dest_x = self._get_copied_number_from_builtin_val(
            float_or_num=dest_x, attr_identifier="dest_x"
        )
        self.dest_y = self._get_copied_number_from_builtin_val(
            float_or_num=dest_y, attr_identifier="dest_y"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.

        Returns
        -------
        svg_str : str
            An SVG path string was created with the
            current setting.
        """
        from apysc._type.value_util import get_value_str_for_expression

        svg_char: String = self._get_svg_char()
        svg_char_str: str = get_value_str_for_expression(value=svg_char)
        control_x_str: str = get_value_str_for_expression(value=self._control_x)
        control_y_str: str = get_value_str_for_expression(value=self._control_y)
        dest_x_str: str = get_value_str_for_expression(value=self._dest_x)
        dest_y_str: str = get_value_str_for_expression(value=self._dest_y)
        svg_str: str = (
            f"{svg_char_str} + String({control_x_str}) "
            f'+ " " + String({control_y_str}) '
            f'+ " " + String({dest_x_str}) '
            f'+ " " + String({dest_y_str})'
        )
        return svg_str

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    @arg_validation_decos.is_num(arg_position_index=4, optional=False)
    @arg_validation_decos.is_boolean(arg_position_index=5, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def update_path_data(
        self,
        control_x: Union[float, Number],
        control_y: Union[float, Number],
        dest_x: Union[float, Number],
        dest_y: Union[float, Number],
        *,
        relative: Union[bool, Boolean] = False,
    ) -> None:
        """
        Update the path's data settings.

        Parameters
        ----------
        control_x : float or Number
            X-coordinate of the bezier's control point.
        control_y : float or Number
            Y-coordinate of the bezier's control point.
        dest_x : float or Number
            X-coordinate of the destination point.
        dest_y : float or Number
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            A boolean value indicates whether the path
            coordinates are relative or not (absolute).

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_3d_continual = ap.PathBezier3DContinual(
        ...     control_x=100, control_y=100, dest_x=100, dest_y=50
        ... )
        >>> bezier_3d_continual.update_path_data(
        ...     control_x=150, control_y=150, dest_x=150, dest_y=100
        ... )
        >>> bezier_3d_continual.control_x
        Number(150.0)

        >>> bezier_3d_continual.control_y
        Number(150.0)

        >>> bezier_3d_continual.dest_x
        Number(150.0)

        >>> bezier_3d_continual.dest_y
        Number(100.0)
        """
        self.control_x = self._get_copied_number_from_builtin_val(
            float_or_num=control_x, attr_identifier="control_x"
        )
        self.control_y = self._get_copied_number_from_builtin_val(
            float_or_num=control_y, attr_identifier="control_y"
        )
        self.dest_x = self._get_copied_number_from_builtin_val(
            float_or_num=dest_x, attr_identifier="dest_x"
        )
        self.dest_y = self._get_copied_number_from_builtin_val(
            float_or_num=dest_y, attr_identifier="dest_y"
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
        if not isinstance(other, PathBezier3DContinual):
            result: Boolean = Boolean(
                False, variable_name_suffix=self._variable_name_suffix
            )
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
        result: Boolean = self == other
        result = result.not_
        return result
