"""This module is for the SVG's `horizontal line` (H) data
class implementation.
"""

from typing import Any
from typing import Union

from typing_extensions import final

from apysc._geom.path_data_base import PathDataBase
from apysc._geom.path_x_mixin import PathXMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class PathHorizontal(PathDataBase, PathXMixIn):
    """
    Path data class for the SVG's `horizontal line` (H).

    References
    ----------
    - Path class
        - https://simon-ritchie.github.io/apysc/en/path.html
    - Graphics draw_path interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html
    - PathHorizontal class
        - https://simon-ritchie.github.io/apysc/en/path_horizontal.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color="#fff", thickness=3)
    >>> path: ap.Path = sprite.graphics.draw_path(
    ...     path_data_list=[
    ...         ap.PathMoveTo(x=0, y=50),
    ...         ap.PathHorizontal(x=50),
    ...     ]
    ... )
    """

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @arg_validation_decos.is_boolean(arg_position_index=2)
    @arg_validation_decos.is_builtin_string(arg_position_index=3, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        x: Union[float, Number],
        *,
        relative: Union[bool, Boolean] = False,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Path data class for the SVG's `horizontal line` (H).

        Parameters
        ----------
        x : float or Number
            X-coordinate of the destination point.
        relative : bool or Boolean, default False
            A boolean value indicates whether the path
            coordinates are relative or not (absolute).
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - Path class
            - https://simon-ritchie.github.io/apysc/en/path.html
        - Graphics draw_path interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html
        - PathHorizontal class
            - https://simon-ritchie.github.io/apysc/en/path_horizontal.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color="#fff", thickness=3)
        >>> path: ap.Path = sprite.graphics.draw_path(
        ...     path_data_list=[
        ...         ap.PathMoveTo(x=0, y=50),
        ...         ap.PathHorizontal(x=50),
        ...     ]
        ... )
        """
        from apysc._geom.path_label import PathLabel

        self._variable_name_suffix = variable_name_suffix
        super(PathHorizontal, self).__init__(
            path_label=PathLabel.HORIZONTAL, relative=relative
        )
        self.x = self._get_copied_number_from_builtin_val(
            float_or_num=x, attr_identifier="x"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.

        Returns
        -------
        svg_str : str
            An SVG path string was created with the current setting.
        """
        from apysc._type import value_util

        svg_char: String = self._get_svg_char()
        svg_char_str: str = value_util.get_value_str_for_expression(value=svg_char)
        x_str: str = value_util.get_value_str_for_expression(value=self._x)
        svg_str: str = f"{svg_char_str} + String({x_str})"
        return svg_str

    @final
    @arg_validation_decos.is_num(arg_position_index=1)
    @arg_validation_decos.is_boolean(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def update_path_data(
        self, x: Union[float, Number], *, relative: Union[bool, Boolean] = False
    ) -> None:
        """
        Update the path's data settings.

        Parameters
        ----------
        x : float or Number
            X-coordinate of the destination point.
        relative : bool or Boolean, default False
            A boolean value indicates whether the path
            coordinates are relative or not (absolute).

        Examples
        --------
        >>> import apysc as ap
        >>> path_horizontal: ap.PathHorizontal = ap.PathHorizontal(x=50)
        >>> path_horizontal.update_path_data(x=100)
        >>> path_horizontal.x
        Number(100.0)
        """
        self.x = self._get_copied_number_from_builtin_val(
            float_or_num=x, attr_identifier="x"
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

        if not isinstance(other, PathHorizontal):
            result: ap.Boolean = ap.Boolean(
                False, variable_name_suffix=self._variable_name_suffix
            )
            return result
        return self.x == other.x and self.relative == other.relative

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
