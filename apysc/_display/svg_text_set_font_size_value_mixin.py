"""The mix-in class implementation for the `_set_font_size_value` method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class SVGTextSetFontSizeValueMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_font_size_value(self, *, font_size: Union[int, Int]) -> None:
        """
        Set a font-size value.

        Parameters
        ----------
        font_size : Union[int, Int]
            A target font-size value.
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )
        from apysc._display.svg_text_font_size_mixin import SVGTextFontSizeMixIn

        if not isinstance(self, SVGTextFontSizeMixIn):
            raise TypeError(
                f"This method is only supported a {SVGTextFontSizeMixIn.__name__} "
                f"instance: {type(self)}"
            )

        if isinstance(font_size, int):
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self, value_identifier="font_size"
            )
            font_size_: Int = Int(font_size, variable_name_suffix=suffix)
        else:
            font_size_ = font_size
        self.font_size = font_size_
