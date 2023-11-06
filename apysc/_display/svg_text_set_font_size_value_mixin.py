"""The mix-in class implementation for the `SvgText`'s `_set_font_size_value` method.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class SvgTextSetFontSizeValueMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_font_size_value(self, *, font_size: Optional[Union[int, Int]]) -> None:
        """
        Set a font-size value.

        Parameters
        ----------
        font_size : Optional[Union[int, Int]]
            A target font-size value. If this value is None,
            this method does not set a font-size value.
        """
        from apysc._display.svg_text_font_size_mixin import SvgTextFontSizeMixIn
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if font_size is None:
            return
        if not isinstance(self, SvgTextFontSizeMixIn):
            raise TypeError(
                f"This method is only supported an {SvgTextFontSizeMixIn.__name__} "
                f"instance: {type(self).__name__}"
            )

        if isinstance(font_size, int):
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self, value_identifier="font_size"
            )
            font_size_: Int = Int(font_size, variable_name_suffix=suffix)
        else:
            font_size_ = font_size
        self.font_size = font_size_
