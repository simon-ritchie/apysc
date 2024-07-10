"""The mix-in class implementation for the material design button's label.
"""

from typing import List, Optional, Union
from apysc._color.color import Color
from apysc._display.svg_text import SvgText
from apysc._type.array import Array
from apysc._type.int import Int
from apysc._type.string import String


class MaterialButtonLabelMixIn:
    _label: String
    _label_text: SvgText
    _text_color: Color
    _font_family: Array[String]
    _font_size: Int

    def _initialize_label(
        self,
        *,
        label: Union[str, String],
        text_color: Optional[Color],
        font_family: Optional[Union[Array[String], List[str]]],
        font_size: Union[int, Int],
    ) -> None:
        """
        Initialize the label setting with the specified argument.

        Parameters
        ----------
        label : Union[str, String]
            A label text to display on this button.
        text_color : Optional[Color]
            The color of the label text.
        font_family : Optional[Union[Array[String], List[str]]]
            A font-family setting.
        font_size : Union[int, Int]
            A font-size setting.
        """
        from apysc._converter.to_apysc_val_from_builtin import get_copied_string_from_builtin_val
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        self._label = get_copied_string_from_builtin_val(
            string=label,
            variable_name_suffix=get_attr_or_variable_name_suffix(
                instance=self, value_identifier="label"
            )
        )
        pass
