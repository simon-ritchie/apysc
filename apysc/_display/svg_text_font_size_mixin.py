"""Class implementation for the SVG text's font-size mix-in.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn


class SVGTextFontSizeMixIn(
    VariableNameMixIn,
):

    _font_size: int = 16

    @property
    @add_debug_info_setting(module_name=__name__)
    def font_size(self) -> Int:
        """
        Get a current font-size setting.

        Returns
        -------
        font_size : Int
            A current font-size setting.
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="font_size",
        )
        font_size: Int = Int(self._font_size, variable_name_suffix=suffix)
        self._append_font_size_getter_expression(font_size=font_size)
        return font_size

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_font_size_getter_expression(self, *, font_size: Int) -> None:
        """
        Append a font-size getter expression string.

        Parameters
        ----------
        font_size : Int
            A target font-size setting.
        """
        import apysc as ap

        expression: str = (
            f'{font_size.variable_name} = {self.variable_name}.font("size");'
        )
        ap.append_js_expression(expression=expression)
