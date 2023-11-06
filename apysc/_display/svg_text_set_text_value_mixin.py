"""The mix-in class implementation for the `SvgText`'s `_set_text_value` method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String


class SvgTextSetTextValueMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_text_value(self, *, text: Union[str, String]) -> None:
        """
        Set a text value.

        Parameters
        ----------
        text : Union[str, String]
            A target text.
        """
        from apysc._display.svg_text_text_mixin import SvgTextTextMixIn
        from apysc._string import string_util
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if not isinstance(self, SvgTextTextMixIn):
            raise TypeError(
                f"This method is only supported an {SvgTextTextMixIn.__name__} "
                f"instance: {type(self).__name__}"
            )

        if isinstance(text, str):
            text = string_util.escape_str(string=text)
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self,
                value_identifier="text",
            )
            text_: String = String(
                text,
                variable_name_suffix=suffix,
            )
        else:
            text_ = text
        self.text = text_
