"""Implementation for the SVG mask class.
"""

from apysc._display.css_mixin import CssMixIn
from apysc._display.graphics_base import GraphicsBase
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class SvgMask(
    CssMixIn,
    SetOverflowVisibleSettingMixIn,
):
    """
    The class for the object masking.

    References
    ----------
    - SvgMask class and its related interfaces
        - https://simon-ritchie.github.io/apysc/en/svg_mask.html

    Examples
    --------
    >>> import apysc as ap

    >>> _ = ap.Stage()
    >>> mask: ap.SvgMask = ap.SvgMask()
    >>> circle: ap.Circle = ap.Circle(
    ...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
    ... )
    >>> mask.add_svg_masking_object(masking_object=circle)
    >>> rectangle: ap.Rectangle = ap.Rectangle(
    ...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
    ... )
    >>> rectangle.svg_mask = mask
    """

    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_builtin_string(arg_position_index=1, optional=False)
    def __init__(
        self,
        *,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class for the SVG masking.

        Parameters
        ----------
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - SvgMask class and its related interfaces
            - https://simon-ritchie.github.io/apysc/en/svg_mask.html

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage()
        >>> mask: ap.SvgMask = ap.SvgMask()
        >>> circle: ap.Circle = ap.Circle(
        ...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
        ... )
        >>> mask.add_svg_masking_object(masking_object=circle)
        >>> rectangle: ap.Rectangle = ap.Rectangle(
        ...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
        ... )
        >>> rectangle.svg_mask = mask
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.MASK
        )
        self.variable_name = variable_name
        self._append_constructor_expression()
        self._set_overflow_visible_setting()

    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._expression import expression_data_util

        stage: Stage = get_stage()
        expression: str = f"var {self.variable_name} = {stage.variable_name}.clip();"
        expression_data_util.append_js_expression(expression=expression)

    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_fill_color_mixin(arg_position_index=1)
    def add_svg_masking_object(
        self,
        *,
        masking_object: GraphicsBase,
    ) -> None:
        """
        Add an SVG masking object to this mask. This instance uses its masking object
        to mask other SVG graphics objects.

        It is possible to add multiple masking objects to a mask.

        Parameters
        ----------
        masking_object : GraphicsBase
            The masking object to add.

        References
        ----------
        - SvgMask class and its related interfaces
            - https://simon-ritchie.github.io/apysc/en/svg_mask.html

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage()
        >>> mask: ap.SvgMask = ap.SvgMask()
        >>> circle: ap.Circle = ap.Circle(
        ...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
        ... )
        >>> mask.add_svg_masking_object(masking_object=circle)
        >>> rectangle: ap.Rectangle = ap.Rectangle(
        ...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
        ... )
        >>> rectangle.svg_mask = mask
        """
        from apysc._expression import expression_data_util

        expression: str = f"{self.variable_name}.add({masking_object.variable_name});"
        expression_data_util.append_js_expression(expression=expression)
