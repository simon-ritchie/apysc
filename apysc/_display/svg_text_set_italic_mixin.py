"""The mix-in class implementation for the `SvgText`'s `_set_italic` method.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean


class SvgTextSetItalicMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_italic(
        self,
        *,
        italic: Optional[Union[bool, Boolean]],
    ) -> None:
        """
        Set an italic style setting.

        Parameters
        ----------
        italic : Optional[Union[bool, Boolean]]
            A boolean whether a text is in an italic style or not (normal).
            If a specified value is `None`, this interface ignores the setting.
        """
        from apysc._display.svg_text_italic_mixin import SvgTextItalicMixIn
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if italic is None:
            return

        if not isinstance(self, SvgTextItalicMixIn):
            raise TypeError(
                f"This method is only supported an {SvgTextItalicMixIn.__name__} "
                f"instance: {type(self).__name__}"
            )

        if isinstance(italic, bool):
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self,
                value_identifier="italic",
            )
            italic_: Boolean = Boolean(italic, variable_name_suffix=suffix)
        else:
            italic_ = italic
        self.italic = italic_
