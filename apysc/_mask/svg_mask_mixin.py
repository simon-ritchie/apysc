"""The SVG mask property-related mix-in class implementation.
"""

from typing import Optional

from apysc._mask.svg_mask import SvgMask
from apysc._html.debug_mode import add_debug_info_setting
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
        """
        from apysc._expression import expression_data_util
        from apysc._validation.variable_name_validation import (
            validate_variable_name_mixin_type,
        )

        self_variable_name: str = validate_variable_name_mixin_type(
            instance=self
        ).variable_name

        if value is None:
            expression: str = f"{self_variable_name}.unmask();"
        else:
            expression = f"{self_variable_name}.maskWith({value.variable_name});"

        expression_data_util.append_js_expression(expression=expression)
        self._mask = value
