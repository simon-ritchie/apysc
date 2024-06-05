"""The SVG mask property-related mix-in class implementation.
"""

from typing import Optional

from apysc._html.debug_mode import add_debug_info_setting
from apysc._mask.svg_mask import SvgMask
from apysc._validation import arg_validation_decos


class SvgMaskMixIn:
    """
    The SVG mask property-related mix-in class.
    """

    _mask: Optional[SvgMask] = None

    @property
    @add_debug_info_setting(module_name=__name__)
    def svg_mask(self) -> Optional[SvgMask]:
        """
        Get an SVG mask setting. If the mask is not set, this property becomes `None`.

        Returns
        -------
        mask : Optional[SvgMask]
            A mask setting.

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
        >>> assert rectangle.svg_mask == mask
        """
        return self._mask

    @svg_mask.setter
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_svg_mask(arg_position_index=1, optional=True)
    def svg_mask(self, value: Optional[SvgMask]) -> None:
        """
        Set an SVG mask setting.

        Parameters
        ----------
        value : Optional[SvgMask]
            SVG mask setting to set.

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
        >>> assert rectangle.svg_mask == mask
        """
        from apysc._expression import expression_data_util
        from apysc._validation.variable_name_validation import (
            validate_variable_name_mixin_type,
        )

        self_variable_name: str = validate_variable_name_mixin_type(
            instance=self
        ).variable_name

        if value is None:
            expression: str = f"{self_variable_name}.unclip();"
        else:
            expression = f"{self_variable_name}.clipWith({value.variable_name});"

        expression_data_util.append_js_expression(expression=expression)
        self._mask = value
