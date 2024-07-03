"""The mix-in class implementation for the `SvgText`'s `_set_font_family` method.
"""

from typing import List
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._converter.list_of_strs_to_array import list_of_strs_to_array_of_string
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.string import String


class SvgTextSetFontFamilyMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_font_family(
        self,
        *,
        font_family: Optional[Union[Array[String], List[str]]],
    ) -> None:
        """
        Set a font-family value.

        Parameters
        ----------
        font_family : Optional[Array[String]]
            A font-family setting.
        """
        from apysc._display.svg_text_font_family_mixin import SvgTextFontFamilyMixIn
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if not isinstance(self, SvgTextFontFamilyMixIn):
            raise TypeError(
                f"This method is only supported an {SvgTextFontFamilyMixIn.__name__} "
                f"instance: {type(self).__name__}"
            )
        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="font_family",
        )
        font_family_: Optional[Array[String]] = list_of_strs_to_array_of_string(
            optional_list_or_arr=font_family,
            variable_name_suffix=suffix,
        )

        if font_family_ is None:
            return
        self.font_family = font_family_
