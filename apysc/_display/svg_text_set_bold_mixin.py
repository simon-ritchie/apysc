"""The mix-in class implementation for the `SVGText`'s `_set_bold` method.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean


class SVGTextSetBoldMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_bold(self, *, bold: Optional[Union[bool, Boolean]]) -> None:
        """
        Set a bold style setting.

        Parameters
        ----------
        bold : Optional[Union[bool, Boolean]]
            A boolean, whether a text is a bold style or not (normal).
            If a specified value is `None`, this interface ignores the setting.
        """
        from apysc._display.svg_text_bold_mixin import SVGTextBoldMixIn
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if bold is None:
            return

        if not isinstance(self, SVGTextBoldMixIn):
            raise TypeError(
                f"This method is only supported an {SVGTextBoldMixIn.__name__} "
                f"instance: {type(self).__name__}"
            )

        if isinstance(bold, bool):
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self,
                value_identifier="bold",
            )
            bold_: Boolean = Boolean(bold, variable_name_suffix=suffix)
        else:
            bold_ = bold
        self.bold = bold_
